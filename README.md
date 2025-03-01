# YouTube Data Scraper

## Description
This project is a YouTube Data Scraper that extracts public information from YouTube videos and channels using the YouTube Data API. The scraper allows users to retrieve video comments and channel details via a simple web interface.

## Features
- Extract comments from a given YouTube video URL.
- Retrieve video details from a YouTube channel homepage.
- User-friendly web interface built with Flask.
- Data export in CSV format for easy analysis.

## Technologies Used
- **Programming Language:** Python
- **Framework:** Flask
- **API:** YouTube Data API v3
- **Libraries:** requests, pandas, Flask, json, csv

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/youtube_scraper.git
   cd youtube_scraper
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Obtain a YouTube API Key:
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project and enable the YouTube Data API v3.
   - Generate an API key and add it to the `.env` file:
     ```
     YOUTUBE_API_KEY=your_api_key_here
     ```

## Usage
1. Run the Flask server:
   ```sh
   python app.py
   ```

2. Open the web interface:
   - Visit `http://127.0.0.1:5000/` in your browser.
   
3. Enter a YouTube video or channel URL and extract the required data.

4. Download the extracted data as a CSV file.

## Limitations
- The scraper only works within YouTube API rate limits.
- Private or restricted content cannot be accessed.
- Scraping emails, phone numbers, or personal data is **not possible** due to YouTube’s policies.

## Future Improvements
- Add more detailed analytics for extracted data.
- Implement database storage for historical scraping.
- Improve UI/UX with better design and functionality.


**Preview**

![1](https://github.com/user-attachments/assets/f77016f0-1d6a-4e0f-a07e-1d72983f2c1e)

**CSV_Example**

![csv_example](https://github.com/user-attachments/assets/bbca32d2-61a4-435a-984a-2f5c8184c6ab)
