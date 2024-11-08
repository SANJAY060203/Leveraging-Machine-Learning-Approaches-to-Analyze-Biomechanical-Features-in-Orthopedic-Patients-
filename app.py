import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Biomechanical Analysis", page_icon=":hospital:", layout="wide")

logo_path = "biomechanics.jpeg"  
st.image(logo_path, width=910)  

st.title('Biomechanical Analysis for Orthopedic Patients')

uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file is not None:
    
    df = pd.read_csv(uploaded_file)
    
    st.write("Dataset Overview:")
    st.dataframe(df.head())

    patient_id = st.number_input('Enter Patient ID:', min_value=int(df['Patient_ID'].min()), max_value=int(df['Patient_ID'].max()), step=1)

    if st.button('Analyze'):
        
        patient_data = df[df['Patient_ID'] == patient_id]
        
        if not patient_data.empty:
            
            pelvic_incidence_mean = patient_data['Pelvic_Incidence'].mean()
            pelvic_tilt_numeric_mean = patient_data['Pelvic_Tilt_Numeric'].mean()
            lumbar_lordosis_angle_mean = patient_data['Lumbar_Lordosis_Angle'].mean()
            sacral_slope_mean = patient_data['Sacral_Slope'].mean()
            degree_spondylolisthesis_mean = patient_data['Degree_Spondylolisthesis'].mean()
            patient_class = patient_data['Class'].iloc[0]
            
            
            st.subheader(f'Analysis Results for Patient {patient_id}')
            st.write(f'Mean Pelvic Incidence: {pelvic_incidence_mean}')
            st.write(f'Mean Pelvic Tilt Numeric: {pelvic_tilt_numeric_mean}')
            st.write(f'Mean Lumbar Lordosis Angle: {lumbar_lordosis_angle_mean}')
            st.write(f'Mean Sacral Slope: {sacral_slope_mean}')
            st.write(f'Mean Degree of Spondylolisthesis: {degree_spondylolisthesis_mean}')
            st.write(f'Patient Class: {patient_class}')
            
            
            st.subheader('Diagnosis and Treatment Recommendations')

            if patient_class == 'Hernia':
                st.write("**Diagnosis:** The patient's biomechanical parameters indicate potential hernia-related abnormalities.")
                st.write("**Treatment Recommendations:**")
                st.write("- Physical therapy to alleviate symptoms and strengthen surrounding muscles.")
                st.write("- Pain management through medications or alternative therapies.")
                st.write("- In severe cases, surgical intervention may be necessary.")
            elif patient_class == 'Spondylolisthesis':
                st.write("**Diagnosis:** The patient's biomechanical parameters indicate potential spondylolisthesis.")
                st.write("**Treatment Recommendations:**")
                st.write("- Physical therapy to stabilize the spine and reduce pain.")
                st.write("- Use of braces or support devices to maintain spinal alignment.")
                st.write("- Surgical intervention may be considered for severe cases.")
            else:
                st.write("**Diagnosis:** The patient's biomechanical parameters are within normal ranges.")
                st.write("**Treatment Recommendations:**")
                st.write("- Regular exercise to maintain spinal health.")
                st.write("- Routine check-ups to monitor any changes in biomechanical features.")

            
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.plot(['Pelvic Incidence', 'Pelvic Tilt', 'Lumbar Lordosis', 'Sacral Slope', 'Spondylolisthesis'], 
                    [pelvic_incidence_mean, pelvic_tilt_numeric_mean, lumbar_lordosis_angle_mean, sacral_slope_mean, degree_spondylolisthesis_mean],
                    marker='o', linestyle='-', color='b')
            ax.set_title(f'Biomechanical Features for Patient {patient_id}')
            ax.set_xlabel('Feature')
            ax.set_ylabel('Values')
            ax.grid(True)
            
            
            st.pyplot(fig)
        else:
            st.warning(f"No data available for Patient ID {patient_id}")
else:
    st.info('Please upload a CSV file to proceed.')

st.header('Developer Profiles', divider="blue")
st.header('Team Hustlers')
st.write('Sanjay')
st.write('Santhosh')
st.write('Vishwa')
st.write('Fayaas')
st.header('Guided by', divider="violet")
st.write('Mr.Maruthupandi')
