import streamlit as st

st.markdown("""
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

st.write("\n")
st.markdown("""
    <div style="text-align:center; background-color:#fff; padding: 20px; border-radius: 16px; margin-bottom: 4rem;">
        <h1 style="margin: 0; padding:0;">Welcome to</h1>
        <h1 style="margin: 0; padding:0;">AI-MED Models UK</h1>
    </div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("<h3>AI-MED Models</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:justify;'>Aimed is a rapidly growing software startup specializing in artificial intelligence (AI) solutions for the healthcare industry. Partner companies founded in 2021, the company has developed a proprietary AI healthcare platform that enhances diagnostic improves patients outcome by optimising treatment plans and predicting potential health issues before comes to critical stages.</p>", unsafe_allow_html=True)

with col2:
    st.markdown("<h3>Why Choose AI-MED Models?</h3>", unsafe_allow_html=True)

    # Add feature points with icons and text
    st.markdown("""
        <div>
            <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 1rem;">
                <i class="fas fa-heart" style="color: #FB8C00; font-size: 20px;"></i>
                <span style="font-size: 16px;">Early disease detection through analysis of medical imaging and patient data.</span>
            </div>
            <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 1rem;">
                <i class="fas fa-user-md" style="color: #FB8C00; font-size: 20px;"></i>
                <span style="font-size: 16px;">Personalized treatment plans based on genetic information and patient history.</span>
            </div>
            <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 1rem;">
                 <i class="fas fa-capsules" style="color: #FB8C00; font-size: 20px;"></i>
                <span style="font-size: 16px;">Drug discovery and development optimization.</span>
            </div>
            <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 1rem;">
                <i class="far fa-hospital" style="color: #FB8C00; font-size: 20px;"></i>
                <span style="font-size: 16px;">Hospital resource management and patient flow prediction.</span>
            </div>
            <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 1rem;">
                <i class="fas fa-shield-alt" style="color: #FB8C00; font-size: 20px;"></i>
                <span style="font-size: 16px;">Epidemic outbreak forecasting and management.</span>
            </div>
        </div>
    """, unsafe_allow_html=True)



# Add a "Visit Us" button at the end
st.markdown("""
    <div style="text-align:center; margin-top: 3rem;">
        <a href="https://www.aimedmodels.com" target="_blank">
            <button style="
                background-color: #FB8C00; 
                color: white; 
                font-size: 16px; 
                padding: 15px 30px; 
                border-radius: 12px; 
                border: none; 
                cursor: pointer;
                text-align: center;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s;">
                Visit AI-MED Models
            </button>
        </a>
    </div>
""", unsafe_allow_html=True)