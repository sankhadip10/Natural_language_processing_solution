from dotenv import load_dotenv
from azure.ai.language.questionanswering import QuestionAnsweringClient
from azure.core.credentials import AzureKeyCredential
import os

def main():
    try:
        # Get Configuration Settings
        load_dotenv()
        ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
        ai_key = os.getenv('AI_SERVICE_KEY')
        ai_project_name = os.getenv('QA_PROJECT_NAME')
        ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

        # Create client using endpoint and key
        credential = AzureKeyCredential(ai_key)
        qa_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)

        # Submit a question and display the answer
        question = "What is your question?"
        response = qa_client.query(
            model=ai_project_name,
            question=question,
            deployment=ai_deployment_name
        )

        print("Answer:", response['answers'][0]['answer'])

    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()
