# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the bin/rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: "Star Wars" }, { name: "Lord of the Rings" }])
#   Character.create(name: "Luke", movie: movies.first)

# require 'faker'
# mcq = MultipleChoiceQuestion.create!(question: "What is the capital of France?", difficulty: 1)
# choice = Choice.create!(answer: "Paris", correct: true, multiple_choice_question: mcq)

mcq = MultipleChoiceQuestion.create!(question: "Cuál de las siguientes opciones describe mejor la velocidad de una onda?", difficulty: 1, hint: "Piensa en cómo se mide la velocidad de una onda, como en la velocidad del sonido o la velocidad de una onda en una cuerda.")
Choice.create!([
  { answer: "La distancia entre dos crestas sucesivas.", correct: false, multiple_choice_question: mcq },
  { answer: "El tiempo que tarda una onda en completar un ciclo.", correct: false, multiple_choice_question: mcq },
  { answer: "La distancia que recorre una onda en un cierto tiempo.", correct: true, multiple_choice_question: mcq },
  { answer: "La cantidad de energía transportada por la onda.", correct: false, multiple_choice_question: mcq }
])

mcq = MultipleChoiceQuestion.create!(question: "Qué es la longitud de onda de una onda?", difficulty: 1,topic: "TEMA 1", hint:'Imagina una onda en el agua y cómo puedes medir la distancia entre dos crestas o dos valles sucesivos.')
Choice.create!([
  { answer: "El número de ciclos por segundo.", correct: false, multiple_choice_question: mcq },
  { answer: "La distancia entre dos puntos en la misma fase de la onda.", correct: true, multiple_choice_question: mcq },
  { answer: "La velocidad de la onda", correct: false, multiple_choice_question: mcq },
  { answer: "La amplitud de la onda.", correct: false, multiple_choice_question: mcq }
])

mcq = MultipleChoiceQuestion.create!(question: "Si aumentas la frecuencia de una onda sin cambiar su velocidad, ¿qué sucederá con su longitud de onda?", difficulty: 1,topic: "TEMA 1", hint: 'Piensa en cómo las ondas se comprimen cuando aumentas la frecuencia.')
Choice.create!([
  { answer: "Aumentará.", correct: true, multiple_choice_question: mcq },
  { answer: "Disminuirá.", correct: false, multiple_choice_question: mcq },
  { answer: "Permanecerá igual.", correct: false, multiple_choice_question: mcq },
  { answer: "No se puede determinar con la información proporcionada.", correct: false, multiple_choice_question: mcq }
])

mcq = MultipleChoiceQuestion.create!(question: "Cuál de las siguientes unidades se utiliza comúnmente para medir la frecuencia de las ondas?", difficulty: 1,topic: "TEMA 1", hint: 'Es una unidad específica utilizada para contar cuántos ciclos o vibraciones ocurren por segundo.')
Choice.create!([
  { answer: "Metros por segundo (m/s).", correct: false, multiple_choice_question: mcq },
  { answer: "Hertz (Hz).", correct: true, multiple_choice_question: mcq },
  { answer: "Newtons (N).", correct: false, multiple_choice_question: mcq },
  { answer: "Julios (J).", correct: false, multiple_choice_question: mcq }
])

mcq = MultipleChoiceQuestion.create!(question: "Si la velocidad de una onda aumenta mientras su frecuencia permanece constante, ¿qué sucede con su longitud de onda?", difficulty: 1,topic: "TEMA 1")
Choice.create!([
  { answer: "Aumenta.", correct: true, multiple_choice_question: mcq },
  { answer: "Disminuye.", correct: false, multiple_choice_question: mcq },
  { answer: "Permanece igual.", correct: false, multiple_choice_question: mcq },
  { answer: "Se invierte.", correct: false, multiple_choice_question: mcq }
])

mcq = MultipleChoiceQuestion.create!(question: "Cuál de las siguientes afirmaciones es verdadera acerca de la amplitud de una onda?", difficulty: 1,topic: "TEMA 1", hint: 'Imagina una onda en una cuerda y cómo la amplitud se refiere a cuán lejos se desvía de su posición de reposo.')
Choice.create!([
  { answer: "Representa la distancia entre dos crestas sucesivas.", correct: false, multiple_choice_question: mcq },
  { answer: "Indica la velocidad de la onda.", correct: false, multiple_choice_question: mcq },
  { answer: "Mide la altura de la onda desde su posición de equilibrio.", correct: true, multiple_choice_question: mcq },
  { answer: "Está relacionada con la frecuencia de la onda.", correct: false, multiple_choice_question: mcq }
])

