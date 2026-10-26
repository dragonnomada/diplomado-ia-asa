# Módulo 1.1 — Fundamentos de sistemas cognitivos

> **Diplomado en Inteligencia Artificial**  
> **Módulo 1:** Sistemas cognitivos y representación del conocimiento
> **Tema:** Fundamentos de sistemas cognitivos

## Introducción

Estas notas introducen los sistemas cognitivos como sistemas capaces de **percibir**, **representar conocimiento**, **razonar bajo incertidumbre**, **aprender**, **decidir** y **actuar** para alcanzar objetivos. El énfasis no está sólo en imitar al ser humano, sino en comprender qué componentes computacionales permiten transformar datos del entorno en decisiones justificables.

Al finalizar el tema, la persona participante podrá:

- distinguir un sistema cognitivo de un programa reactivo, un sistema experto y un modelo aislado de aprendizaje automático;
- explicar el ciclo percepción–cognición–acción y el papel de la memoria, las metas y la retroalimentación;
- comparar los enfoques simbólico, conexionista, probabilístico, corporizado e híbrido;
- reconocer que representar conocimiento implica seleccionar qué aspectos del mundo conservar y cómo utilizarlos;
- formular un problema sencillo de decisión bajo incertidumbre mediante un POMDP;
- anticipar cómo estos fundamentos conducen a representación del conocimiento, lógica difusa, ontologías, grafos y optimización de procesos.

---

## 1. ¿Qué es un sistema cognitivo?

### 1.1 Definición de trabajo

Un **sistema cognitivo** es un agente —biológico, artificial o sociotécnico— que mantiene y actualiza información acerca de sí mismo y de su entorno para seleccionar acciones orientadas a metas, incluso cuando la información es incompleta, ambigua o cambiante.

Una definición operacional útil es:

> Un sistema es cognitivo en la medida en que integra percepción, memoria, representación, inferencia, aprendizaje, decisión y acción dentro de un ciclo de retroalimentación.

Esta definición evita dos confusiones:

1. **Cognición no es sinónimo de conciencia.** Un sistema puede exhibir capacidades cognitivas funcionales sin que exista evidencia de experiencia subjetiva.
2. **IA no es automáticamente un sistema cognitivo.** Un clasificador de imágenes aislado realiza una tarea inteligente, pero no necesariamente posee metas persistentes, memoria, razonamiento ni capacidad de actuar y aprender en un entorno.

### 1.2 Sistema cognitivo, arquitectura cognitiva y modelo de IA

| Concepto | Qué describe | Ejemplo | Alcance |
|---|---|---|---|
| Algoritmo o modelo de IA | Una función o procedimiento específico | clasificador de objetos, modelo de lenguaje | una o varias tareas delimitadas |
| Arquitectura cognitiva | Los componentes estables y sus mecanismos de interacción | Soar, ACT-R | marco general para construir o explicar cognición |
| Sistema cognitivo | El agente completo situado en un entorno | asistente operacional que observa, razona, recomienda y aprende | ciclo integral percepción–acción |
| Sistema sociotécnico cognitivo | Personas, procedimientos y tecnología que conocen y deciden conjuntamente | centro de control aeroportuario | cognición distribuida entre actores |

