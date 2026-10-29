# Módulo 1.4 - Ontologías y grafos de conocimiento

> **Inteligencia Artificial**  
> **Módulo 1 — Sistemas cognitivos y representación del conocimiento**  
> **Tema:** Ontologías y grafos de conocimiento

## Introducción: tres maneras de utilizar una red

Una red de ciudades permite preguntar **cómo llegar**. Una red de estados permite preguntar **qué sucede cuando ocurre un evento**. Una red de conceptos permite preguntar **qué sabemos y qué podemos deducir**. Los tres modelos comparten nodos y conexiones, pero no comparten necesariamente sus reglas de interpretación.

Al finalizar se podrá: (1) representar y recorrer grafos dirigidos y no dirigidos; (2) ejecutar manualmente Dijkstra con pesos no negativos; (3) construir y ejecutar autómatas mediante tablas de transición; (4) expresar hechos mediante tripletas RDF; y (5) justificar inferencias a partir de axiomas y reglas.

**Ruta conceptual:** conjunto → grafo → recorrido → estado → transición → tripleta → ontología → deducción.

---

## I. Grafos: representar conexiones (80 min)

### 1. De conjuntos a redes

Un **conjunto** reúne elementos; un **grafo** añade relaciones entre ellos. Formalmente, $G=(V,E)$, donde $V$ es un conjunto de vértices y $E$ un conjunto de aristas.

Para un grafo no dirigido, cada arista es un par no ordenado $\{u,v\}$. Para uno dirigido, cada arco es un par ordenado $(u,v)$, de modo que $(u,v)$ no implica $(v,u)$. Una conexión no dirigida puede representarse mediante dos arcos opuestos, aunque ambas estructuras no sean idénticas formalmente.

**Ejemplo:** $V=\{A,B,C,D\}$, $E=\{(A,B),(A,C),(B,D),(C,D)\}$. Dibujar el grafo y responder: ¿desde A se alcanza D?, ¿hay más de una ruta?, ¿se puede regresar desde D hasta A?

Un **camino** es una secuencia de vértices conectados por aristas consecutivas. En un grafo dirigido debe respetar la orientación. Un **ciclo** es un camino cerrado. El **grado** cuenta incidencias; en grafos dirigidos distinguimos grado de entrada y de salida.

### 2. Pesos y recorridos

Un grafo ponderado incorpora una función $w:E\to\mathbb{R}$. Un peso puede significar distancia, costo, tiempo o capacidad; no debe asumirse que todos esos significados son intercambiables.

Dos estrategias de exploración:

- **BFS (anchura):** explora por niveles; encuentra un camino con el menor número de aristas en grafos no ponderados.
- **DFS (profundidad):** continúa por una rama antes de retroceder; es útil para exploración y alcanzabilidad.

**Actividad breve:** dibujar A→B, A→C, B→D, C→E, D→F, E→F. Escribir un recorrido BFS y uno DFS desde A. El orden puede variar según cómo se ordenen los vecinos.

### 3. Dijkstra: encontrar el camino de menor costo

**Problema:** hallar la distancia mínima desde A hasta F. Se utiliza un grafo **no dirigido**, con pesos no negativos:

| Arista | Peso | Arista | Peso | Arista | Peso |
|---|---:|---|---:|---|---:|
| A—B | 4 | A—C | 2 | B—C | 1 |
| B—D | 5 | C—D | 8 | C—E | 10 |
| D—E | 2 | D—F | 6 | E—F | 3 |

**Regla de actualización (relajación):**

$$
d(v)\leftarrow\min\{d(v),d(u)+w(u,v)\}.
$$

Se inicia con $d(A)=0$ y las demás distancias en infinito. En cada iteración se fija el nodo pendiente con menor distancia tentativa y se actualizan sus vecinos.

