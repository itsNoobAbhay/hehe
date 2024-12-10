import streamlit as st

# HTML and JavaScript code to access the webcam and display the video feed
html_code = """
    <html>
        <body>
            <h2>Live Camera Feed</h2>
            <video id="video" width="640" height="480" autoplay></video>
            <script>
                // Access the camera
                navigator.mediaDevices.getUserMedia({ video: true })
                    .then(function (stream) {
                        // Display the camera feed in the video element
                        document.getElementById('video').srcObject = stream;
                    })
                    .catch(function (error) {
                        console.log("Error accessing the camera: ", error);
                    });
            </script>
        </body>
    </html>
"""

# Display the HTML code in Streamlit
st.markdown(html_code, unsafe_allow_html=True)
