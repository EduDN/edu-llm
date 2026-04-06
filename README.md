# edu-llm


### Distribución de probabilidad
Para entender los LLMs, la **distribución de probabilidad** es un concepto base. A partir del contexto previo, el modelo asigna un porcentaje de probabilidad a cada palabra de su vocabulario. Luego, utilizando estos valores, el modelo selecciona la próxima palabra a generar, permitiendo crear texto coherente.

Si no existe el contexto, a pesar de tener un mayor porcentaje la palabras asignada no tendría sentido, como es en el caso de la función random.choices , la cual se basa en el porcentaje asignada a las palabras para definir cuál elegirá. 