| Iteración | Nodo fijado | A | B | C | D | E | F |
|---|---|---:|---:|---:|---:|---:|---:|
| 0 | — | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | A | 0 | 4 | 2 | ∞ | ∞ | ∞ |
| 2 | C | 0 | 3 | 2 | 10 | 12 | ∞ |
| 3 | B | 0 | 3 | 2 | 8 | 12 | ∞ |
| 4 | D | 0 | 3 | 2 | 8 | 10 | 14 |
| 5 | E | 0 | 3 | 2 | 8 | 10 | 13 |
| 6 | F | 0 | 3 | 2 | 8 | 10 | 13 |

**Predecesores finales:** C←A; B←C; D←B; E←D; F←E. La ruta mínima es **A→C→B→D→E→F**, con costo **13**.

**Corrida manual:** reconstruir cada fila sin consultar la siguiente. Registrar por separado qué nodo se fija y cuál fue el predecesor de cada mejora. Verificar por qué seleccionar simplemente la arista más barata disponible no resuelve el problema.

**Reto:** cambiar el peso de D—E de 2 a 9 y repetir la corrida. ¿Cambia la ruta? **Comprobación:** la nueva ruta mínima es A→C→E→F, costo 15.

**Límite del método:** Dijkstra no garantiza resultados correctos con pesos negativos. La complejidad de los problemas de grafos varía; encontrar un camino mínimo no es lo mismo que visitar todas las ciudades una sola vez. No necesitamos estudiar P y NP para aplicar este algoritmo.

---

## II. Máquinas de estados: representar comportamiento (80 min)

### 4. Del nodo al estado

Un nodo ahora representa una **situación posible** del sistema. Una arista dirigida representa una **transición** habilitada por una entrada o evento. No basta con que exista una conexión: debe ocurrir la entrada correspondiente.

Un autómata finito determinista (AFD) reconocedor puede describirse por

$$
M=(Q,\Sigma,\delta,q_0,F),\qquad \delta:Q\times\Sigma\to Q.
$$

Aquí $Q$ es el conjunto de estados; $\Sigma$, el alfabeto de entradas; $\delta$, la función de transición; $q_0$, el estado inicial; y $F$, los estados de aceptación. **Determinista** significa que cada pareja (estado, símbolo) determina exactamente un siguiente estado.

### 5. Autómata de lenguaje: cadenas que terminan en 01

Estados: $q_0$ (sin sufijo útil), $q_1$ (último símbolo 0), $q_2$ (últimos símbolos 01). Estado inicial $q_0$; estado de aceptación $F=\{q_2\}$.

| Estado actual | Entrada 0 | Entrada 1 |
|---|---|---|
| q₀ | q₁ | q₀ |
| q₁ | q₁ | q₂ |
| q₂ | q₁ | q₀ |

**Corrida 1:** `10101` → q₀ → q₀ → q₁ → q₂ → q₁ → q₂: **aceptada**.

**Corrida 2:** `10110` → q₀ → q₀ → q₁ → q₂ → q₀ → q₁: **rechazada**.

**Actividad:** evaluar `01`, `1101`, `100`, `0101`, `111`. Explicar por qué aceptar no significa detenerse al visitar q₂: importa el estado **después de procesar toda la cadena**.

### 6. Autómata aplicado: despachador de monedas

Una máquina vende un artículo de **\$3**, acepta monedas de **\$1 y \$2**, despacha al alcanzar o superar \$3 y **no devuelve cambio**. Tras despachar, reinicia el saldo a cero. Los estados representan saldo acumulado: q₀=\$0, q₁=\$1 y q₂=\$2.

Es una **máquina de Mealy**: además de cambiar de estado, produce una salida según el estado actual y la entrada. Se añade $\lambda:Q\times\Sigma\to\Gamma$, con $\Gamma=\{\text{Esperar},\text{Despachar}\}$.

| Estado | Moneda | Estado siguiente | Salida |
|---|---:|---|---|
| q₀ | \$1 | q₁ | Esperar |
| q₀ | \$2 | q₂ | Esperar |
| q₁ | \$1 | q₂ | Esperar |
| q₁ | \$2 | q₀ | Despachar |
| q₂ | \$1 | q₀ | Despachar |
| q₂ | \$2 | q₀ | Despachar |

