import streamlit as st
import streamlit.components.v1 as components

# HTML and JavaScript code to access the webcam, draw a rectangle, and display it
html_code = """
    <html>
        <body>
            <h2>Live Camera Feed with Rectangle (416x416)</h2>
            <!-- Camera feed with 416x416 dimensions -->
            <div style="position:relative; width:416px; height:416px;">
                <video id="myVidPlayer" controls muted autoplay width="416" height="416" style="position: absolute;"></video>
                <canvas id="myCanvas" width="416" height="416" style="position: absolute; top: 0; left: 0;"></canvas>
            </div>
            
            <script type="text/javascript">
                // Selector for video and canvas elements
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

                // Function to draw the rectangle within the 416x416 camera window
                function drawRectangle() {
                    ctx.clearRect(0, 0, canvas.width, canvas.height); // Clear previous frames
                    ctx.strokeStyle = 'red'; // Set rectangle color
                    ctx.lineWidth = 4; // Set rectangle border width
                    ctx.strokeRect(50, 50, 200, 150); // Draw a rectangle at (50, 50) with width=200 and height=150
                }

                // Draw the rectangle continuously, synchronizing with video frame rate
                video.addEventListener('play', function() {
                    function update() {
                        if (!video.paused && !video.ended) {
                            drawRectangle();
                            requestAnimationFrame(update); // Call update for the next frame
                        }
                    }
                    update();
                });
            </script>
        </body>
    </html>
"""

# Embed the HTML code using Streamlit's component API
components.html(html_code, height=500)
