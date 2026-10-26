# Módulo 1.1 — Glosario de fundamentos de sistemas cognitivos

> **Diplomado en Inteligencia Artificial**  
> **Módulo 1:** Sistemas cognitivos y representación del conocimiento  
> **Tema:** Fundamentos de sistemas cognitivos

## Cómo utilizar este glosario

Los conceptos se presentan en orden alfabético. Cada entrada contiene:

- una explicación breve;
- su relación con otros términos del módulo;
- una referencia o tema para continuar el aprendizaje.

Las referencias priorizan documentación institucional, artículos académicos y textos fundacionales. Los ejemplos aeroportuarios son didácticos y no representan procedimientos operacionales.

---

## ACT-R

**ACT-R** significa *Adaptive Control of Thought—Rational*, que puede traducirse como **Control Adaptativo del Pensamiento—Racional**. Es una arquitectura cognitiva desarrollada principalmente para formular y comprobar teorías sobre la cognición humana mediante modelos computacionales.

ACT-R divide la cognición en módulos especializados —por ejemplo, percepción visual, acción motora y memoria declarativa— que intercambian pequeñas cantidades de información a través de **buffers**. Un sistema central de reglas de producción coordina lo que se hace con esa información.

- **Control adaptativo:** la conducta no permanece fija. La experiencia modifica la disponibilidad de recuerdos, la utilidad de las reglas y la rapidez o probabilidad con que se seleccionan. La arquitectura intenta explicar cómo una persona pasa de seguir pasos deliberados a ejecutar una habilidad con mayor fluidez.
- **Pensamiento racional:** “racional” no significa que el agente sea perfecto. ACT-R supone que ciertos mecanismos cognitivos se ajustan al entorno y emplean los recursos limitados de manera aproximadamente útil. El tiempo de recuperación, la frecuencia de uso y el costo de una acción influyen en la conducta.
- **Importancia:** permite construir modelos que producen no sólo respuestas, sino también predicciones sobre tiempos de reacción, errores, aprendizaje y carga cognitiva.

**Relacionado con:** arquitectura cognitiva, memoria declarativa, memoria procedimental, regla de producción, racionalidad limitada.

