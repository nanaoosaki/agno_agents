# External API Errors Documentation

This document tracks common errors encountered with external APIs and their solutions to prevent future occurrences.

## OpenAI Structured Output API Errors

### Error: "Invalid schema for response_format: $ref cannot have keywords {'description'}"

**Status:** ✅ **RESOLVED**

**Date:** 2025-01-15  
**Context:** Health Logger v3 implementation  
**API:** OpenAI Chat Completions with `response_format` (Structured Output)

#### Problem Description

When using Pydantic models with OpenAI's structured output feature (`response_model` in Agno), OpenAI generates a JSON schema. If the Pydantic model contains nested `BaseModel` classes with `Field(description=...)`, OpenAI creates `$ref` references in the JSON schema that include `description` keywords, which violates the JSON Schema specification.

#### Error Message

```
ERROR API status error from OpenAI API: Error code: 400 - {'error': 
{'message': "Invalid schema for response_format 'RouterOutput': 
context=('properties', 'fields'), $ref cannot have keywords {'description'}.", 
'type': 'invalid_request_error', 'param': 'response_format', 'code': None}}
```

#### Root Cause

The issue occurs when:
1. Using nested Pydantic models as `response_model`
2. Nested models have `Field(description="...")` parameters
3. OpenAI converts the Pydantic model to JSON schema
4. The generated schema includes `$ref` objects with `description` properties
5. JSON Schema specification doesn't allow additional keywords alongside `$ref`

#### Example Problematic Code

```python
class Fields(BaseModel):
    severity: Optional[int] = Field(None, description="Severity level 0-10")  # ❌ PROBLEMATIC
    location: Optional[str] = Field(None, description="Body location")        # ❌ PROBLEMATIC

class RouterOutput(BaseModel):
    fields: Fields = Field(default_factory=Fields, description="Extracted health data")  # ❌ PROBLEMATIC

# Using with Agno
agent = Agent(
    response_model=RouterOutput,  # ❌ FAILS - generates invalid schema
    # ...
)
```

#### Solutions

**Solution 1: Remove descriptions from nested models**
```python
class Fields(BaseModel):
    severity: Optional[int] = None  # ✅ WORKS - no description
    location: Optional[str] = None  # ✅ WORKS - no description

class RouterOutput(BaseModel):
    fields: Fields = Field(default_factory=Fields)  # ✅ WORKS - no description
```

**Solution 2: Flatten the schema (recommended)**
```python
class SimpleRouterOutput(BaseModel):
    """Flattened schema for OpenAI compatibility"""
    intent: Literal["observation", "episode_create", "episode_update", "intervention", "query"]
    condition: Optional[str] = None
    severity: Optional[int] = None        # ✅ FLAT - no nesting
    location: Optional[str] = None        # ✅ FLAT - no nesting
    notes: Optional[str] = None           # ✅ FLAT - no nesting
    link_strategy: Literal["same_episode", "new_episode", "unknown"]
    confidence: float = 0.0

# Convert back to complex structure after LLM call
@classmethod
def to_complex(cls, simple: SimpleRouterOutput) -> RouterOutput:
    # Convert flat structure to nested structure
    pass
```

**Solution 3: Use string descriptions in docstrings**
```python
class Fields(BaseModel):
    """Health data fields extracted from user message"""
    severity: Optional[int] = None  # Severity level 0-10
    location: Optional[str] = None  # Body location
    notes: Optional[str] = None     # Additional notes
```

#### Best Practices

1. **For OpenAI Structured Output:**
   - Use flat schemas without nested BaseModel classes
   - Avoid `Field(description=...)` in models used as `response_model`
   - Use docstrings and comments for documentation instead

2. **For Internal Use:**
   - Create rich, nested models with descriptions for internal processing
   - Convert between simple/complex schemas as needed

