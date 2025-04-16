# AI Economic Impact Simulator

This Flask web application lets you explore how AI-driven automation affects jobs, government budgets, and Universal Basic Income (UBI). You can tweak settings like the number of jobs lost to AI, taxes on automation, and UBI payments to see their impact on the economy, all with easy-to-read results and visuals.

## Features

- **Interactive Inputs**: Change settings like jobs displaced, wages, taxes, and UBI amounts.
- **Real-Time Results**: Instantly see updates to tax losses, revenue, and fiscal impacts.
- **Visualizations**: A bar chart shows the financial effects in trillions of USD.
- **Simple Explanations**: Each setting comes with a clear description for easy understanding.

## Installation

Here’s how to get the app running on your computer, even if you’re new to this!

### What You Need

- **Python 3.x**: This is the program that runs the app. Download it from python.org if you don’t have it. Follow the installer’s steps—check “Add Python to PATH” during setup.
- **pip**: This comes with Python and helps install extra tools. It’s ready if Python is installed.

### Steps

1. **Get the App Files**:

   - If you use Git (a tool for downloading code), open a terminal (search “cmd” on Windows or “terminal” on Mac) and type:

     ```bash
     git clone https://github.com/your-repo/ai-economic-impact-simulator.git
     ```

   - No Git? Just download the ZIP file from the GitHub page and unzip it to a folder.

2. **Go to the App Folder**:

   - In your terminal, move to the folder by typing:

     ```bash
     cd ai-economic-impact-simulator
     ```

   - Replace “ai-economic-impact-simulator” with wherever you unzipped the files.

3. **Install the Tools**:

   - Type this in the terminal to add what the app needs:

     ```bash
     pip install -r requirements.txt
     ```

   - If there’s no `requirements.txt` file, just install Flask by typing:

     ```bash
     pip install flask
     ```

4. **Start the App**:

   - Run it by typing:

     ```bash
     python app.py
     ```

   - You’ll see a message like `* Running on http://127.0.0.1:5000/`. That means it’s working!

5. **Open the App**:

   - Open your web browser (like Chrome or Firefox) and go to: `http://127.0.0.1:5000/`. You’re ready to use it!

## User Guide

### Settings You Can Change

- **Jobs Displaced by AI (millions)**: How many jobs AI might replace by 2030. Starts at 500 million.
- **Average Global Wage ($ per year)**: What workers earn on average worldwide. Starts at $16,000.
- **Labor Tax Rate (% of wage income)**: How much of wages goes to taxes. Starts at 17.7%.
- **Automation Tax per Job ($ per year)**: A tax on companies for each job AI takes. Starts at $10,000.
- **UBI Payment per Person ($ per year)**: Money given to each displaced worker. Starts at $10,000.
- **Government Efficiency Savings (% of GDP)**: Savings from AI helping governments, as a percentage. Starts at 2.285% ($2.4 trillion).
- **AI-Driven GDP Growth (% increase)**: How much AI boosts the economy. Starts at 15%.
- **Total Global Workforce (millions)**: All workers worldwide. Starts at 3,650 million.

### How to Use It

1. **Change Settings**: Type new numbers into the boxes. Try raising jobs displaced to see what happens!
2. **Hit Calculate**: Click the “Calculate” button to update everything.
3. **Check Results**: A table shows things like tax losses and total fiscal impact in trillions of USD and as percentages.
4. **Look at the Chart**: A bar chart makes it easy to see the money impacts.
5. **Learn More**: Scroll down for simple explanations of each setting.

### Example

- **Starting Point**: With 500 million jobs lost, you get a $1.0 trillion surplus.
- **Big Change**: Set jobs displaced to 1,000 million (1 billion)—now it’s a $0.4 trillion deficit. This shows why policies matter!

## Libraries Needed

- **Flask**: Runs the web app. Install with `pip install flask`.
- **Chart.js**: Makes the charts. It’s included when you run the app, so no extra install needed.

## Notes

- Money is in 2023 US dollars.
- The starting global GDP is $105 trillion, growing with AI boosts.
- This is a learning tool with simple models—real life might be different.

## Help

- **App Won’t Start?**: Check Flask is installed (`pip install flask`) and you’re in the right folder.
- **No Chart?**: Ensure your browser allows JavaScript (it’s usually on by default).
- **Typing Issues?**: Use numbers only in the boxes, or it might not work.

Need more help? Check the Flask docs or Chart.js docs.