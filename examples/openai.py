import openai

openai.api_key = "YOUR_API_KEY"

models = openai.models.list()
for model in models.data:
    print(model.id)