**Corrida:** entradas `1, 1, 2, 2, 1`.

| Paso | Moneda | Estado anterior | Salida | Estado posterior |
|---|---:|---|---|---|
| 1 | 1 | q₀ | Esperar | q₁ |
| 2 | 1 | q₁ | Esperar | q₂ |
| 3 | 2 | q₂ | Despachar | q₀ |
| 4 | 2 | q₀ | Esperar | q₂ |
| 5 | 1 | q₂ | Despachar | q₀ |

**Resultado:** dos productos entregados. En el paso 3 se introducen \$4 para un producto de \$3 y se conserva \$1 de excedente por la regla establecida.

**Reto de diseño:** ¿qué estados o salidas serían necesarios para devolver cambio, indicar inventario agotado o bloquear monedas mientras se despacha? Distinguir estado, entrada, condición y acción.

### 7. Alcanzabilidad y determinismo

En grafos preguntamos si hay un camino entre nodos; en autómatas preguntamos si **existe una secuencia de entradas** que lleve del estado inicial a otro. En una máquina determinista una misma secuencia, desde un mismo estado, produce siempre la misma secuencia de estados. Esto no significa que el entorno que produce las entradas sea predecible.

---

## III. Grafos de conocimiento y ontologías (60 min)

### 8. Del arco etiquetado a la tripleta RDF

En un mapa, A—B puede significar carretera; en un autómata, q₀→q₁ puede significar entrada `1`; en un grafo de conocimiento, una arista etiquetada expresa una relación con significado.

La unidad básica de RDF es una **tripleta**:

$$
(s,p,o)=(\text{sujeto},\text{predicado},\text{objeto}).
$$

| Sujeto | Predicado | Objeto |
|---|---|---|
| Juan | opera | Avión01 |
| Avión01 | utiliza | Pista03 |
| Pista03 | perteneceA | Aeropuerto01 |
| Juan | esUn | Piloto |
| Piloto | subClaseDe | Persona |

En RDF real, los recursos y predicados se identifican mediante IRIs; el objeto puede ser otro recurso o un literal. La tabla es una notación simplificada para trabajar a mano.

**Consulta por recorrido:** ¿qué aeropuerto se relaciona con el avión operado por Juan? Se sigue `opera → utiliza → perteneceA`. Encontrar el camino **no prueba automáticamente** una nueva relación: la composición semántica requiere reglas o una consulta que especifique esa secuencia.

### 9. Clases, conjuntos y ontologías

Una **clase** agrupa individuos de un tipo. Una **taxonomía** organiza clases jerárquicamente. Una **ontología** especifica vocabulario, clases, propiedades y axiomas que permiten interpretar afirmaciones.

$$
\text{Piloto}\subseteq\text{Persona},\qquad \text{Juan}\in\text{Piloto}.
$$

De estas premisas se deduce $\text{Juan}\in\text{Persona}$. Es una **deducción**: la conclusión se sigue necesariamente si las premisas son válidas. La **inducción**, en cambio, propone generalizaciones a partir de observaciones y no ofrece la misma garantía lógica.

Las relaciones también pueden tener propiedades: inversa, simétrica, transitiva, dominio y rango. Por ejemplo, `conoceA` **no** es necesariamente transitiva: si Ana conoce a Beto y Beto conoce a Carla, no se sigue que Ana conozca a Carla.

### 10. Inferencia simbólica

Definimos reglas sencillas:

$$
\text{Piloto}(x)\Rightarrow\text{Persona}(x)
$$

$$
\text{Opera}(x,y)\land\text{Avión}(y)\Rightarrow\text{OperaAeronave}(x)
$$

**Hechos iniciales:** `Piloto(Juan)`, `Opera(Juan,Avión01)`, `Avión(Avión01)`.

**Conclusiones justificadas:** `Persona(Juan)` y `OperaAeronave(Juan)`. No podemos deducir que Juan es propietario del avión ni que está volando en este momento.

**Actividad de cierre del bloque:** identificar, para cada afirmación, si es un hecho explícito, una consecuencia inferida o una proposición no justificada.

