import streamlit as st

# HTML and JavaScript code for accessing the webcam
html_code = """
    <html>
        <body>
            <h2>Live Camera Feed</h2>
            <video id="myVidPlayer" controls muted autoplay width="640" height="480"></video>
            <script type="text/javascript">
                // Selector for your <video> element
                const video = document.querySelector('#myVidPlayer');

                // Core logic to access the webcam
                window.navigator.mediaDevices.getUserMedia({ video: true })
                    .then(stream => {
                        video.srcObject = stream;
                        video.onloadedmetadata = (e) => {
                            video.play();
                        };
                    })
                    .catch(() => {
                        alert('You have to give the browser permission to run the Webcam ;(');
                    });
            </script>
        </body>
    </html>
"""

# Display the HTML and JavaScript in Streamlit
st.markdown(html_code, unsafe_allow_html=True)
