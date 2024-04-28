import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts.prompt import PromptTemplate
from langchain.callbacks import get_openai_callback

#fix Error: module 'langchain' has no attribute 'verbose'
import langchain
langchain.verbose = False

class Chatbot:

    def __init__(self, model_name, temperature, vectors):
        self.model_name = model_name
        self.temperature = temperature
        self.vectors = vectors

    qa_template = """
        You are a helpful AI assistant named Claim Correspondent. You are to create notices and claims based on FIDIC clauses. Use the contractor's perspective, describing and locating relevant clauses in the given data by user txt file and using them in the notices. The attached document contains clauses on which you need to base your logic for creating a notice or claim. Make sure to follow the pattern for generating claims as displayed later in the attached document.
        If you don't know the answer, just say you don't know. Do NOT try to make up an answer. Only generate claims and notices rather than telling the process or steps to do these. Use the data provided by the user to generate claims and notices accordingly. Use the logic presented in the document's attached ie clauses. If according to data a claim or notice should not be generated, then don't. 
        If the question is unrelated to the context, politely respond, "I am sorry, I cannot generate Claim or notice on your query".
        Use as much detail as possible when responding. Make sure to just generate claims and notices only.

        context: {context}
        =========
        question: {question}
        ======
        """

    QA_PROMPT = PromptTemplate(template=qa_template, input_variables=["context","question" ])

    def conversational_chat(self, query):
        """
        Start a conversational chat with a model via Langchain
        """
        llm = ChatOpenAI(model_name=self.model_name, temperature=self.temperature)

        retriever = self.vectors.as_retriever()


        chain = ConversationalRetrievalChain.from_llm(llm=llm,
            retriever=retriever, verbose=True, return_source_documents=True, max_tokens_limit=4097, combine_docs_chain_kwargs={'prompt': self.QA_PROMPT})

        chain_input = {"question": query, "chat_history": st.session_state["history"]}
        result = chain(chain_input)

        st.session_state["history"].append((query, result["answer"]))
        #count_tokens_chain(chain, chain_input)
        return result["answer"]


def count_tokens_chain(chain, query):
    with get_openai_callback() as cb:
        result = chain.run(query)
        st.write(f'###### Tokens used in this conversation : {cb.total_tokens} tokens')
    return result 

    
    
