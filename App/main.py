import streamlit as st

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    # url_input = st.text_input("Enter a URL:", value="https://www.accenture.com/in-en/careers/jobdetails?id=ATCI-4636508-S1789347_en&title=Data%20Modeler")
    # submit_button = st.button("Submit")

    # if submit_button:
    #     try:
    #         loader = WebBaseLoader([url_input])
    #         data = clean_text(loader.load().pop().page_content)
    #         portfolio.load_portfolio()
    #         jobs = llm.extract_jobs(data)
    #         for job in jobs:
    #             skills = job.get('skills', [])
    #             links = portfolio.query_links(skills)
    #             email = llm.write_mail(job, links)
    #             st.code(email, language='markdown')
    #     except Exception as e:
    #         st.error(f"An Error Occurred: {e}")
# Streamlit UI

    st.title("Cold Email Generator for Job Applications")
            
    st.write("""
                This application helps you draft a professional cold email for a job application. 
                Provide the job description, required skills, and your personal experience, and the application will generate an email tailored to your inputs.
            """)
        
            # Input fields
    job_description = st.text_area("Job Description", placeholder="Paste the job description here...")
    required_skills = st.text_area("Required Skills", placeholder="List the skills required for the job...")
    user_experience = st.text_area("Your Experience", placeholder="Describe your experience and qualifications...")
        
            # Generate cold email
    if st.button("Generate Email"):
        if job_description and required_skills and user_experience:
                with st.spinner("Generating email...Please wait"):
                        # email = generate_cold_email(job_description, required_skills, user_experience)
                    st.subheader("Generated Cold Email:")
                        # st.write(email)
        else:
            st.error("Please fill in all the fields.")


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, clean_text)

