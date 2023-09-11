class NumericQuestionsController < ApplicationController
  def create_first_question
    # Generate random values for wave speed (v) and frequency (f)
    wave_speed = rand(100..300)  # Adjust the range as needed
    frequency = rand(1..10)      # Adjust the range as needed
    wavelength = (wave_speed.to_f / frequency.to_f).round(2)

    # Load the image data (assuming you have the same image for all players)
    image_path = Rails.root.join('public', 'images', 'longitud_onda.jpg')
    image_data = File.read(image_path)

    # Create a new NumericQuestion with the random parameters
    nq = NumericQuestion.create!(
      question: "Si una onda se propaga a una velocidad de _ metros por segundo (m/s) y su frecuencia es de _ Hz, ¿cuál es la longitud de onda de esta onda?",
      image_data: image_data,
      difficulty: 1,
      topic: "TEMA 1"
    )

    # Create Parameters for the question
    Parameter.create!(
      [
        { number: wave_speed, numeric_question: nq },
        { number: frequency, numeric_question: nq }
      ]
    )

    # Create a NumericAnswer with the calculated wavelength
    NumericAnswer.create!(
      answer: wavelength,
      correct: true,
      numeric_question: nq,
      equation: "v / f",
      hint: 'Recuerda que la longitud de onda es la distancia entre dos puntos en la misma fase de la onda.'
    )

    # Redirect or render as needed
  end

  def create_second_question
    wave_speed = rand(300..600)  # Adjust the range as needed
    frequency = rand(300..400)
    wavelength = (wave_speed.to_f / frequency.to_f).round(2)

    image_path = Rails.root.join('public', 'images', 'sonido_.jpg')
    image_data = File.read(image_path)

    # Create a new NumericQuestion with the random parameters
    nq = NumericQuestion.create!(
      question: "Si un músico toca una nota musical que tiene una frecuencia de 440 Hz. Si esta nota se propaga como una onda sonora en el aire a una velocidad de 343 metros por segundo, calcula:

      a) ¿Cuál es la longitud de onda de esta onda sonora?
      b) Si la frecuencia de la nota se duplica, ¿cómo cambiará la longitud de onda?
      ",
      image_data: image_data,
      difficulty: 1,
      topic: "TEMA 1"
    )

    # Create Parameters for the question
    Parameter.create!(
      [
        { number: wave_speed, numeric_question: nq },
        { number: frequency, numeric_question: nq }
      ]
    )

    # Create a NumericAnswer with the calculated wavelength
    NumericAnswer.create!(
      answer: wavelength,
      correct: true,
      numeric_question: nq,
      equation: "v / f",
      hint: 'Recuerda que la longitud de onda es la distancia entre dos puntos en la misma fase de la onda.'
    )

    NumericAnswer.create!(
      answer: (wavelength/2).round(2),
      correct: true,
      numeric_question: nq,
      equation: "v / f",
      hint: 'Recuerda que la frecuencia es que tan larga es la onda, por lo que si se duplica, la longitud de onda se reduce a la mitad.')

    # Redirect or render as needed
  end
end