3. **Schema Design Pattern:**
   ```python
   # Simple schema for OpenAI
   class SimpleSchema(BaseModel):
       field1: str
       field2: int
   
   # Complex schema for internal use
   class ComplexSchema(BaseModel):
       section1: SectionModel = Field(..., description="Rich description")
       section2: SectionModel = Field(..., description="Rich description")
       
       @classmethod
       def from_simple(cls, simple: SimpleSchema) -> "ComplexSchema":
           # Conversion logic
           pass
   ```

#### Prevention Checklist

- [ ] Remove `description` from `Field()` in models used as `response_model`
- [ ] Avoid nested `BaseModel` classes in OpenAI schemas
- [ ] Test schema generation before deployment
- [ ] Use flat schemas for LLM communication
- [ ] Document field meanings in docstrings/comments instead

#### Related Issues

- This error has occurred in previous Health Logger implementations (v1, v2)
- Similar issues may occur with other structured output APIs
- Agno framework abstracts OpenAI calls but inherits these limitations

## Agno Tool Decorator Errors

### Error: "'Function' object is not callable"

**Date:** 2025-01-15  
**Context:** Health Logger v3 workflow step execution  
**Library:** Agno Tools  

#### Problem Description

When using the `@tool` decorator on functions that are meant to be called directly in workflow steps (not by agents), the functions become `agno.tools.Function` objects instead of regular Python functions, resulting in a `TypeError: 'Function' object is not callable` error.

#### Error Message

```
WARNING  Step Process failed (attempt 1): 'Function' object is not callable
TypeError: 'Function' object is not callable
```

#### Root Cause

The issue occurs when:
1. Functions are decorated with `@tool` for future Agent use
2. Same functions are called directly in workflow steps  
3. `@tool` decorator wraps functions as `agno.tools.Function` objects
4. Function objects are only callable within Agent context, not as regular functions

#### Example Problematic Code

```python
from agno.tools import tool

@tool  # ❌ PROBLEMATIC - makes function uncallable outside Agent
def fetch_data(param: str) -> str:
    return f"Data for {param}"

# In workflow step:
def process_step(step_input):
    data = fetch_data("test")  # ❌ FAILS - 'Function' object is not callable
```

#### Solution

**Remove `@tool` decorators** from functions called directly in workflow steps:

```python
# ✅ WORKS - regular Python function
def fetch_data(param: str) -> str:
    return f"Data for {param}"

# In workflow step:
def process_step(step_input):
    data = fetch_data("test")  # ✅ WORKS - regular function call
```

#### Best Practices

1. **For Workflow Functions:**
   - Use regular Python functions (no `@tool` decorator)
   - Call directly in workflow steps
   - Keep function signatures simple and clear

2. **For Agent Tools:**
   - Use `@tool` decorator for functions agents should call
   - Add to agent's `tools=[]` parameter
   - Don't call these directly in workflow code

3. **Hybrid Approach:**
   ```python
   # Regular function for direct calls
   def _internal_fetch_data(param: str) -> str:
       return f"Data for {param}"
   
   # Tool wrapper for agents
   @tool
   def fetch_data_tool(param: str) -> str:
       """Tool for agents to fetch data"""
       return _internal_fetch_data(param)
   ```

#### Prevention Checklist

- [ ] Use `@tool` only for Agent tools, not workflow functions
- [ ] Call regular Python functions directly in workflow steps
- [ ] Test function calls outside of Agent context
- [ ] Separate internal functions from Agent tools when both are needed

#### References

- [OpenAI Structured Outputs Documentation](https://platform.openai.com/docs/guides/structured-outputs)
- [JSON Schema Specification - $ref behavior](https://json-schema.org/understanding-json-schema/structuring.html#ref)
- [Pydantic JSON Schema Generation](https://docs.pydantic.dev/latest/concepts/json_schema/)
- [Agno Tools Documentation](https://docs.agno.com/tools/introduction)
- [Agno Tool Decorator](https://docs.agno.com/tools/tool-decorator)