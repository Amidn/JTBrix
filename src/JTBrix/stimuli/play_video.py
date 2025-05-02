import os
from flask import render_template_string

def register_video(app, video_path):
    """
    Registers the /video route in the shared Flask app.
    Displays a start button which plays the video with sound when clicked.
    
    Args:
        app: Flask app instance.
        video_path: Path to the video inside the 'static' folder, e.g. 'static/FB.mp4'.
    """
    video_filename = os.path.basename(video_path)

    @app.route('/video')
    def serve_video():
        return f"""
        <html>
        <head>
            <title>Video</title>
            <style>
                body, html {{
                    margin: 0;
                    padding: 0;
                    height: 100%;
                    background-color: black;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }}
                #startBtn {{
                    position: absolute;
                    z-index: 2;
                    padding: 20px 40px;
                    font-size: 24px;
                    background-color: #28a745;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    cursor: pointer;
                }}
                video {{
                    display: none;
                    width: 100%;
                    height: 100%;
                    object-fit: contain;
                }}
            </style>
        </head>
        <body>
            <button id="startBtn" onclick="startVideo()">Start Video</button>
            <video id="videoPlayer" onended="window.location.href='/question/1'">
                <source src="/static/{os.path.basename(video_path)}" type="video/mp4">
                Your browser does not support the video tag.
            </video>

            <script>
                function startVideo() {{
                    const video = document.getElementById('videoPlayer');
                    const button = document.getElementById('startBtn');
                    button.style.display = 'none';
                    video.style.display = 'block';
                    video.play();
                    video.requestFullscreen().catch(e => console.log("Fullscreen not allowed:", e));
                }}
            </script>
        </body>
        </html>
        """