ACT-R se presenta como una teoría computacional para simular y comprender la cognición humana; Soar organiza la conducta deliberada como selección y aplicación de operadores sobre estados. Son **arquitecturas**, no aplicaciones completas por sí mismas ([ACT-R, Carnegie Mellon University](https://act-r.psy.cmu.edu/); [manual de Soar, University of Michigan](https://soar.eecs.umich.edu/soar_manual/02_TheSoarArchitecture/)).

### 1.3 El ciclo cognitivo mínimo

```text
                 ┌──────────── memoria / conocimiento ────────────┐
                 │                                                 │
entorno → sensores/datos → percepción → estado o creencia → decisión → acción
   ↑                                  ↕                ↕              │
   └────────────── nueva evidencia ← resultado ← evaluación ──────────┘
                                      │
                                  aprendizaje
```

El ciclo es continuo:

1. **Percibir:** transformar señales, registros o mensajes en observaciones utilizables.
2. **Atender:** seleccionar qué información es relevante dada una meta y recursos limitados.
3. **Representar:** construir un estado interno, concepto, regla, vector, probabilidad o grafo acerca del mundo.
4. **Recordar:** recuperar conocimiento semántico, episodios previos o procedimientos.
5. **Inferir y predecir:** obtener consecuencias, hipótesis o futuros posibles.
6. **Decidir y planear:** comparar acciones según metas, restricciones, riesgo y costo.
7. **Actuar:** modificar el entorno o emitir una recomendación.
8. **Evaluar y aprender:** comparar el resultado con lo esperado y actualizar conocimiento o política.

La cognición aparece en el **acoplamiento** entre estos elementos. Una percepción exacta puede ser inútil si la representación no conserva lo relevante; una decisión matemáticamente óptima puede ser peligrosa si parte de observaciones sesgadas; una acción correcta puede degradarse si no existe retroalimentación.

---

## 2. Elementos más importantes que se deben comprender

### 2.1 Agente, entorno, metas y límites

Todo análisis comienza identificando:

- **agente:** quién percibe y decide;
- **entorno:** aquello con lo que interactúa;
- **meta:** condición que intenta alcanzar o mantener;
- **acciones posibles:** intervenciones disponibles;
- **restricciones:** tiempo, energía, regulación, seguridad, datos y capacidad de cómputo;
- **criterio de desempeño:** cómo se juzga el resultado.

La racionalidad de un sistema es **limitada**: rara vez dispone de información total, tiempo infinito o capacidad para examinar todas las alternativas. Por ello, un sistema útil no siempre elige la acción perfecta; busca una acción suficientemente buena y segura con los recursos disponibles.

### 2.2 Percepción no equivale a registro

Un sensor produce datos; la percepción les asigna estructura y relevancia. Un reporte de visibilidad, una imagen de plataforma y un mensaje de mantenimiento tienen formatos distintos, incertidumbres diferentes y escalas temporales propias. Percibir exige:

- detectar señales y eventos;
- separar señal de ruido;
- integrar fuentes heterogéneas;
- estimar la confiabilidad de cada fuente;
- situar la observación en tiempo y contexto.

**Idea clave:** el sistema no accede directamente al mundo; accede a observaciones del mundo. Esta separación será central en el modelo POMDP.

### 2.3 Representación del conocimiento

Una representación es una estructura interna que sustituye ciertos aspectos del mundo para poder operar con ellos. Ninguna representación contiene todo: es una **abstracción con propósito**.

| Forma | Expresa bien | Limitación típica | Puente al módulo |
|---|---|---|---|
| reglas `si–entonces` | políticas, procedimientos, explicación local | fragilidad ante excepciones | 1.2 y 1.3 |
| lógica y símbolos | hechos, relaciones y deducciones | incertidumbre y costo de modelado | 1.2 |
| probabilidades | incertidumbre aleatoria y evidencia | requiere supuestos y estimaciones | 1.2 y 1.5 |
| conjuntos difusos | grados de pertenencia: “visibilidad baja” | funciones de pertenencia subjetivas | 1.3 |
| vectores o embeddings | similitud y patrones en datos complejos | menor interpretabilidad explícita | módulos 4 y 5 |
| ontologías y grafos | conceptos, relaciones, procedencia e integración | gobernanza y mantenimiento | 1.4 |

Representar conocimiento no es sólo almacenar datos. Implica decidir **qué entidades existen**, **qué relaciones importan**, **qué inferencias se permiten**, **qué incertidumbre se conserva** y **qué procedencia respalda cada afirmación**.

### 2.4 Memoria: no existe una sola memoria

Una arquitectura cognitiva suele distinguir:

- **memoria de trabajo:** estado activo y limitado de la tarea actual;
- **memoria semántica:** hechos y conceptos generales;
- **memoria episódica:** experiencias situadas en tiempo y contexto;
- **memoria procedimental:** habilidades, reglas o políticas para actuar.

Ejemplo aeroportuario: “la pista 05 existe” es conocimiento semántico; “ayer se detectó un objeto extraño a las 07:42” es episódico; “ante una alerta se ejecuta el protocolo de inspección” es procedimental; los vuelos y alertas activos ocupan la memoria de trabajo.

### 2.5 Inferencia, incertidumbre y explicación

Inferir es derivar una conclusión a partir de evidencia y conocimiento. Puede ser:

- **deductiva:** si las premisas son verdaderas y la regla es válida, la conclusión se sigue necesariamente;
- **inductiva:** generaliza patrones a partir de ejemplos;
- **abductiva:** propone la mejor explicación disponible para una observación;
- **probabilística:** actualiza grados de creencia con nueva evidencia;
- **difusa:** opera con categorías graduales en lugar de fronteras rígidas.

Es indispensable diferenciar dos incertidumbres:

- **aleatoria:** variabilidad inherente, por ejemplo el tiempo de llegada de un evento;
- **epistémica:** falta de conocimiento, por ejemplo un sensor sin cobertura o una fuente no validada.

Un sistema responsable debe comunicar no sólo una respuesta, sino su **confianza**, evidencia, supuestos y límites. La fluidez verbal no garantiza conocimiento correcto.

### 2.6 Aprendizaje y adaptación

Aprender significa modificar representaciones, parámetros, reglas o estrategias a partir de experiencia. Algunas vías son:

- aprendizaje supervisado: ejemplos con respuesta esperada;
- no supervisado: estructura sin etiquetas;
- por refuerzo: consecuencias de las acciones;
- en línea: actualización durante la operación;
- transferencia: reutilización de conocimiento entre tareas;
- aprendizaje humano-en-el-ciclo: retroalimentación y corrección experta.

Debe distinguirse **aprender correlaciones** de **comprender causas**. Un sistema puede predecir una demora sin identificar qué intervención la reduce.

### 2.7 Acción, retroalimentación y agencia

Un sistema cognitivo no termina al producir una predicción. Debe relacionar el resultado con una acción: recomendar, preguntar, planear, asignar recursos o activar un procedimiento. La agencia aumenta el impacto y también el riesgo.

Una práctica prudente es graduar la autonomía:

1. informar;
2. advertir;
3. recomendar alternativas;
4. ejecutar con autorización;
5. ejecutar y permitir veto;
6. ejecutar autónomamente dentro de límites verificados.

En dominios críticos, la supervisión humana no debe ser decorativa: la persona necesita tiempo, información y autoridad real para intervenir.

### 2.8 Enfoques principales

#### A. Simbólico

Modela conceptos y reglas explícitas. Facilita trazabilidad, composición y explicación. Puede ser costoso de mantener y frágil ante datos ruidosos o situaciones no previstas. La hipótesis del sistema físico de símbolos influyó profundamente en esta tradición ([Newell y Simon, 1976](https://doi.org/10.1145/360018.360022)).

#### B. Conexionista

Aprende representaciones distribuidas mediante redes de unidades y pesos. Es potente para percepción, lenguaje y reconocimiento de patrones, pero sus representaciones suelen ser menos transparentes y pueden heredar sesgos de datos.

#### C. Probabilístico

Representa creencias y relaciones inciertas. Permite actualizar evidencia y cuantificar riesgo, aunque depende de modelos, priors y probabilidades que deben validarse.

#### D. Corporizado o situado

Sostiene que parte de la cognición emerge de la interacción del agente —incluido su cuerpo o medio de acción— con el entorno, y no sólo de manipular representaciones internas. Esta perspectiva resulta relevante en robótica y sistemas humano-máquina ([Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/embodied-cognition/)).

#### E. Híbrido

Combina aprendizaje estadístico con conocimiento simbólico, restricciones y planeación. Por ejemplo: visión artificial detecta una anomalía; una ontología identifica el activo; reglas validan el procedimiento; un optimizador propone la secuencia; una persona autoriza. La dificultad se desplaza hacia la integración y evaluación extremo a extremo.

### 2.9 Cognición humana, artificial y distribuida

En una organización, el conocimiento no reside en una sola mente ni en una sola base de datos. Se distribuye entre operadores, manuales, sistemas, instrumentos, turnos y rutinas. Por ello, la unidad de diseño relevante puede ser el conjunto **persona–tecnología–procedimiento–entorno**.

En aviación, los fallos pueden emerger de interacciones inesperadas entre tarea, ambiente, automatización y operadores. NASA emplea ingeniería cognitiva y métodos formales para analizar sistemas humano-automatización de alta criticidad ([NASA Aerospace Cognitive Engineering Laboratory](https://www.nasa.gov/human-systems-integration-division/integration-and-evaluation/aerospace-cognitive-engineering/)).

### 2.10 Evaluación: ¿cómo sabemos que funciona?

No basta medir exactitud promedio. Deben evaluarse:

- desempeño de la tarea: precisión, costo, tiempo y cumplimiento de meta;
- calibración: si “80 % de confianza” corresponde aproximadamente a 80 % de aciertos;
- robustez: respuesta ante ruido, cambio de distribución y casos extremos;
- generalización: desempeño fuera de ejemplos conocidos;
- explicabilidad y trazabilidad: posibilidad de reconstruir evidencia y decisión;
- seguridad: severidad y probabilidad de daño;
- carga cognitiva y confianza apropiada del usuario;
- equidad, privacidad, responsabilidad y posibilidad de apelación;
- desempeño del sistema sociotécnico completo, no sólo del modelo.

---

## 3. Cinco preguntas de investigación

Las respuestas siguientes son deliberadamente **parciales**: presentan lo que hoy puede sostenerse y dejan visible lo que debe investigarse.

### Pregunta 1. ¿Qué convierte una conducta inteligente en cognición y no sólo en automatización?

**Respuesta parcial.** No existe una frontera universalmente aceptada. Un termostato percibe, compara y actúa, pero su repertorio y representación son mínimos. Un sistema se vuelve más claramente cognitivo cuando integra múltiples funciones, mantiene estado y metas, transfiere conocimiento, aprende de resultados y adapta su conducta a situaciones novedosas. Aun así, estas propiedades describen capacidad funcional, no conciencia.

**Investigación involucrada:** definir niveles de capacidad; comparar tareas conocidas y nuevas; medir transferencia, adaptación y autonomía; evitar que una demostración estrecha se generalice indebidamente.

### Pregunta 2. ¿Puede un sistema comprender o sólo correlacionar símbolos y datos?

**Respuesta parcial.** Los sistemas simbólicos conectan expresiones mediante reglas explícitas; los conexionistas aprenden regularidades estadísticas; ambos pueden producir conducta competente sin resolver por sí solos el problema filosófico del significado. En ingeniería, una prueba pragmática consiste en verificar si la representación se mantiene consistente al cambiar el contexto, si fundamenta sus conceptos en observaciones o acciones y si permite intervenir correctamente.

**Investigación involucrada:** grounding de símbolos, causalidad, razonamiento contrafactual, cognición corporizada, evaluación fuera de distribución y combinación neuro-simbólica.

### Pregunta 3. ¿Cómo decide un agente cuando no puede observar por completo el estado real?

**Respuesta parcial.** Mantiene una **creencia**: una distribución o estimación sobre estados posibles. Cada nueva observación actualiza esa creencia; después compara acciones por sus efectos, costos, riesgos y por la información que pueden revelar. El POMDP de la sección 6 formaliza esta idea. En escenarios críticos, la decisión debe incorporar aversión al riesgo y restricciones duras, no sólo utilidad esperada.

**Investigación involucrada:** fusión de sensores, inferencia bayesiana, calidad de datos, valor de la información, POMDP, lógica difusa y decisiones robustas.

### Pregunta 4. ¿Cuándo debe actuar el sistema y cuándo debe escalar la decisión a una persona?

**Respuesta parcial.** La respuesta depende de incertidumbre, reversibilidad, severidad del daño, tiempo disponible y competencia relativa humano-máquina. Una política razonable automatiza acciones frecuentes y reversibles, y eleva casos ambiguos o de alto impacto. Sin embargo, delegar sólo los casos excepcionales puede dejar a la persona sin práctica ni contexto justo cuando más se necesita.

**Investigación involucrada:** niveles de autonomía, factores humanos, calibración de confianza, explicaciones accionables, prevención del sesgo de automatización y diseño de autoridad compartida.

### Pregunta 5. ¿Cómo sabemos si el sistema aprendió una causa útil o un atajo estadístico?

**Respuesta parcial.** Una alta precisión histórica no es evidencia suficiente. Se requieren pruebas bajo cambios controlados, análisis contrafactual, conocimiento de dominio, validación temporal, detección de variables espurias y, cuando sea posible, experimentos o diseños cuasi-experimentales. El criterio decisivo es si la intervención basada en el modelo produce el efecto esperado sin daño colateral.

**Investigación involucrada:** inferencia causal, robustez, explicabilidad, auditoría de datos, monitoreo posterior al despliegue y aprendizaje continuo gobernado.

---

## 4. Tres casos de estudio

### Caso 1. IBM Watson en *Jeopardy!*: hipótesis, evidencia y confianza

**Problema.** Responder en segundos preguntas formuladas indirectamente, con juegos de palabras, dominio abierto y penalización por respuestas incorrectas.

**Arquitectura cognitiva observada.** DeepQA analizaba la pregunta, generaba múltiples hipótesis, recuperaba evidencia mediante métodos diversos, asignaba puntuaciones de confianza y decidía si convenía responder. La arquitectura integró muchas técnicas en vez de depender de un único algoritmo ([Ferrucci et al., 2010/2011](https://research.ibm.com/publications/building-watson-an-overview-of-the-deepqa-project)).

**Resultado.** En febrero de 2011 Watson venció a dos campeones destacados del programa. El reto mostró que la estimación de confianza y la estrategia de decisión importaban tanto como encontrar una respuesta. El equipo utilizó simulación y métodos de Monte Carlo para optimizar decisiones como apostar o activar el pulsador ([Tesauro et al., 2013](https://research.ibm.com/publications/analysis-of-watsons-strategies-for-playing-jeopardy)).

**Qué enseña.**

- comprender una entrada requiere descomponerla;
- conviene producir y contrastar hipótesis, no una sola respuesta inmediata;
- la confianza debe vincularse con la decisión y su costo;
- éxito en un entorno cerrado no implica transferencia automática a otros dominios.

**Pregunta para discusión.** ¿Qué tendría que cambiar para trasladar la arquitectura a documentación técnica en español, donde una respuesta incorrecta puede afectar una operación?

### Caso 2. AlphaGo: aprender una política y planear

**Problema.** El juego de Go tiene un espacio de búsqueda enorme y una función de evaluación difícil de programar mediante reglas manuales.

**Arquitectura cognitiva observada.** AlphaGo combinó una red de política para proponer movimientos, una red de valor para estimar posiciones y búsqueda Monte Carlo para anticipar consecuencias. Aprendió de partidas humanas y de autojuego. La versión publicada en 2016 derrotó 5–0 al campeón europeo Fan Hui y reportó 99.8 % de victorias frente a otros programas de Go ([Silver et al., 2016](https://www.nature.com/articles/nature16961)). AlphaGo Zero mostró después aprendizaje por refuerzo desde las reglas y autojuego, sin partidas humanas ([Silver et al., 2017](https://www.nature.com/articles/nature24270)).

**Qué enseña.**

- percepción de estado, evaluación, política y planeación pueden aprenderse y combinarse;
- el autojuego crea experiencia cuando existe un simulador confiable;
- una función objetivo clara acelera el aprendizaje;
- un juego tiene reglas, observación y recompensas mucho más definidas que un proceso organizacional real.

**Pregunta para discusión.** ¿Qué equivale a “ganar” en una operación aeroportuaria cuando seguridad, puntualidad, costo y sostenibilidad pueden entrar en tensión?

### Caso 3. Asistencia cognitiva para configuración de pista: sistema sociotécnico

**Problema.** Elegir una configuración de pistas exige integrar viento, demanda, restricciones, ruido, disponibilidad de infraestructura y coordinación humana. No basta con predecir: hay que recomendar de forma comprensible y segura.

**Diseño conceptual.**

1. sensores y sistemas operacionales aportan observaciones;
2. un modelo estima el estado y pronostica demanda o condiciones;
3. una ontología alinea activos, eventos y restricciones;
4. reglas duras eliminan opciones inseguras o no autorizadas;
5. un optimizador compara configuraciones factibles;
6. la interfaz presenta recomendación, evidencia, incertidumbre y alternativas;
7. el responsable humano decide y su resultado retroalimenta el sistema.

La NASA investiga interacción humano-automatización, métodos formales, simulación y herramientas de apoyo para sistemas aeronáuticos críticos, sus publicaciones incluyen trabajo reciente sobre aprendizaje automático y asistencia para la configuración de pistas ([NASA ACE Lab](https://www.nasa.gov/human-systems-integration-division/integration-and-evaluation/aerospace-cognitive-engineering/); [NASA Aviation Systems Division](https://www.nasa.gov/ames/aviationsystems/publications/si/)). Este caso se plantea aquí como **adaptación**, no como descripción de una instalación de ASA.

**Qué enseña.**

- la cognición puede distribuirse entre personas y tecnología;
- una recomendación debe respetar restricciones antes de optimizar preferencias;
- explicar por qué una alternativa fue descartada puede ser tan importante como la recomendación final;
- la evaluación debe medir al equipo humano–IA y no sólo la precisión del modelo.

**Pregunta para discusión.** ¿Qué datos, reglas y autorizaciones necesitaría una prueba controlada en el contexto de ASA y qué decisiones deberían permanecer fuera del alcance del prototipo?

---

## 5. Línea de tiempo: avances e hitos

| Año | Hito | Aporte a los sistemas cognitivos |
|---:|---|---|
| 1943 | McCulloch y Pitts proponen un modelo lógico de neuronas | conecta actividad neuronal simplificada y cómputo |
| 1950 | Alan Turing publica *Computing Machinery and Intelligence* | sustituye la pregunta abstracta “¿pueden pensar las máquinas?” por una prueba operacional de conducta ([archivo de Turing](https://turingarchive.kings.cam.ac.uk/publications-lectures-and-talks-amtb/amt-b-9)) |
| 1955–1956 | propuesta y taller de Dartmouth | consolida “inteligencia artificial” como programa de investigación: lenguaje, abstracción, solución de problemas y auto-mejora ([propuesta original](https://www-formal.stanford.edu/jmc/history/dartmouth.pdf)) |
| 1956 | Logic Theorist de Newell, Simon y Shaw | demuestra búsqueda heurística y manipulación simbólica para probar teoremas |
| 1957–1958 | perceptrón de Rosenblatt | establece una vía temprana de aprendizaje conexionista |
| 1959–1961 | General Problem Solver | intenta separar estrategias generales de solución del contenido específico |
| 1965 | DENDRAL | inaugura sistemas expertos que combinan conocimiento especializado e inferencia |
| 1969–1972 | Shakey | integra percepción, representación, planeación y acción en un robot móvil |
| 1976 | Newell y Simon formulan la hipótesis del sistema físico de símbolos | articula símbolos y búsqueda como base del comportamiento inteligente ([artículo ACM](https://doi.org/10.1145/360018.360022)) |
| década de 1980 | auge de sistemas expertos; desarrollo de Soar y ACT | formaliza reglas, memoria y arquitecturas integradas; también evidencia el costo de adquirir y mantener conocimiento |
| 1986 | popularización de retropropagación en redes multicapa | revitaliza el aprendizaje de representaciones distribuidas |
| 1988 | redes bayesianas y razonamiento probabilístico se consolidan | ofrecen una base sistemática para inferir bajo incertidumbre |
| 1991 | Brooks impulsa inteligencia situada y basada en conducta | cuestiona que toda inteligencia requiera un modelo simbólico central completo |
| 1997 | Deep Blue derrota a Garry Kasparov | muestra el poder de búsqueda, evaluación especializada y cómputo a gran escala |
| 1998 | Kaelbling, Littman y Cassandra sistematizan planeación en dominios parcialmente observables | relaciona creencias, valor de información y acción ([artículo](https://doi.org/10.1016/S0004-3702(98)00023-X)) |
| 2011 | Watson vence en *Jeopardy!* | integra lenguaje, generación de hipótesis, evidencia, confianza y estrategia |
| 2012 | AlexNet impulsa el aprendizaje profundo en visión | evidencia la escala de datos, cómputo y redes profundas para percepción |
| 2016–2017 | AlphaGo y AlphaGo Zero | combinan redes, búsqueda y aprendizaje por refuerzo/autojuego |
| 2017 | arquitectura Transformer | la atención permite modelar dependencias y paralelizar entrenamiento, base de posteriores modelos fundacionales ([Vaswani et al.](https://proceedings.neurips.cc/paper/7181-attention-is-all-you-need.pdf)) |
| 2020–presente | modelos fundacionales, agentes con herramientas y sistemas multimodales | amplían interacción y generalidad aparente; vuelven centrales grounding, verificación, memoria, seguridad, procedencia y gobernanza |

### Lectura crítica de la línea de tiempo

La historia no es una marcha lineal desde sistemas “primitivos” hacia uno “correcto”. Las tradiciones simbólica, probabilística, conexionista y situada resuelven problemas diferentes y hoy suelen combinarse. Muchos avances dependen tanto de datos, hardware, interfaces y organización como del algoritmo central.

---

## 6. Modelo matemático: cognición como decisión parcialmente observable

### 6.1 Por qué usar un POMDP

Un **proceso de decisión de Markov parcialmente observable** (POMDP) aproxima a un agente que debe actuar sin conocer directamente el estado real. No es una teoría completa de la mente, pero formaliza cuatro ideas cognitivas esenciales:

1. percibir no revela toda la realidad;
2. la memoria resume evidencia anterior;
3. actuar cambia el mundo y produce información;
4. decidir exige valorar consecuencias futuras.

La formulación clásica conecta investigación de operaciones e IA para planear en dominios estocásticos parcialmente observables ([Kaelbling, Littman y Cassandra, 1998](https://doi.org/10.1016/S0004-3702(98)00023-X)).

### 6.2 Componentes

Un POMDP se representa mediante la tupla:

$$
\mathcal{M}=\langle S,A,T,R,\Omega,O,\gamma \rangle
$$

donde:

- $S$: conjunto de **estados reales** posibles;
- $A$: conjunto de **acciones** disponibles;
- $T(s'\mid s,a)$: probabilidad de pasar de $s$ a $s'$ al ejecutar $a$;
- $R(s,a)$: recompensa —o utilidad— de actuar $a$ en el estado $s$;
- $\Omega$: conjunto de **observaciones** posibles;
- $O(o\mid s',a)$: probabilidad de observar $o$ después de llegar a $s'$ mediante $a$;
- $\gamma\in[0,1)$: descuento que pondera consecuencias futuras.

Correspondencia cognitiva:

| POMDP | Interpretación cognitiva |
|---|---|
| estado $s$ | situación del mundo, aunque no sea directamente visible |
| observación $o$ | percepción obtenida por sensores, reportes o interacción |
| creencia $b(s)$ | memoria de trabajo probabilística acerca de lo que podría ocurrir |
| transición $T$ | modelo de cómo cambia el entorno |
| recompensa $R$ | metas, costos y preferencias |
| política $\pi$ | estrategia para elegir acciones |
| actualización de $b$ | inferencia y aprendizaje a partir de evidencia |

### 6.3 Estado de creencia

Como el agente no observa $s_t$, mantiene una distribución:

$$
b_t(s)=P(s_t=s\mid o_{1:t},a_{1:t-1})
$$

Es decir, $b_t(s)$ expresa qué tan plausible es cada estado después de considerar observaciones y acciones anteriores. La creencia funciona como un resumen de memoria relevante para decidir.

### 6.4 Predicción y actualización bayesiana

Después de ejecutar $a_t$ y recibir $o_{t+1}$, el agente actualiza:

$$
b_{t+1}(s')=\eta\,O(o_{t+1}\mid s',a_t)
\sum_{s\in S}T(s'\mid s,a_t)b_t(s)
$$

donde $\eta$ normaliza las probabilidades para que sumen uno.

La ecuación tiene dos pasos:

1. **Predicción:** $\sum_s T(s'\mid s,a_t)b_t(s)$ estima el nuevo estado antes de mirar la evidencia.
2. **Corrección:** $O(o_{t+1}\mid s',a_t)$ pondera esa predicción según cuán compatible sea con la observación.

### 6.5 Valor y política

La política $\pi(b)$ elige una acción a partir de la creencia. Su valor esperado puede expresarse como:

$$
V^{\pi}(b)=\mathbb{E}_{\pi}\left[
\sum_{t=0}^{\infty}\gamma^t R(s_t,a_t)\mid b_0=b
\right]
$$

La política óptima busca:

$$
\pi^*=\arg\max_{\pi} V^{\pi}(b)
$$

Para problemas de seguridad, maximizar el promedio puede no ser suficiente. Pueden añadirse restricciones como:

$$
P(\text{evento inseguro}\mid b,a)\leq \varepsilon
$$

o penalizaciones que reflejen la severidad del daño. La elección de $R$ es normativa: revela qué valora la organización. Una función mal diseñada puede optimizar puntualidad sacrificando seguridad o calidad.

### 6.6 Ejemplo: inspeccionar o liberar una pista

> **Nota:** este ejemplo no representa un procedimiento operacional ni sustituye normativa, criterio experto o certificación.

Supongamos dos estados:

$$S=\{L,C\}$$

- $L$: pista libre;
- $C$: posible contaminación u objeto extraño.

Acciones:

$$A=\{\text{liberar},\text{inspeccionar}\}$$

Observación de un sensor:

$$\Omega=\{\text{alerta},\text{sin alerta}\}$$

Creencia previa:

$$P(C)=0.02,\qquad P(L)=0.98$$

Características del sensor:

$$P(\text{alerta}\mid C)=0.90$$

$$P(\text{alerta}\mid L)=0.05$$

Si se recibe una alerta, Bayes actualiza:

$$
P(C\mid \text{alerta})=
\frac{P(\text{alerta}\mid C)P(C)}
{P(\text{alerta}\mid C)P(C)+P(\text{alerta}\mid L)P(L)}
$$

$$
=\frac{0.90(0.02)}{0.90(0.02)+0.05(0.98)}
=\frac{0.018}{0.067}\approx0.269
$$

La alerta eleva la creencia de contaminación de **2 % a 26.9 %**, pero no demuestra con certeza que exista. El sistema debe ahora comparar acciones.

Definamos utilidades:

| Acción y estado | Utilidad |
|---|---:|
| liberar si está libre | $+10$ |
| liberar si está contaminada | $-1000$ |
| inspeccionar, cualquiera que sea el estado | $-8$ |

Utilidad esperada de liberar tras la alerta:

$$
EU(\text{liberar})=P(L\mid \text{alerta})(10)+P(C\mid \text{alerta})(-1000)
$$

$$
=(1-0.269)(10)+0.269(-1000)\approx -261.7
$$

Utilidad esperada de inspeccionar:

$$
EU(\text{inspeccionar})=-8
$$

Bajo estos supuestos, inspeccionar domina. El interés del ejemplo no es el número final, sino observar cómo:

- la percepción modifica una creencia, no una verdad absoluta;
- la misma probabilidad puede conducir a otra decisión si cambian costos y restricciones;
- una acción de inspección tiene **valor de información**: cuesta tiempo, pero reduce incertidumbre;
- la trazabilidad permite explicar qué datos y supuestos produjeron la recomendación.

### 6.7 Umbral de decisión

Sea $p=P(C\mid o)$. Conviene liberar cuando:

$$
(1-p)(10)+p(-1000)>-8
$$

$$
10-1010p>-8
$$

$$
p<\frac{18}{1010}\approx0.0178
$$

Con estas utilidades, sólo se liberaría si la probabilidad estimada de contaminación fuera menor a **1.78 %**. Esto muestra que el umbral no lo determina únicamente el modelo predictivo: depende de consecuencias, regulación y tolerancia al riesgo.

### 6.8 Qué simplifica el modelo

El ejemplo supone sólo dos estados, probabilidades conocidas, utilidades comparables y decisiones centralizadas. En la realidad:

- hay muchos estados y fuentes con dependencias;
- las condiciones cambian con el tiempo;
- algunos riesgos no deben compensarse con beneficios;
- existen reglas, roles y autorizaciones;
- las personas interpretan, coordinan y corrigen;
- los modelos de transición y observación también son inciertos.

Por ello, el POMDP es un **mapa conceptual y matemático**, no una réplica exhaustiva del sistema real.

### 6.9 Puentes a los siguientes temas

- **1.2 Arquitecturas de representación:** $b$, $T$, reglas y memorias requieren estructuras computacionales concretas.
- **1.3 Lógica difusa:** “riesgo alto” o “visibilidad baja” pueden representarse por grados de pertenencia; esto no es lo mismo que probabilidad. La probabilidad expresa incertidumbre sobre un hecho; la pertenencia difusa expresa gradualidad de un concepto.
- **1.4 Ontologías y grafos:** estados, sensores, pistas, eventos, responsables y evidencia pueden compartir una semántica explícita y trazable.
- **1.5 Optimización de procesos:** la política busca acciones de alto valor bajo restricciones, pero debe integrarse con seguridad y gobernanza.

---

## 7. Síntesis para estudio

1. Un sistema cognitivo integra capacidades en un ciclo, no sólo ejecuta un modelo.
2. Toda percepción es parcial y toda representación selecciona aspectos del mundo.
3. La memoria y las metas convierten observaciones aisladas en conducta coherente.
4. Razonar puede significar deducir, inducir, explicar o actualizar creencias.
5. Aprender patrones no equivale automáticamente a comprender causas.
6. La acción y la retroalimentación distinguen a un agente de un analizador pasivo.
7. Los enfoques simbólico, conexionista, probabilístico y situado son complementarios en sistemas híbridos.
8. En contextos críticos, la unidad relevante es el sistema sociotécnico humano–IA.
9. Desempeño, calibración, robustez, seguridad y trazabilidad deben evaluarse juntos.
10. Un POMDP formaliza percepción parcial, creencias, acciones y consecuencias, y abre el camino hacia optimización bajo incertidumbre.

## 8. Actividades

### Actividad breve A — ¿Es cognitivo?

Clasificar un termostato, un chatbot, un recomendador, un piloto automático y un centro de operaciones. Para cada uno, identificar percepción, memoria, metas, aprendizaje, acción y retroalimentación. Justificar dónde se traza la frontera.

### Actividad breve B — Cambiar la representación

Representar el mismo evento —“una pista tiene baja disponibilidad”— como:

1. regla lógica;
2. probabilidad;
3. variable difusa;
4. subgrafo de conocimiento.

Discutir qué inferencias facilita y qué información pierde cada forma.

### Actividad breve C — Sensibilidad del modelo

Recalcular el ejemplo si la tasa de falsos positivos cambia de 5 % a 15 %, o si el costo de inspección cambia de $-8$ a $-30$. Explicar por qué una política puede cambiar aun cuando el evento físico sea el mismo.

## 9. Preguntas de comprobación

1. ¿Por qué un clasificador aislado no constituye necesariamente un sistema cognitivo?
2. ¿Cuál es la diferencia entre estado real, observación y creencia?
3. ¿Qué tipos de memoria se distinguen y para qué sirven?
4. ¿En qué difieren incertidumbre probabilística y vaguedad difusa?
5. ¿Por qué una arquitectura híbrida puede ser preferible en un dominio crítico?
6. ¿Qué riesgo surge cuando una persona supervisa automatización sin contexto ni tiempo para intervenir?
7. ¿Qué representa la función de recompensa y por qué debe gobernarse?
8. ¿Qué aporta una ontología al ciclo cognitivo?

---

## Referencias y lecturas recomendadas

- ACT-R Research Group. *ACT-R: A cognitive architecture*. Carnegie Mellon University. <https://act-r.psy.cmu.edu/>
- Ferrucci, D. et al. (2010/2011). “Building Watson: An Overview of the DeepQA Project”. *AI Magazine*. <https://research.ibm.com/publications/building-watson-an-overview-of-the-deepqa-project>
- Kaelbling, L. P., Littman, M. L. y Cassandra, A. R. (1998). “Planning and Acting in Partially Observable Stochastic Domains”. *Artificial Intelligence*, 101(1–2), 99–134. <https://doi.org/10.1016/S0004-3702(98)00023-X>
- McCarthy, J., Minsky, M., Rochester, N. y Shannon, C. (1955). *A Proposal for the Dartmouth Summer Research Project on Artificial Intelligence*. <https://www-formal.stanford.edu/jmc/history/dartmouth.pdf>
- NASA. *Aerospace Cognitive Engineering Laboratory*. <https://www.nasa.gov/human-systems-integration-division/integration-and-evaluation/aerospace-cognitive-engineering/>
- Newell, A. y Simon, H. A. (1976). “Computer Science as Empirical Inquiry: Symbols and Search”. *Communications of the ACM*, 19(3), 113–126. <https://doi.org/10.1145/360018.360022>
- Silver, D. et al. (2016). “Mastering the Game of Go with Deep Neural Networks and Tree Search”. *Nature*, 529, 484–489. <https://www.nature.com/articles/nature16961>
- Silver, D. et al. (2017). “Mastering the Game of Go without Human Knowledge”. *Nature*, 550, 354–359. <https://www.nature.com/articles/nature24270>
- Soar Group. *The Soar Architecture*. University of Michigan. <https://soar.eecs.umich.edu/soar_manual/02_TheSoarArchitecture/>
- Tesauro, G. et al. (2013). “Analysis of Watson's Strategies for Playing Jeopardy!”. *Journal of Artificial Intelligence Research*. <https://research.ibm.com/publications/analysis-of-watsons-strategies-for-playing-jeopardy>
- Turing, A. M. (1950). “Computing Machinery and Intelligence”. *Mind*, 59(236), 433–460. Registro en el Turing Digital Archive: <https://turingarchive.kings.cam.ac.uk/publications-lectures-and-talks-amtb/amt-b-9>
- Vaswani, A. et al. (2017). “Attention Is All You Need”. *Advances in Neural Information Processing Systems 30*. <https://proceedings.neurips.cc/paper/7181-attention-is-all-you-need.pdf>
- Wilson, R. A. y Foglia, L. (2021). “Embodied Cognition”. *Stanford Encyclopedia of Philosophy*. <https://plato.stanford.edu/entries/embodied-cognition/>

### Nota de uso académico

Estas notas ofrecen un marco introductorio y ejemplos simplificados. Los casos operacionales deben contrastarse con normativa vigente, procedimientos institucionales, especialistas de dominio y evidencia local antes de diseñar o desplegar cualquier sistema.
