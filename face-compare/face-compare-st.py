import streamlit as st
# import cv2
import numpy as np
from PIL import Image
import face_recognition
import matplotlib.pyplot as plt

def compare_faces(image1, image2):
    # Convert images to numpy arrays
    img1_array = np.array(image1)
    img2_array = np.array(image2)

    # Find face locations and encodings
    face_locations1 = face_recognition.face_locations(img1_array)
    face_encodings1 = face_recognition.face_encodings(img1_array, face_locations1)

    face_locations2 = face_recognition.face_locations(img2_array)
    face_encodings2 = face_recognition.face_encodings(img2_array, face_locations2)

    if not face_encodings1 or not face_encodings2:
        return "No faces found in one or both images."

    # Compare faces
    results = face_recognition.compare_faces([face_encodings1[0]], face_encodings2[0])
    distance = face_recognition.face_distance([face_encodings1[0]], face_encodings2[0])
    print(distance)

    return results[0], distance[0]

def create_similarity_gauge(distance):
    fig, ax = plt.subplots(figsize=(10, 2))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Create gradient
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    # Plot gradient
    ax.imshow(gradient, aspect='auto', extent=[0, 1, 0, 1], cmap='RdYlGn_r')

    # Add marker for distance
    ax.plot(distance, 0.5, 'v', color='black', markersize=20)

    # Add text
    ax.text(0.01, 0.7, 'More Similar', fontsize=12, va='center')
    ax.text(0.99, 0.7, 'Less Similar', fontsize=12, va='center', ha='right')
    ax.text(distance, 0.2, f'{distance:.2f}', fontsize=12, ha='center', va='center')

    return fig

st.title("Face Comparison App")

# File uploaders
uploaded_file1 = st.file_uploader("Choose the first image", type=["jpg", "jpeg", "png"])
uploaded_file2 = st.file_uploader("Choose the second image", type=["jpg", "jpeg", "png"])

if uploaded_file1 is not None and uploaded_file2 is not None:
    # Display uploaded images
    image1 = Image.open(uploaded_file1)
    image2 = Image.open(uploaded_file2)

    col1, col2 = st.columns(2)
    with col1:
        st.image(image1, caption="First Image", use_column_width=True)
    with col2:
        st.image(image2, caption="Second Image", use_column_width=True)

    # Compare faces
    if st.button("Compare Faces"):
        result, distance = compare_faces(image1, image2)

        if isinstance(result, str):
            st.write(result)
        else:
            match_result = "Yes" if result else "No"
            match_color = "green" if result else "red"
            match_icon = "✅" if result else "❌"
            st.markdown(f"<h2 style='text-align: center; color: {match_color};'>{match_icon} Face Match: {match_result}</h2>", unsafe_allow_html=True)

            # Display similarity gauge
            st.write("Face Similarity:")
            similarity_gauge = create_similarity_gauge(distance)
            st.pyplot(similarity_gauge)

            st.write("Note: Lower distance indicates higher similarity.")

st.write("Upload two images to compare the faces in them.")

