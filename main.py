import streamlit as st
import streamlit.components.v1 as components

# HTML and JavaScript code to access webcam, resize it, and draw a rectangle on it
html_code = """
    <html>
        <body>
            <h2>Live Camera Feed with Rectangle (416x416)</h2>
            <video id="myVidPlayer" controls muted autoplay width="416" height="416"></video>
            <canvas id="myCanvas" width="416" height="416"></canvas>
            
            <script type="text/javascript">
                // Selector for your <video> element and <canvas> element
                const video = document.querySelector('#myVidPlayer');
                const canvas = document.querySelector('#myCanvas');
                const ctx = canvas.getContext('2d');

                // Access the back camera (if available)
                window.navigator.mediaDevices.enumerateDevices().then(devices => {
                    const videoDevices = devices.filter(device => device.kind === 'videoinput');
                    const backCamera = videoDevices.find(device => device.label.toLowerCase().includes('back'));

                    const constraints = {
                        video: {
                            deviceId: backCamera ? { exact: backCamera.deviceId } : undefined,
                            width: { ideal: 416 },
                            height: { ideal: 416 }
                        }
                    };

                    // Access the webcam stream
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

                // Draw a rectangle on the canvas over the video
                function drawRectangle() {
                    ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear previous frames
                    ctx.strokeStyle = 'red'; // Set rectangle color
                    ctx.lineWidth = 4; // Set rectangle border width
                    ctx.strokeRect(50, 50, 200, 150); // Draw a rectangle at (50,50) with width=200 and height=150
                }

                // Call drawRectangle every 100ms to keep it drawing while video is playing
                setInterval(drawRectangle, 100);
            </script>
        </body>
    </html>
"""

# Embed the HTML code using Streamlit's component API
components.html(html_code, height=500)