### 11. Consistencia y mundo abierto

Si declaramos que `PistaLibre` y `PistaObstruida` son clases disjuntas, un mismo individuo no puede pertenecer a ambas en un modelo consistente. **Sin ese axioma, las dos etiquetas no producen por sí solas una contradicción formal.**

En la semántica de mundo abierto de OWL, **no saber que una pista está obstruida no demuestra que esté libre**. Esto contrasta con muchas consultas operativas que tratan la ausencia de registros como ausencia de hechos bajo reglas explícitas de negocio.

---

## IV. Integración: conocer, decidir y actuar (20 min)

Se dispone de las siguientes tripletas:

| Sujeto | Predicado | Objeto |
|---|---|---|
| Vuelo23 | utiliza | Pista01 |
| Objeto17 | estáEn | Pista01 |
| Objeto17 | esUn | Obstáculo |

**Regla de conocimiento:**

$$
\text{Obstáculo}(o)\land\text{EstáEn}(o,p)\Rightarrow\text{RequiereInspección}(p).
$$

**Máquina de estados de la pista:** $Q=\{\text{Libre},\text{Inspección},\text{Bloqueada}\}$. Por ejemplo, $\delta(\text{Libre},\text{ordenInspección})=\text{Inspección}$.

**Cadena de razonamiento:** las tripletas permiten inferir `RequiereInspección(Pista01)`. Una **política de control** convierte esa conclusión en el evento `ordenInspección`. La máquina cambia de Libre a Inspección. La inferencia no altera automáticamente el estado físico de la pista.

**Pregunta final:** ¿qué información faltaría para autorizar la apertura de la pista? Diferenciar la evidencia disponible, la decisión y la acción.

---

## Cinco preguntas para investigar y discutir

**1. ¿Un grafo dirigido puede representar uno no dirigido?**  
*Respuesta parcial:* sí, sustituyendo cada arista no dirigida por dos arcos opuestos. **Reto:** ¿qué cambia si los pesos de ida y vuelta son distintos?

**2. ¿Por qué Dijkstra fija definitivamente un nodo?**  
*Respuesta parcial:* con pesos no negativos, ningún desvío posterior puede reducir la distancia del nodo pendiente que ya tiene la menor distancia tentativa. **Reto:** construir un ejemplo con un peso negativo y examinar qué falla.

**3. ¿Una máquina determinista puede tener comportamiento impredecible para un observador?**  
*Respuesta parcial:* sí, si las entradas futuras son desconocidas. **Reto:** diferenciar incertidumbre sobre las entradas de indeterminismo de la función de transición.

**4. ¿Tener una ruta entre entidades significa que existe una inferencia válida?**  
*Respuesta parcial:* no; las etiquetas y axiomas determinan qué composiciones son legítimas. **Reto:** comparar `estáEn` con `conoceA` y analizar transitividad.

**5. ¿Un sistema puede ser consistente y, aun así, estar equivocado?**  
*Respuesta parcial:* sí; consistencia lógica no garantiza correspondencia con el mundo. **Reto:** proponer una ontología coherente pero basada en una premisa empírica falsa.

---

## Tres casos históricos

### Caso 1. Los siete puentes de Königsberg (Euler, 1736)

El problema consistía en recorrer siete puentes cruzando cada uno exactamente una vez. Euler abstrajo las regiones terrestres como vértices y los puentes como aristas: el problema dependía de la estructura de conexiones, no de las distancias del mapa. **Pregunta:** ¿qué se gana al eliminar detalles físicos irrelevantes?

### Caso 2. Autómatas finitos y teoría de la computación (décadas de 1940–1950)

Los trabajos de McCulloch y Pitts sobre redes lógicas (1943), Kleene sobre eventos regulares (1956) y Rabin y Scott sobre autómatas finitos (1959) ayudaron a formalizar sistemas que procesan secuencias mediante estados y transiciones. **Pregunta:** ¿por qué un reconocedor de cadenas puede modelarse con memoria finita?

