# Changelog

All notable changes to the AI Agents Health Companion project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

#### Critical Bug Fixes
- **Profile Agent Direct Selection**: Fixed `'dict' object has no attribute 'text'` error when selecting Profile & Onboarding agent directly instead of through router. ProfileOnboardingWrapper now consistently returns ChatResult objects regardless of activation path.

## [2.1.0] - 2024-08-24

### Added - Profile & Onboarding System

#### New Features
- **Complete User Profile Management System**
  - Multi-step onboarding workflow (conditions � medications � routines � confirmation)
  - Resumable onboarding sessions with persistent state management
  - Profile update and modification capabilities
  - Comprehensive data validation with Pydantic v2 schemas

#### New Components
- **Profile Data Models** (`profile_and_onboarding/schema.py`)
  - `UserProfile` with conditions, medications, and routines
  - `Condition`, `Medication`, `Routine` core data models
  - Structured agent response models for onboarding steps
  - Change proposal models for profile updates

- **Atomic Storage System** (`profile_and_onboarding/storage.py`)
  - JSON-based profile storage with atomic write operations
  - Windows-compatible file handling with proper temp file management
  - Profile event logging for audit trails
  - Idempotency support for duplicate operation prevention

- **Onboarding Workflow** (`profile_and_onboarding/onboarding_workflow.py`)
  - 4-step guided onboarding process
  - Specialized agents for conditions, medications, and routines extraction
  - Session state management with step tracking
  - Profile preview and confirmation system

- **Profile Update Agent** (`profile_and_onboarding/updater_agent.py`)
  - Natural language profile modification requests
  - Structured change proposals with user confirmation
  - Batch update operations with rollback support

#### Enhanced Routing System
- **Extended Router Schema** (`health_advisor/router/schema.py`)
  - Added profile-specific intents (onboarding, profile_update, profile_view)
  - Profile action classification for granular routing
  - Enhanced confidence scoring for profile-related requests

- **Master Agent Enhancements** (`agents.py`)
  - Session-aware routing with onboarding flow persistence
  - Profile intent handling with proper state management
  - Improved error handling and fallback responses
  - AI response logging for debugging

### Fixed

#### Critical Bug Fixes
- **Session State Persistence**: Fixed MasterAgent creating new wrapper instances on each call, causing session state loss
- **Unicode Encoding Issues**: Removed all emoji characters causing `'charmap' codec` errors on Windows
- **Agent Response Extraction**: Added proper handling for Agno v2 RunResponse objects vs. direct structured responses
- **Preview Step Logic**: Fixed onboarding summary display that was inverted (only showing when no message)
- **Pydantic Schema Validation**: Added "onboarding" as valid source value for Condition and Medication models

#### Workflow Improvements
- **Step Transition Logic**: Fixed immediate transition to preview step after routines completion
- **Medications Agent Instructions**: Enhanced to handle simple medication names like "ubrelvy"
- **Confirmation Processing**: Improved preview agent to recognize various confirmation phrases ("yes please", "confirm", etc.)
- **Error Handling**: Added validation for empty medications lists with user-friendly error messages

### Changed

#### Code Quality Improvements
- **Pydantic Compatibility**: Fixed `.model_dump()` vs `.dict()` method calls for cross-version compatibility
- **Agent Instructions**: Refined with specific examples and clearer guidance
- **Console Logging**: Added structured debug output for workflow progression
- **Port Configuration**: Changed default port to 7861 to avoid conflicts

#### Architecture Enhancements
- **Session Management**: Centralized session state storage in MasterAgent
- **Workflow Orchestration**: Improved state tracking across multi-step processes
- **Agent Response Processing**: Standardized structured data extraction patterns

### Technical Details

#### New Dependencies
- Enhanced Pydantic v2 usage with advanced validation features
- Expanded Agno v2 integration with proper RunResponse handling

#### Database Schema
- JSON-based profile storage with versioning support
- Event logging for profile changes and onboarding completion
- Atomic file operations for data integrity

#### Testing Coverage
- Comprehensive manual testing workflow documented
- Error condition handling verified
- Cross-platform compatibility (Windows focus) validated

### Documentation

#### Implementation Reports
- **Complete implementation report**: `docs/Linda/profile_onboarding_implementation_report.md`
- **Multi-modal health logger report**: `docs/Linda/multimodal_health_logger_implementation_report.md`

#### Project Documentation
- **CLAUDE.md**: Comprehensive project guide for AI assistants
- **README updates**: Enhanced project description and setup instructions

### Migration Notes

#### For Developers
- Profile system requires "onboarding" as valid source value in existing data
- Session state management now centralized in MasterAgent
- Unicode characters removed from console output for Windows compatibility

#### For Users
- New onboarding flow accessible via "new here" or similar phrases
- Profile data stored in local JSON files for privacy
- Multi-step workflows maintain state across interactions

---

## [2.0.0] - Previous Release

### Added
- Multi-modal health logging with image analysis
- Coach and Recall agent specialists  
- Router-based intent classification
- ChromaDB integration for conversation memory

### Infrastructure
- Agno v2 workflow framework integration
- Gradio web interface for multi-modal input
- OpenAI GPT-4o-mini model integration

---

*For detailed implementation information, see the reports in `docs/Linda/`*