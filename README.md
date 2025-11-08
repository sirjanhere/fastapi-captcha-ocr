1. Activate your virtual environment:

   macOS / Linux
   ```bash
   source venv/bin/activate
   ```

   Windows (PowerShell)
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   Windows (Command Prompt)
   ```bat
   .\venv\Scripts\activate.bat
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

4. While the server is running, submit the following URL in the TDS portal:
   http://localhost:8000/captcha
