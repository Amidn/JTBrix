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
        return render_template_string(f"""
        <!DOCTYPE html>
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
                    flex-direction: column;
                }}
                video {{
                    width: 100%;
                    height: 100%;
                    display: none;
                    object-fit: contain;
                }}
                #startBtn {{
                    font-size: 24px;
                    padding: 15px 30px;
                    background-color: #28a745;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    cursor: pointer;
                }}
            </style>
        </head>
        <body>
            <button id="startBtn">Start Video</button>
            <video id="videoPlayer" controls onended="window.location.href='/question/1'">
                <source src="/static/{video_filename}" type="video/mp4">
                Your browser does not support the video tag.
            </video>

            <script>
                document.getElementById("startBtn").onclick = function () {{
                    const video = document.getElementById("videoPlayer");
                    this.style.display = "none";
                    video.style.display = "block";
                    video.play().catch(e => console.log("Playback error:", e));
                    video.requestFullscreen().catch(e => console.log("Fullscreen not supported:", e));
                }};
            </script>
        </body>
        </html>
        """)