**Para aprender más:** [sitio oficial de ACT-R, Carnegie Mellon University](https://act-r.psy.cmu.edu/) y el tema **modelado computacional de la cognición humana**.

---

## Agente

Entidad que percibe un entorno y selecciona acciones para alcanzar o mantener metas. Puede ser una persona, un robot, un programa o un sistema sociotécnico. Llamarlo “agente” obliga a especificar qué puede observar, recordar y hacer, en vez de atribuirle inteligencia de forma vaga.

**Relacionado con:** entorno, política, autonomía, ciclo percepción–acción.

**Para aprender más:** tema **agentes racionales** en inteligencia artificial y [Artificial Intelligence: A Modern Approach — recursos](https://aima.cs.berkeley.edu/).

---

## Arquitectura cognitiva

Marco que define los componentes relativamente estables de un sistema cognitivo —memorias, representaciones, mecanismos de aprendizaje y decisión— y la manera en que interactúan. Una arquitectura no es una aplicación terminada: necesita conocimiento, objetivos, sensores y acciones propios de un dominio.

Soar y ACT-R son arquitecturas cognitivas. Ambas integran varias capacidades, aunque Soar se ha orientado ampliamente hacia agentes inteligentes generales y ACT-R hacia modelos verificables de la cognición humana.

**Relacionado con:** ACT-R, Soar, sistema cognitivo, arquitectura híbrida.

**Para aprender más:** tema **modelo estándar de la mente** y [A Standard Model of the Mind, Laird, Lebiere y Rosenbloom](https://ojs.aaai.org/index.php/aimagazine/article/view/2744).

---

## Arquitectura híbrida o sistema neuro-simbólico

Sistema que combina componentes aprendidos a partir de datos —como redes neuronales— con conocimiento explícito —como reglas, restricciones, ontologías o grafos—. La combinación busca aprovechar el reconocimiento de patrones de los modelos estadísticos y la trazabilidad de los métodos simbólicos.

Ejemplo: un modelo visual detecta un objeto; un grafo identifica el activo y su ubicación; reglas verifican restricciones; un optimizador propone una acción.

**Relacionado con:** conexionismo, representación simbólica, ontología, razonamiento.

**Para aprender más:** tema **integración neuro-simbólica** y [Neuro-Symbolic Artificial Intelligence: The State of the Art](https://ebooks.iospress.nl/volume/neuro-symbolic-artificial-intelligence-the-state-of-the-art).

---

## Cadena de Markov

Modelo matemático de una secuencia de estados aleatorios en la que la distribución del siguiente estado depende del estado actual y no de toda la historia, una vez conocido el presente:

$$
P(X_{t+1}=x'\mid X_t=x,X_{t-1},\ldots,X_0)
=P(X_{t+1}=x'\mid X_t=x)
$$

Esta es la **propiedad de Markov**. No afirma que el pasado sea irrelevante en sentido absoluto, sino que el estado actual contiene el resumen del pasado necesario para predecir el siguiente paso dentro del modelo.

Una cadena de Markov normalmente representa transiciones entre estados **sin decisiones del agente**. Por ejemplo, modelar el cambio entre niveles discretos de demanda: baja, media y alta.

**Relacionado con:** propiedad de Markov, proceso de Markov, matriz de transición, MDP.

**Para aprender más:** tema **matrices de transición y distribuciones estacionarias** y [Markov chain, Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Markov_chain).

---

## Calibración de confianza

Correspondencia entre la confianza declarada por un sistema y su frecuencia real de aciertos. Si, entre cien predicciones emitidas con 80 % de confianza, aproximadamente ochenta son correctas, el sistema está bien calibrado en ese intervalo.

Un modelo puede tener buena exactitud y mala calibración. En decisiones de riesgo, saber cuándo el sistema duda puede ser tan importante como su respuesta más probable.

**Relacionado con:** incertidumbre, probabilidad, supervisión humana, evaluación.

**Para aprender más:** tema **diagramas de confiabilidad y error esperado de calibración** y [On Calibration of Modern Neural Networks](https://proceedings.mlr.press/v70/guo17a.html).

---

## Cognición corporizada o situada

Familia de enfoques que sostiene que la cognición depende de la interacción del agente con su cuerpo, sus posibilidades de acción y su entorno. Cuestiona que pensar consista únicamente en manipular símbolos dentro de un sistema aislado.

En robótica, la forma del cuerpo y los sensores determina qué se puede aprender y hacer. En un sistema organizacional, las interfaces, herramientas y procedimientos también forman parte del contexto que hace posible la decisión.

**Relacionado con:** agente, entorno, grounding, cognición distribuida.

**Para aprender más:** [Embodied Cognition, Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/embodied-cognition/).

---

## Cognición distribuida

Perspectiva según la cual un proceso cognitivo puede estar distribuido entre varias personas, artefactos, representaciones y momentos. Una lista de verificación, una pantalla, un procedimiento y la comunicación entre turnos pueden conservar y transformar conocimiento junto con los operadores.

Esta idea es especialmente importante en aviación: evaluar únicamente el algoritmo ignora cómo la información fluye por el sistema humano–tecnología–organización.

**Relacionado con:** sistema sociotécnico, factores humanos, memoria externa, conciencia situacional.

**Para aprender más:** tema **cognición distribuida en cabinas de vuelo** y Hutchins, *Cognition in the Wild* ([MIT Press](https://mitpress.mit.edu/9780262581462/cognition-in-the-wild/)).

---

## Creencia o estado de creencia

Distribución de probabilidad que resume lo que un agente considera posible acerca del estado no observable del mundo:

$$
b_t(s)=P(s_t=s\mid o_{1:t},a_{1:t-1})
$$

No es una afirmación psicológica sobre “creer”, sino una representación matemática de incertidumbre. En un POMDP, la creencia cumple la función de un estado informacional sobre el cual se puede decidir.

**Relacionado con:** POMDP, inferencia bayesiana, observación, incertidumbre epistémica.

**Para aprender más:** tema **filtro bayesiano** en [Planning and Acting in Partially Observable Stochastic Domains](https://doi.org/10.1016/S0004-3702(98)00023-X).

---

## Función de recompensa o utilidad

Expresión numérica de las consecuencias que el sistema debe preferir o evitar. En aprendizaje por refuerzo y procesos de decisión, guía la elección de acciones.

La recompensa no es un hecho neutral: traduce metas organizacionales a números. Si sólo premia rapidez, el sistema puede perjudicar seguridad o calidad. Por eso debe distinguirse entre preferencias optimizables y restricciones que nunca deben violarse.

**Relacionado con:** MDP, POMDP, política, optimización, alineación de objetivos.

**Para aprender más:** tema **diseño de recompensas y especificación de objetivos** y [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html).

---

## Grafo de conocimiento

Representación de entidades como nodos y relaciones como aristas, acompañadas frecuentemente por tipos, identificadores y procedencia. Permite conectar datos dispersos y consultar rutas como “qué equipo pertenece a qué instalación y qué evento lo afectó”.

Una ontología puede aportar el esquema semántico del grafo, pero ambos términos no son idénticos: la ontología define conceptos y restricciones; el grafo contiene instancias y relaciones concretas.

**Relacionado con:** ontología, representación del conocimiento, inferencia, procedencia.

**Para aprender más:** [Knowledge Graphs, Hogan et al.](https://doi.org/10.1145/3447772) y el tema **RDF y consultas SPARQL**.

---

## Grounding o fundamentación de símbolos

Problema de explicar cómo los símbolos internos de un sistema adquieren significado conectado con percepción, acción o uso, y no sólo mediante relaciones con otros símbolos. Una etiqueta como “pista bloqueada” debe vincularse con observaciones, criterios y consecuencias verificables.

**Relacionado con:** representación simbólica, cognición corporizada, percepción, semántica.

**Para aprender más:** Harnad, “The Symbol Grounding Problem” ([Physica D](https://doi.org/10.1016/0167-2789(90)90087-6)).

---

## Inferencia bayesiana

Método para actualizar una creencia previa al observar nueva evidencia:

$$
P(H\mid E)=\frac{P(E\mid H)P(H)}{P(E)}
$$

El **prior** $P(H)$ representa la creencia antes de observar; la verosimilitud $P(E\mid H)$ indica qué tan compatible es la evidencia con la hipótesis; el **posterior** $P(H\mid E)$ es la creencia actualizada.

**Relacionado con:** creencia, probabilidad, red bayesiana, POMDP.

**Para aprender más:** tema **teorema de Bayes, prior, verosimilitud y posterior** y [Probabilistic Models of Cognition](https://probmods.org/).

---

## Lógica difusa

Marco para representar conceptos graduales mediante grados de pertenencia entre 0 y 1. Por ejemplo, una visibilidad de cierto valor puede pertenecer parcialmente a las categorías “media” y “baja”.

El grado difuso no es automáticamente una probabilidad. La expresión “0.7 de pertenencia a visibilidad baja” describe gradualidad del concepto; “0.7 de probabilidad de que la visibilidad sea menor a un umbral” expresa incertidumbre sobre un evento.

**Relacionado con:** conjunto difuso, regla lingüística, incertidumbre, control.

**Para aprender más:** Zadeh, “Fuzzy Sets” ([Information and Control, 1965](https://doi.org/10.1016/S0019-9958(65)90241-X)).

---

## Memoria declarativa y memoria procedimental

- **Declarativa:** conserva hechos y conceptos que pueden recuperarse, como “la plataforma A tiene cinco posiciones”.
- **Procedimental:** conserva el saber hacer, normalmente como reglas, habilidades o políticas, como “si ocurre una alerta validada, iniciar la secuencia de inspección”.

En ACT-R, la memoria declarativa contiene *chunks* y el conocimiento procedimental se expresa mediante reglas de producción. En Soar también existen memorias diferenciadas, aunque sus mecanismos específicos no son idénticos.

**Relacionado con:** ACT-R, Soar, memoria semántica, regla de producción.

**Para aprender más:** tema **sistemas de memoria de largo plazo** y [ACT-R Publications](https://act-r.psy.cmu.edu/publications/).

---

## MDP — Proceso de decisión de Markov

Un **Markov Decision Process** amplía una cadena de Markov al incorporar un agente que elige acciones, recompensas y una política. Se representa comúnmente como:

$$
\langle S,A,T,R,\gamma\rangle
$$

El estado se supone completamente observable. La acción modifica las probabilidades de transición $T(s'\mid s,a)$ y produce una recompensa $R(s,a)$. El objetivo es encontrar una política que maximice el retorno esperado a largo plazo.

**Relacionado con:** cadena de Markov, política, recompensa, POMDP, aprendizaje por refuerzo.

**Para aprender más:** tema **ecuaciones de Bellman** en [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html).

---

## Observación y estado

El **estado** describe la situación relevante del entorno; la **observación** es la información que llega al agente mediante sensores, registros o mensajes. No deben confundirse: una alerta es una observación, mientras que la condición física que se intenta conocer pertenece al estado.

Si la observación revela completamente el estado, puede usarse un MDP. Si sólo aporta evidencia parcial o ruidosa, un POMDP suele ser una representación más adecuada.

**Relacionado con:** percepción, estado de creencia, MDP, POMDP.

**Para aprender más:** tema **modelos de observación y sensores** en [Kaelbling, Littman y Cassandra, 1998](https://doi.org/10.1016/S0004-3702(98)00023-X).

---

## Ontología

Especificación explícita de los conceptos de un dominio, sus relaciones y, en algunos casos, restricciones lógicas. Ayuda a que personas y sistemas utilicen términos como “activo”, “evento”, “ubicación” o “responsable” con significados compatibles.

Una ontología no es sólo una lista de palabras. Define clases, propiedades, jerarquías y axiomas que pueden permitir validación e inferencia.

**Relacionado con:** grafo de conocimiento, representación simbólica, interoperabilidad, inferencia.

**Para aprender más:** [Ontology Development 101, Stanford](https://protege.stanford.edu/publications/ontology_development/ontology101.pdf) y el tema **OWL**.

---

## Política

Regla o función que indica qué acción elegir. En un MDP puede escribirse como $\pi(a\mid s)$; en un POMDP, como $\pi(a\mid b)$ porque la decisión se basa en la creencia sobre el estado.

Una política puede ser determinista, probabilística, aprendida o definida por reglas. No debe confundirse con una política institucional, aunque esta última puede convertirse parcialmente en restricciones o reglas del modelo.

**Relacionado con:** agente, recompensa, valor, MDP, POMDP.

**Para aprender más:** tema **evaluación y mejora de políticas** en [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/the-book-2nd.html).

---

## POMDP — Proceso de decisión de Markov parcialmente observable

Un **Partially Observable Markov Decision Process** representa decisiones secuenciales cuando el agente no observa directamente el estado real. Su formulación típica es:

$$
\mathcal{M}=\langle S,A,T,R,\Omega,O,\gamma\rangle
$$

El nombre puede descomponerse así:

- **Proceso:** la situación evoluciona a lo largo del tiempo; no se trata de una clasificación aislada.
- **De decisión:** existe un agente que puede elegir acciones y afectar las consecuencias.
- **Parcialmente observable:** sensores o reportes sólo ofrecen evidencia incompleta o ruidosa sobre el estado.
- **De Markov:** si el estado estuviera disponible, contendría la información necesaria para modelar la siguiente transición; no sería necesario conservar toda la historia.

Como el estado no se observa, el agente mantiene un **estado de creencia** $b(s)$. Esta distribución se actualiza con cada acción y observación. Así, el POMDP convierte un problema parcialmente observable en un problema de decisión sobre creencias.

Relación entre modelos:

```text
proceso estocástico
└── proceso de Markov
    ├── cadena de Markov: transiciones, sin decisiones
    └── MDP: decisiones y estado observable
        └── POMDP: decisiones y estado sólo parcialmente observable
```

Un POMDP es útil cuando una acción puede tener dos valores simultáneos: cambiar el entorno y obtener información. Inspeccionar, por ejemplo, puede tener un costo inmediato pero reducir incertidumbre antes de una decisión de mayor riesgo.

**Relacionado con:** proceso de Markov, MDP, creencia, valor de la información, inferencia bayesiana.

**Para aprender más:** Kaelbling, Littman y Cassandra, “Planning and Acting in Partially Observable Stochastic Domains” ([Artificial Intelligence, 1998](https://doi.org/10.1016/S0004-3702(98)00023-X)).

---

## Proceso de Markov

Proceso estocástico que satisface la propiedad de Markov: condicionado al estado presente, el futuro es independiente del pasado. Es una categoría general que puede formularse en tiempo discreto o continuo y con espacios de estado discretos o continuos.

La expresión **cadena de Markov** suele reservarse para estados discretos, mientras que “proceso de Markov” es más amplio. Un proceso de Markov por sí solo no exige decisiones ni recompensas; éstos aparecen en un MDP.

Ejemplos conceptuales:

- cadena discreta: demanda baja → media → alta;
- proceso continuo: degradación de un componente a lo largo del tiempo;
- MDP: decidir si inspeccionar o intervenir según el estado;
- POMDP: decidir cuando dicho estado sólo se estima mediante mediciones imperfectas.

**Relacionado con:** propiedad de Markov, cadena de Markov, proceso estocástico, MDP.

**Para aprender más:** tema **procesos de Markov en tiempo continuo** y [Introduction to Probability Models, Academic Press](https://www.sciencedirect.com/book/9780128143469/introduction-to-probability-models).

---

## Propiedad de Markov

Supuesto según el cual el presente resume toda la información histórica necesaria para modelar el futuro. La propiedad depende de cómo se construye el estado. Si el “estado actual” omite la antigüedad de un componente y ésta afecta su falla, el modelo puede dejar de ser markoviano; una solución es ampliar el estado para incluirla.

**Relacionado con:** estado, cadena de Markov, proceso de Markov, suficiencia estadística.

**Para aprender más:** tema **diseño del espacio de estados** y [Markov Processes, Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Markov_process).

---

## Racionalidad limitada

Idea asociada con Herbert Simon: los agentes reales deciden con información, tiempo y capacidad de cómputo limitados. En vez de encontrar siempre el óptimo global, suelen buscar alternativas suficientemente satisfactorias.

En sistemas cognitivos, reconocer estos límites conduce a usar heurísticas, atención selectiva, memoria finita y escalamiento a personas. También obliga a medir el costo de obtener más información o calcular una solución mejor.

**Relacionado con:** heurística, ACT-R, decisión, costo computacional.

**Para aprender más:** Simon, “A Behavioral Model of Rational Choice” ([Quarterly Journal of Economics, 1955](https://doi.org/10.2307/1884852)).

---

## Red bayesiana

Grafo dirigido acíclico que representa variables aleatorias y sus dependencias condicionales. Cada nodo tiene una distribución condicionada por sus padres. La estructura permite factorizar una distribución conjunta y razonar sobre causas, síntomas y evidencia, siempre que las relaciones y probabilidades estén justificadas.

**Relacionado con:** inferencia bayesiana, grafo, incertidumbre, causalidad.

**Para aprender más:** Pearl, *Probabilistic Reasoning in Intelligent Systems* ([Morgan Kaufmann](https://www.sciencedirect.com/book/9780080514895/probabilistic-reasoning-in-intelligent-systems)).

---

## Regla de producción

Regla de la forma **si condición, entonces acción o conclusión**. En arquitecturas cognitivas, las reglas de producción pueden consultar la memoria de trabajo y proponer o ejecutar operaciones. Separan conocimiento procedimental de los datos concretos sobre los que actúa.

Ejemplo simplificado: “si existe una alerta validada y la pista está activa, entonces proponer inspección”. En un sistema real harían falta prioridades, excepciones, procedencia y control de conflictos.

**Relacionado con:** Soar, ACT-R, memoria procedimental, sistema experto.

**Para aprender más:** tema **sistemas de producción y resolución de conflictos** en [The Soar Architecture](https://soar.eecs.umich.edu/soar_manual/02_TheSoarArchitecture/).

---

## Representación del conocimiento

Forma computable de describir objetos, propiedades, relaciones, eventos y reglas para que un sistema pueda consultar o inferir. Una representación siempre selecciona ciertos aspectos del mundo; su calidad depende de la tarea, no de cuánto detalle acumule.

Las representaciones pueden ser simbólicas —lógica, reglas, ontologías—, probabilísticas, difusas o distribuidas —vectores y embeddings—.

**Relacionado con:** ontología, grafo de conocimiento, lógica difusa, embedding.

**Para aprender más:** tema **compromisos ontológicos y adecuación representacional** y [Knowledge Representation and Reasoning, Brachman y Levesque](https://www.sciencedirect.com/book/9781558609327/knowledge-representation-and-reasoning).

---

## Sistema cognitivo

Agente biológico, artificial o sociotécnico que integra percepción, representación, memoria, inferencia, aprendizaje, decisión y acción orientada a metas. No es sinónimo de conciencia ni de un modelo aislado de IA.

La propiedad clave es la integración dentro de un ciclo de retroalimentación: las acciones producen resultados, los resultados generan nueva evidencia y el sistema modifica sus creencias o estrategias.

**Relacionado con:** arquitectura cognitiva, agente, ciclo percepción–acción, sistema sociotécnico.

**Para aprender más:** tema **sistemas cognitivos integrados** y [Soar: Cognitive Architecture](https://soar.eecs.umich.edu/home/About/).

---

## Sistema sociotécnico

Conjunto formado por personas, tecnología, procesos, normas y organización. Su desempeño emerge de la interacción entre componentes; por ello, un modelo preciso puede fracasar si la interfaz confunde, la autoridad no está clara o el procedimiento contradice la recomendación.

**Relacionado con:** cognición distribuida, factores humanos, automatización, gobernanza.

**Para aprender más:** [NASA Aerospace Cognitive Engineering Laboratory](https://www.nasa.gov/human-systems-integration-division/integration-and-evaluation/aerospace-cognitive-engineering/) y el tema **interacción humano–automatización en sistemas críticos**.

---

## Soar

**Soar** es una arquitectura cognitiva general diseñada para construir agentes que exhiban conducta inteligente. Integra memoria de trabajo, memoria procedimental, memoria semántica, memoria episódica, aprendizaje y mecanismos de decisión.

Su ciclo deliberativo se entiende mediante tres conceptos centrales:

- **Estado:** representación en memoria de trabajo de la situación actual del problema. Incluye información sobre el entorno, la meta y el progreso alcanzado. No es necesariamente el estado físico completo del mundo, sino lo que el agente representa como relevante.
- **Operador:** transformación candidata que el agente puede aplicar al estado. Un operador puede representar una acción externa —mover un robot— o una operación mental —recuperar conocimiento o descomponer un problema—. Las reglas proponen operadores, expresan preferencias, seleccionan uno y lo aplican.
- **Resultado:** cambios producidos al aplicar el operador. Pueden modificar la representación interna o generar acciones en el entorno. El resultado conduce a un nuevo estado de resolución del problema.

De forma simplificada:

```text
estado actual → proponer operadores → evaluar preferencias
              → seleccionar operador → aplicarlo → resultado/nuevo estado
```

Cuando el conocimiento disponible no permite seleccionar o aplicar un operador, ocurre un **impasse**. Soar crea entonces un subestado para resolverlo. Si encuentra una solución, el mecanismo de **chunking** puede aprender una nueva regla que evite repetir el mismo razonamiento en situaciones semejantes.

**Relacionado con:** arquitectura cognitiva, regla de producción, memoria de trabajo, impasse, chunking.

**Para aprender más:** [The Soar Architecture, manual oficial](https://soar.eecs.umich.edu/soar_manual/02_TheSoarArchitecture/) y [Introduction to Soar](https://arxiv.org/abs/2205.03854).

---

## Valor de la información

Beneficio esperado de obtener información adicional antes de decidir. Una inspección, medición o consulta puede costar tiempo y recursos, pero ser valiosa si cambia la acción elegida o reduce un riesgo importante.

En un POMDP, las acciones pueden ser informativas además de producir efectos físicos. Este rasgo distingue la decisión secuencial de una clasificación pasiva.

**Relacionado con:** POMDP, creencia, exploración, decisión bajo incertidumbre.

**Para aprender más:** tema **Expected Value of Perfect Information y Expected Value of Sample Information** en [Decision Analysis, Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/decision-theory/).

---

## Mapa de relaciones esenciales

```text
Sistema cognitivo
├── se organiza mediante → arquitectura cognitiva
│   ├── Soar → estado + operador + resultado
│   └── ACT-R → módulos + buffers + reglas de producción
├── representa → estado, memoria, ontología, grafo de conocimiento
├── percibe → observaciones parciales o ruidosas
├── infiere → lógica, probabilidad, Bayes o lógica difusa
└── decide
    ├── cadena/proceso de Markov → evolución sin decisiones
    ├── MDP → decisiones con estado observable
    └── POMDP → decisiones mediante estados de creencia
```

## Lecturas de continuidad dentro del módulo

- Para **1.2 Arquitecturas de representación del conocimiento**: arquitectura cognitiva, regla de producción, representación del conocimiento y arquitectura híbrida.
- Para **1.3 Lógica difusa e inferencia**: lógica difusa, inferencia bayesiana, calibración y red bayesiana.
- Para **1.4 Ontologías y grafos de conocimiento**: ontología, grafo de conocimiento, grounding y procedencia.
- Para **1.5 Optimización de procesos**: agente, política, recompensa, MDP, POMDP y valor de la información.
