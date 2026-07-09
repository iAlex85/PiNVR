import asyncio
import os
import logging

logger = logging.getLogger("PiNVR.RecordingEngine")

class RecordingManager:
    def __init__(self):
        self.active_processes = {}

    async def start_continuous_recording(self, camera_id, stream_url, camera_name):
        output_dir = f"storage/cam_{camera_id}_{camera_name}"
        os.makedirs(output_dir, exist_ok=True)
        
        cmd = [
            "ffmpeg", "-rtsp_transport", "tcp", "-i", stream_url,
            "-c", "copy", "-f", "segment", "-segment_time", "900",
            f"{output_dir}/rec_%Y%m%d_%H%M%S.mp4"
        ]
        
        process = await asyncio.create_subprocess_exec(*cmd)
        self.active_processes[camera_id] = process
        logger.info(f"Started recording: {camera_name}")

recording_engine = RecordingManager()