import streamlit as st
import streamlit.components.v1 as components

# HTML and JavaScript code for accessing the webcam (with resize and back camera)
html_code = """
    <html>
        <body>
            <h2>Live Camera Feed (Back Camera, 416x416)</h2>
            <video id="myVidPlayer" controls muted autoplay width="416" height="416"></video>
            <script type="text/javascript">
                // Selector for your <video> element
                const video = document.querySelector('#myVidPlayer');

                // Access the back camera (if available)
                window.navigator.mediaDevices.enumerateDevices().then(devices => {
                    const videoDevices = devices.filter(device => device.kind === 'videoinput');
                    const backCamera = videoDevices.find(device => device.label.toLowerCase().includes('back')); // Select back camera

                    const constraints = {
                        video: {
                            deviceId: backCamera ? { exact: backCamera.deviceId } : undefined,
                            width: { ideal: 416 },
                            height: { ideal: 416 }
                        }
                    };

                    window.navigator.mediaDevices.getUserMedia(constraints)
                        .then(stream => {
                            video.srcObject = stream;
                            video.onloadedmetadata = (e) => {
                                video.play();
                            };
                        })
                        .catch(() => {
                            alert('You need to give permission to use the Webcam.');
                        });
                });
            </script>
        </body>
    </html>
"""

# Embed the HTML code using Streamlit's component API
components.html(html_code, height=500)