### Caso 3. Web semántica y RDF (finales de los 1990–2000)

RDF surgió como una forma estandarizada de describir recursos mediante relaciones. La visión de la Web Semántica impulsó la representación explícita de significado, vocabularios compartidos y razonamiento automatizado; OWL añadió expresividad ontológica. **Pregunta:** ¿qué diferencia existe entre enlazar dos páginas y declarar formalmente una relación entre dos entidades?

---

## Línea de tiempo

| Año | Hito | Conexión con la sesión |
|---|---|---|
| 1736 | Euler estudia los puentes de Königsberg | Nace una formulación fundacional de grafos |
| 1936 | Turing formaliza un modelo abstracto de computación | Estados, símbolos y reglas de operación |
| 1943 | McCulloch y Pitts estudian redes lógicas | Relación entre computación y sistemas formales |
| 1956 | Dijkstra concibe su algoritmo de camino mínimo | Optimización de recorridos |
| 1959 | Publicación del algoritmo de Dijkstra y trabajos de Rabin–Scott | Caminos mínimos y autómatas finitos |
| 1999 | Recomendación inicial de RDF del W3C | Tripletas para describir recursos |
| 2004 | OWL se convierte en recomendación del W3C | Ontologías para la Web Semántica |
| 2012 | OWL 2, segunda edición de la recomendación | Ampliación y consolidación del estándar |

---

## Conexiones con los siguientes módulos

**Python:** grafos como diccionarios y listas de adyacencia; tablas de transición como diccionarios; RDF como tripletas procesables. BFS, DFS y Dijkstra pueden implementarse posteriormente.

**Ciencia de datos:** entidades y relaciones como estructura de datos; granularidad de los registros; grafos como representaciones de interacciones; diferencias entre observación, hipótesis y conclusión.

**Redes neuronales:** una red neuronal también tiene nodos y conexiones, pero sus pesos suelen ser parámetros aprendidos y no distancias de carretera ni predicados RDF. En una red neuronal recurrente, el estado interno evoluciona; esa analogía no convierte automáticamente a una red neuronal en un autómata finito.

**Sistemas cognitivos:** un grafo organiza relaciones; una ontología formaliza conocimiento; una máquina de estados gobierna comportamiento. Una arquitectura puede integrar los tres, pero necesita reglas explícitas para transformar inferencias en decisiones y acciones.

---

## Síntesis final

| Modelo | Estructura mínima | Pregunta principal | Operación práctica |
|---|---|---|---|
| Grafo | $G=(V,E)$ | ¿Cómo se conectan los elementos? | Recorrer y optimizar caminos |
| Autómata | $(Q,\Sigma,\delta,q_0,F)$ | ¿Qué sucede con cada entrada? | Actualizar estados |
| Conocimiento | Tripletas + axiomas + reglas | ¿Qué significa y qué se deduce? | Inferir consecuencias |

**Idea central:** un grafo no es únicamente un mapa de rutas. Puede describir la estructura de un sistema, sus cambios posibles o las relaciones que sustentan su conocimiento. La interpretación de los nodos, las aristas y las reglas determina qué preguntas podemos responder.

## Referencias para profundizar

- Euler, L. (1736). *Solutio problematis ad geometriam situs pertinentis*.
- Dijkstra, E. W. (1959). *A note on two problems in connexion with graphs*. *Numerische Mathematik*, 1, 269–271. DOI: 10.1007/BF01386390.
- Rabin, M. O., & Scott, D. (1959). *Finite automata and their decision problems*. *IBM Journal of Research and Development*, 3(2), 114–125. DOI: 10.1147/rd.32.0114.
- W3C (2014). *RDF 1.1 Concepts and Abstract Syntax*. https://www.w3.org/TR/rdf11-concepts/
- W3C (2012). *OWL 2 Web Ontology Language Document Overview (Second Edition)*. https://www.w3.org/TR/owl2-overview/
- Russell, S., & Norvig, P. *Artificial Intelligence: A Modern Approach*. Secciones sobre búsqueda, representación del conocimiento y razonamiento.
