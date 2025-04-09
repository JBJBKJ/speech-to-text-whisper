from flask import Flask, request, jsonify
import whisper

app = Flask(__name__)
model = whisper.load_model("tiny")  # Используем модель base, можно выбрать другую

@app.route("/transcribe", methods=["POST"])
def transcribe():
    file = request.files["file"]  # Получаем файл от пользователя
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Сохраняем временно файл
    file_path = "temp.wav"
    file.save(file_path)

    # Преобразуем аудио в текст
    result = model.transcribe(file_path)

    # Возвращаем результат
    return jsonify({"text": result["text"]})

if __name__ == "__main__":
    app.run(debug=True)