mcq = MultipleChoiceQuestion.create!(question: "Si duplicas la frecuencia de una onda y mantienes constante su velocidad, ¿cómo se verá afectada su longitud de onda?", difficulty: 1,topic: "TEMA 1", hint: 'Piensa en cómo esto afecta a la separación entre las crestas o valles.')
Choice.create!([
  { answer: "Se duplicará.", correct: false, multiple_choice_question: mcq },
  { answer: "Se reducirá a la mitad.", correct: true, multiple_choice_question: mcq },
  { answer: "Permanecerá igual.", correct: false, multiple_choice_question: mcq },
  { answer: "Dependerá de la amplitud de la onda.", correct: false, multiple_choice_question: mcq }
])

mcq = MultipleChoiceQuestion.create!(question: "Qué característica de una onda se relaciona con la cantidad de energía que transporta?", difficulty: 1,topic: "TEMA 1", hint: 'Piensa en cómo una onda grande puede tener más energía que una onda pequeña.')
Choice.create!([
  { answer: "Frecuencia.", correct: false, multiple_choice_question: mcq },
  { answer: "Velocidad.", correct: false, multiple_choice_question: mcq },
  { answer: "Amplitud.", correct: true, multiple_choice_question: mcq },
  { answer: "Longitud de onda.", correct: false, multiple_choice_question: mcq }
])

mcq = MultipleChoiceQuestion.create!(question: "Si una onda tiene una frecuencia de 50 Hz, ¿cuántos ciclos completa en un segundo?", difficulty: 1, topic: "TEMA 1", hint: 'Piensa en cuántos ciclos o vibraciones ocurren en un solo segundo.')
Choice.create!([
  { answer: "5 ciclos.", correct: false, multiple_choice_question: mcq },
  { answer: "20 ciclos.", correct: false, multiple_choice_question: mcq },
  { answer: "50 ciclos.", correct: true, multiple_choice_question: mcq },
  { answer: "100 ciclos.", correct: false, multiple_choice_question: mcq }
])

mcq = MultipleChoiceQuestion.create!(question: "Qué tipo de onda se produce cuando las partículas del medio oscilan perpendicularmente a la dirección de propagación de la onda?", difficulty: 1,topic: "TEMA 1", hint:'Imagina una onda en una cuerda donde las partículas de la cuerda se mueven hacia arriba y abajo, no en la dirección de la onda.')
Choice.create!([
  { answer: "Onda longitudinal.", correct: false, multiple_choice_question: mcq },
  { answer: "Onda transversal.", correct: true, multiple_choice_question: mcq },
  { answer: "Onda estacionaria.", correct: false, multiple_choice_question: mcq },
  { answer: "Onda periódica.", correct: false, multiple_choice_question: mcq }
])



################################### Numerical Questions #########################################

wave_speed = rand(100..300)
frequency = rand(1..10)
wavelength = (wave_speed.to_f / frequency.to_f).round(2)

image_path = Rails.root.join('public', 'images', 'longitud_onda.png')
image_data = File.read(image_path)

nq = NumericQuestion.create!(
  pregunta: "Si una onda se propaga a una velocidad de _ metros por segundo (m/s) y su frecuencia es de _ Hz, ¿cuál es la longitud de onda de esta onda?",
  image_data: image_data,
  difficulty: 1,
  topic: "TEMA 1"
)

# Create Parameters for the question
Parameter.create!(
  [
    { name: 'Wave Speed', number: wave_speed, numeric_question: nq },
    { name: 'Frequency', number: frequency, numeric_question: nq }
  ]
)


# Create a NumericAnswer with the calculated wavelength
NumericAnswer.create!(
  respuesta: wavelength,
  correct: true,
  numeric_question: nq,
  equation: "v / f",
  hint: 'Recuerda que la longitud de onda es la distancia entre dos'
)

# db/seeds.rb

# # Create a NumericQuestion
# nq = NumericQuestion.create!(
#   question: "If x = _, what's half of x and what's twice x?",
#   difficulty: 1,
#   topic: "Math"
# )

# # Create a Parameter for the question
# Parameter.create!(
#   name: 'x',
#   min_value: 1,
#   max_value: 10,
#   numeric_question: nq
# )

# # Create NumericAnswers for the question
# NumericAnswer.create!(
#   answer: 'x / 2',
#   correct: true,
#   numeric_question: nq,
#   hint: 'Half of x is obtained by dividing x by 2.'
# )

# NumericAnswer.create!(
#   answer: 'x * 2',
#   correct: true,
#   numeric_question: nq,
#   hint: 'Twice x is obtained by multiplying x by 2.'
# )
