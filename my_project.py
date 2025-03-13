import serial
import serial.tools.list_ports  # Optional: for listing available ports
import time
import openai
import gradio as gr

# Replace with your OpenAI API key
openai.api_key = "YOUR_API_KEY"

# Connect to Arduino (Change COM3 to your Arduino port)
arduino = serial.Serial(port="COM3", baudrate=9600, timeout=1)  
time.sleep(2)  # Wait for Arduino to initialize

def chat_with_gpt(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    response_text = response["choices"][0]["message"]["content"]

    # Send response to Arduino (truncate if too long for LCD)
    arduino.write((response_text[:32] + "\n").encode())  
    return response_text  # Display in Gradio UI

# Create Gradio Chatbot
iface = gr.Interface(fn=chat_with_gpt, inputs="text", outputs="text", title="ChatGPT LCD Chatbot")
iface.launch()
