# Módulo 1.3 — Lógica difusa e inferencia en entornos de software

> **Inteligencia Artificial**  
> **Módulo 1 — Sistemas cognitivos y representación del conocimiento**  
> **Tema:** Lógica difusa e inferencia en entornos de software

## Introducción

Muchos criterios de ingeniería no tienen fronteras naturales exactas. Una superficie puede estar *poco*, *moderadamente* o *muy* contaminada; una inspección puede ser *reciente* o estar *próxima a vencer*; una carga puede ser *alta* sin que exista un único valor universal a partir del cual cambie abruptamente de baja a alta.

La **lógica difusa** permite representar estas transiciones graduales mediante grados de pertenencia entre 0 y 1. Sobre esa representación, un sistema de inferencia puede combinar mediciones y reglas lingüísticas para producir una recomendación, una señal de control o una puntuación interpretable.

Esto no elimina la precisión de la ingeniería. Por el contrario, obliga a declarar:

- qué significa cada término lingüístico;
- cómo se convierten las mediciones en grados de pertenencia;
- qué reglas relacionan las entradas con las salidas;
- cómo se resuelven coincidencias y conflictos;
- qué ocurre cuando faltan datos o ninguna regla aplica;
- quién conserva la autoridad sobre la decisión final.

La pregunta central de este tema es:

> **¿Cómo convertir criterios graduales expresados en lenguaje humano en inferencias computables, verificables y gobernables?**

---

## 1. Fundamentos de lógica difusa

### 1.1 De los conjuntos clásicos a los conjuntos difusos

En un conjunto clásico, un elemento pertenece o no pertenece:

\[
\chi_A(x)\in\{0,1\}
\]

En un conjunto difuso, la función de pertenencia admite valores intermedios:

\[
\mu_A:X\rightarrow[0,1]
\]

Si `x = 70` es un índice de residuos y \(\mu_{alto}(70)=0.5\), la expresión significa que el valor 70 tiene grado 0.5 de pertenencia al concepto definido como **residuo alto**.

El grado depende del modelo construido. No es una propiedad física aislada ni una frecuencia observada: expresa en qué medida un valor satisface un concepto gradual.

### 1.2 Vaguedad no es probabilidad

La lógica difusa y la probabilidad responden preguntas distintas:

| Enfoque | Pregunta | Ejemplo |
|---|---|---|
| lógica clásica | ¿pertenece o no? | la pista está bloqueada |
| lógica difusa | ¿en qué grado satisface el concepto? | el nivel de residuo es alto en grado 0.5 |
| probabilidad | ¿qué tan incierto es que ocurra un evento? | existe 27 % de probabilidad de contaminación |

Por tanto:

\[
\mu_{alto}(70)=0.5 \not\Rightarrow P(\text{contaminación})=0.5
\]

Ambos enfoques pueden coexistir. Un sistema puede estimar probabilísticamente la presencia de una falla y, de manera separada, evaluar difusamente si su severidad es baja, media o alta. La semántica de cada valor debe conservarse durante todo el proceso.

### 1.3 Universo de discurso

El **universo de discurso** es el intervalo o conjunto de valores sobre el cual se define una variable. Por ejemplo:

```text
Variable: índice de residuos
Universo: [0, 100]
Unidad o escala: índice normalizado
Términos: bajo, medio, alto
```

Un universo mal delimitado deforma la interpretación. También debe indicarse si la escala es física, ordinal, normalizada o construida a partir de varias mediciones.

### 1.4 Variable lingüística

Una **variable lingüística** toma palabras o expresiones como valores. Su especificación incluye:

1. nombre de la variable;
2. universo de discurso;
3. términos lingüísticos;
4. función de pertenencia de cada término;
5. unidad, fuente y condiciones de validez.

Ejemplo:

```text
antigüedad_de_inspección ∈ [0, 60] minutos
{reciente, próxima_a_vencer, vencida}
```

### 1.5 Funciones de pertenencia

Las formas más frecuentes son:

- **triangular:** simple, interpretable y económica;
- **trapezoidal:** útil cuando existe una región completa de pertenencia máxima;
- **gaussiana:** produce transiciones suaves;
- **sigmoidal:** adecuada para conceptos que crecen o decrecen de forma monotónica;
- **por tramos o aprendida:** útil cuando el dominio exige una forma particular.

Función triangular:

\[
\operatorname{tri}(x;a,b,c)=
\max\left(\min\left(\frac{x-a}{b-a},\frac{c-x}{c-b}\right),0\right)
\]

donde \(a\) y \(c\) delimitan el soporte y \(b\) es el punto de pertenencia máxima.

La forma elegida debe justificarse con conocimiento experto, datos, normas o una combinación de éstos. Una curva estéticamente suave no es necesariamente una buena representación del dominio.

### 1.6 Solapamiento y partición lingüística

Un valor puede pertenecer simultáneamente a varios términos. Por ejemplo:

```text
μ_medio(70) = 0.33
μ_alto(70)  = 0.50
```

Este solapamiento evita saltos artificiales y permite transiciones graduales. Sin embargo, un solapamiento excesivo vuelve indistinguibles los términos; uno insuficiente puede dejar zonas sin cobertura.

### 1.7 Operaciones difusas

Con los operadores estándar de Zadeh:

\[
\mu_{\neg A}(x)=1-\mu_A(x)
\]

\[
\mu_{A\cap B}(x)=\min(\mu_A(x),\mu_B(x))
\]

\[
\mu_{A\cup B}(x)=\max(\mu_A(x),\mu_B(x))
\]

En una regla, `Y` suele implementarse con una **t-norma** y `O` con una **s-norma**. Mínimo y máximo son elecciones comunes, pero no las únicas. También existen el producto algebraico y la suma probabilística. Cambiar el operador puede cambiar la salida, por lo que debe formar parte de la especificación versionada.

### 1.8 Cortes alfa

El corte alfa convierte un conjunto difuso en uno clásico para un nivel dado:

\[
A_\alpha=\{x\in X\mid \mu_A(x)\geq\alpha\}
\]

Los cortes alfa ayudan a inspeccionar rangos, comparar conjuntos y comunicar qué valores satisfacen un concepto al menos en cierto grado. No sustituyen el razonamiento difuso; son una vista útil de él.

---

## 2. Anatomía de un sistema de inferencia difusa

Un **sistema de inferencia difusa** transforma entradas numéricas o simbólicas en una salida mediante funciones de pertenencia y reglas.

```text
medición
   ↓
validación y normalización
   ↓
fuzzificación
   ↓
evaluación de reglas
   ↓
implicación y agregación
   ↓
desfuzzificación o promedio ponderado
   ↓
salida + traza de explicación
```

### 2.1 Fuzzificación

Convierte una entrada concreta en grados de pertenencia:

```text
residuo = 70
→ bajo: 0.00
→ medio: 0.33
→ alto: 0.50
```

El sistema no reemplaza el valor original. Lo conserva junto con unidad, tiempo, procedencia y versión de la función utilizada.

### 2.2 Base de conocimiento

Contiene dos componentes:

- **base de datos difusa:** universos, variables y funciones de pertenencia;
- **base de reglas:** relaciones lingüísticas entre antecedentes y consecuentes.

Ejemplo:

```text
SI residuo ES alto O inspección ES vencida
ENTONCES urgencia ES muy_alta
```

Las reglas deben expresar conocimiento del dominio. Si sólo reproducen condiciones arbitrarias del código, el sistema será difícil de validar y explicar.

### 2.3 Activación de reglas

Para una regla con conjunción:

\[
\alpha_i=\min(\mu_A(x),\mu_B(y))
\]

Para una regla con disyunción:

\[
\alpha_i=\max(\mu_A(x),\mu_B(y))
\]

\(\alpha_i\) es la fuerza de activación de la regla. Puede interpretarse como el grado con el que el caso satisface sus antecedentes, no como la probabilidad de que la regla sea correcta.

### 2.4 Implicación y agregación

En un sistema Mamdani, cada regla produce un conjunto difuso de salida. La fuerza de activación recorta o escala su función de pertenencia. Después, las salidas de las reglas se agregan en un solo conjunto.

Estas decisiones —recorte o escalamiento, máximo o suma acotada— deben mantenerse explícitas porque influyen en el resultado.

### 2.5 Desfuzzificación

Cuando la aplicación necesita una salida numérica, el conjunto agregado se transforma en un valor concreto. El método de centroide es común:

\[
y^*=\frac{\int y\,\mu_{salida}(y)\,dy}
{\int \mu_{salida}(y)\,dy}
\]

Otros métodos incluyen bisector, media de máximos y máximo izquierdo o derecho. Cada uno conserva propiedades diferentes.

### 2.6 La salida no es todavía la decisión

Una puntuación difusa debe pasar por una **capa de política** antes de producir una acción:

```text
inferencia: urgencia = 78/100
política: puntuación > 65 requiere inspección
autoridad: supervisor confirma bloqueo o liberación
```

Separar inferencia, política y autoridad permite cambiar umbrales operativos sin alterar el significado de las variables y evita que una recomendación se confunda con una autorización.

---

## 3. Modelos principales de inferencia

### 3.1 Mamdani

En el modelo de Mamdani, los consecuentes son conjuntos difusos:

```text
SI temperatura ES alta Y presión ES media
ENTONCES apertura ES grande
```

**Fortalezas:**

- reglas cercanas al lenguaje del especialista;
- buena trazabilidad conceptual;
- salida interpretable como conjunto difuso.

**Limitaciones:**

- requiere agregación y desfuzzificación;
- puede aumentar el costo cuando existen muchas reglas y salidas;
- la superficie final depende de varios operadores de diseño.

### 3.2 Takagi–Sugeno

En un sistema Takagi–Sugeno, el consecuente es una constante o función de las entradas:

\[
R_i:\quad \text{SI }x\text{ es }A_i\text{ Y }z\text{ es }B_i,
\quad \text{ENTONCES }f_i=p_i x+q_i z+r_i
\]

La salida se obtiene como promedio ponderado:

\[
y^*=\frac{\sum_i \alpha_i f_i}{\sum_i\alpha_i}
\]

Si \(f_i\) es constante, se denomina Sugeno de orden cero.

**Fortalezas:**

- cálculo eficiente y continuo;
- integración conveniente con optimización y aprendizaje;
- apropiado para control y aproximación funcional.

**Limitaciones:**

- los consecuentes son menos lingüísticos;
- una regla con una ecuación aprendida puede ser menos fácil de explicar;
- necesita controles para evitar que la optimización destruya la interpretabilidad.

### 3.3 Tsukamoto

En Tsukamoto, cada consecuente utiliza una función de pertenencia monotónica y produce un valor concreto por regla. La salida final también es un promedio ponderado. Es útil cuando cada regla debe asociarse con una respuesta numérica inequívoca.

### 3.4 Comparación resumida

| Criterio | Mamdani | Sugeno | Tsukamoto |
|---|---|---|---|
| consecuente | conjunto difuso | constante o función | conjunto monotónico |
| salida por regla | conjunto recortado o escalado | valor numérico | valor numérico |
| salida final | desfuzzificación | promedio ponderado | promedio ponderado |
| legibilidad lingüística | alta | media | media |
| eficiencia computacional | media | alta | alta |
| uso frecuente | decisión explicable, control | control, modelado, aprendizaje | control monotónico |

---

## 4. Inferencia difusa en una arquitectura de software

### 4.1 Capas recomendadas

| Capa | Responsabilidad | Riesgo que controla |
|---|---|---|
| adaptadores de entrada | reciben sensores, formularios o servicios | formatos incompatibles |
| validación y unidades | verifica rango, antigüedad, unidad y calidad | datos imposibles o desactualizados |
| transformación | normaliza sin perder el valor original | escalas ambiguas |
| motor difuso | aplica pertenencias, operadores y reglas | inferencia opaca |
| política | convierte la salida en recomendación operativa | confundir puntuación con autoridad |
| integración | publica respuesta o activa un flujo | efectos no controlados |
| observabilidad | registra entradas, reglas, versiones y salida | falta de auditoría |

### 4.2 Contrato de entrada y salida

Un servicio no debería recibir sólo números sin contexto:

```json
{
  "residue_index": 70,
  "inspection_age_min": 40,
  "observed_at": "2026-10-27T10:15:00-06:00",
  "source": "sensor-S17",
  "model_version": "runway-fis-1.0"
}
```

Una respuesta explicable puede incluir:

```json
{
  "urgency_score": 78,
  "recommendation": "inspect_and_escalate",
  "memberships": {
    "residue": {"low": 0, "medium": 0.333, "high": 0.5},
    "inspection": {"recent": 0, "due": 0.333, "expired": 0.333}
  },
  "fired_rules": [
    {"id": "R1", "strength": 0.5},
    {"id": "R2", "strength": 0.333}
  ],
  "model_version": "runway-fis-1.0"
}
```

La traza facilita explicación, pruebas y reproducción. No debe exponer datos sensibles ni sustituye los registros de seguridad del sistema.

### 4.3 Versionado

Conviene versionar conjuntamente:

- universos y unidades;
- funciones de pertenencia;
- operadores `Y`, `O` y negación;
- reglas, prioridades y pesos;
- método de agregación y salida;
- política de interpretación;
- datos y criterios usados para validar el modelo.

Modificar una sola frontera puede alterar varias reglas simultáneamente. Por eso no debe desplegarse como un cambio cosmético.

### 4.4 Manejo de entradas incompletas

Si falta una entrada, el sistema debe seguir una política explícita:

- rechazar la inferencia;
- aplicar sólo un subsistema válido;
- usar un valor estimado y etiquetarlo;
- solicitar una nueva medición;
- devolver `cobertura_insuficiente`.

Asignar silenciosamente cero suele ser incorrecto: cero puede ser una medición válida y no equivale a “desconocido”.

### 4.5 Escalabilidad de las reglas

Con \(n\) variables y \(k\) términos por variable, una partición completa puede producir hasta \(k^n\) combinaciones. Para evitar una explosión de reglas se utilizan:

- subsistemas jerárquicos;
- reglas dispersas centradas en regiones relevantes;
- agrupación por contexto;
- modelos híbridos;
- aprendizaje con restricciones;
- revisión de reglas redundantes o dominadas.

Reducir reglas no debe crear zonas sin cobertura ni eliminar excepciones de seguridad.

---

## 5. Cinco preguntas de interés

### Pregunta 1. ¿Cómo se eligen las funciones de pertenencia?

No existe una forma universal. Pueden obtenerse mediante:

1. entrevistas y ejercicios de clasificación con especialistas;
2. normas y límites operativos;
3. análisis de distribución y agrupamiento de datos;
4. optimización supervisada;
5. una estrategia híbrida que aprende parámetros dentro de restricciones expertas.

La respuesta no termina al ajustar una curva. Debe evaluarse cobertura, sensibilidad, estabilidad, interpretabilidad y desempeño en casos extremos. Si dos especialistas discrepan, el desacuerdo debe registrarse y resolverse con evidencia o políticas, no promediarse sin explicación.

### Pregunta 2. ¿Cuándo usar lógica difusa y cuándo probabilidad?

La lógica difusa es apropiada cuando el problema central es la **gradualidad semántica**: caliente, cercano, riesgoso o prioritario. La probabilidad es apropiada cuando el problema central es la **incertidumbre acerca de hechos o eventos**.

Una aplicación puede requerir ambas. Por ejemplo:

```text
modelo probabilístico → P(objeto en pista | señales)
modelo difuso         → severidad operacional de la situación
política              → acción permitida según evidencia y severidad
```

La investigación híbrida estudia cómo combinarlas sin borrar sus significados.

### Pregunta 3. ¿Cómo conservar interpretabilidad al crecer el sistema?

La interpretabilidad disminuye cuando existen demasiadas variables, funciones muy irregulares, reglas redundantes o consecuentes complejos. Algunas respuestas parciales son:

- vocabulario limitado y estable;
- reglas cortas y con identificador;
- módulos por contexto;
- detección de conflictos y redundancias;
- explicaciones locales con las reglas realmente activadas;
- comparación de versiones mediante superficies de respuesta.

La comprensibilidad no depende sólo del número de reglas: también depende de si sus términos corresponden con conceptos reconocibles para el usuario.

### Pregunta 4. ¿Puede aprenderse un sistema difuso a partir de datos?

Sí. Métodos neurodifusos como ANFIS ajustan parámetros de funciones y consecuentes mediante aprendizaje. También pueden descubrirse reglas con agrupamiento u optimización.

La respuesta sigue siendo parcial: mejorar una métrica predictiva puede generar conjuntos difíciles de nombrar, reglas contradictorias o comportamiento no monotónico. En dominios regulados conviene imponer restricciones, conservar versiones, validar fuera de muestra y exigir revisión humana.

### Pregunta 5. ¿Cómo se verifica un motor de inferencia difusa?

La exactitud promedio es insuficiente. Se requieren pruebas de:

- límites y puntos de cruce;
- cobertura del universo;
- continuidad esperada;
- monotonicidad cuando el dominio la exige;
- conflictos entre reglas;
- valores faltantes, infinitos o fuera de rango;
- conversión de unidades;
- reproducción determinista;
- regresión entre versiones;
- trazabilidad de cada resultado.

La investigación en verificación busca combinar pruebas numéricas, análisis formal y validación con especialistas.

---

## 6. Tres casos de estudio

### Caso 1. Control lingüístico de una máquina de vapor

En 1975, Ebrahim Mamdani y Sedrak Assilian mostraron un controlador que traducía reglas lingüísticas heurísticas para operar una combinación de máquina de vapor y caldera. El caso fue decisivo porque demostró que expresiones cercanas al razonamiento del operador podían convertirse en control computacional.

**Representación simplificada:**

```text
SI error ES positivo_grande
Y cambio_del_error ES positivo
ENTONCES cambio_de_control ES negativo_grande
```

**Aprendizajes:**

- las reglas pueden capturar experiencia procedimental;
- las particiones lingüísticas hacen visible el diseño;
- estabilidad, respuesta y seguridad deben validarse además de la legibilidad;
- una base de reglas no sustituye el análisis del sistema físico.

### Caso 2. Modelado Takagi–Sugeno y aprendizaje neurodifuso

Takagi y Sugeno propusieron en 1985 representar regiones difusas de entrada con consecuentes funcionales. Esto facilita aproximar sistemas no lineales mediante modelos locales que se combinan suavemente. En 1993, Jang presentó ANFIS, una arquitectura de red adaptativa capaz de ajustar sistemas de inferencia difusa con datos.

**Esquema:**

```text
región difusa 1 → modelo lineal local 1
región difusa 2 → modelo lineal local 2
región difusa 3 → modelo lineal local 3
                 ↓
           promedio ponderado
```

**Aprendizajes:**

- un sistema complejo puede aproximarse mediante comportamientos locales;
- aprendizaje e interpretación pueden combinarse, pero existe tensión entre ambos;
- el conjunto de entrenamiento debe cubrir la región operativa;
- las restricciones físicas y de seguridad no deben aprenderse sólo por correlación.

### Caso 3. Prioridad para inspeccionar o liberar una pista

El caso de las pistas puede extenderse con una capa difusa que traduzca mediciones graduales en una **urgencia de inspección**. La salida no libera ni bloquea la pista por sí sola: apoya una decisión gobernada por protocolos, evidencia y autoridad humana.

**Entradas:**

- índice de residuos de 0 a 100;
- minutos desde la última inspección válida.

**Salida:**

- urgencia de inspección de 0 a 100.

**Separación necesaria:**

```text
señales → evaluación difusa → recomendación
                              ↓
evidencia + protocolo + autoridad → decisión y registro
```

Este caso se desarrolla matemáticamente en la sección 8.

---

## 7. Línea de tiempo

| Año | Hito | Importancia |
|---:|---|---|
| 1920–1930 | desarrollo de lógicas multivaluadas | cuestiona que toda proposición deba operar sólo con dos valores |
| 1965 | Lotfi A. Zadeh publica *Fuzzy Sets* | formaliza conjuntos con grados continuos de pertenencia |
| 1973 | Zadeh desarrolla la noción de variables lingüísticas | conecta términos del lenguaje con restricciones difusas |
| 1975 | Mamdani y Assilian presentan control lingüístico experimental | demuestra una aplicación de reglas difusas a control |
| 1985 | Takagi y Sugeno proponen identificación y modelado difuso | introduce consecuentes funcionales y modelos locales |
| 1980–1990 | expansión de controladores difusos industriales | muestra su utilidad en control, automatización y productos de consumo |
| 1993 | Jang presenta ANFIS | integra aprendizaje adaptativo y sistemas de inferencia difusa |
| 1990–2000 | consolidación de sistemas difusos tipo 2 | permite representar incertidumbre sobre las propias pertenencias |
| 2000–2020 | sistemas híbridos, evolutivos y neurodifusos | automatizan parte del diseño y ajuste de reglas |
| actualidad | integración con analítica, sistemas embebidos e IA explicable | renueva el interés por modelos auditables y conocimiento experto |

La evolución no reemplaza automáticamente los modelos anteriores. Un sistema Mamdani pequeño puede ser preferible a uno aprendido si la explicación y el control de cambios son prioritarios.

---

## 8. Modelo matemático aplicado: urgencia de inspección de una pista

### 8.1 Objetivo y límites

Se construirá un sistema Sugeno de orden cero para estimar una urgencia \(u\in[0,100]\). Es un ejemplo didáctico, no un procedimiento aeronáutico certificado.

La puntuación:

- no es una probabilidad de accidente;
- no demuestra que exista contaminación;
- no autoriza liberar o bloquear una pista;
- sí resume cómo dos mediciones satisfacen criterios graduales definidos.

### 8.2 Variables de entrada

1. Índice de residuos \(r\in[0,100]\).
2. Antigüedad de la inspección \(t\in[0,60]\) minutos.

Para evitar divisiones indefinidas en los hombros, se expresan sus funciones por tramos.

#### Residuo bajo

\[
\mu_{bajo}(r)=
\begin{cases}
1 & 0\le r\le20\\
\frac{40-r}{20} & 20<r<40\\
0 & r\ge40
\end{cases}
\]

#### Residuo medio

\[
\mu_{medio}(r)=\operatorname{tri}(r;20,50,80)
\]

#### Residuo alto

\[
\mu_{alto}(r)=
\begin{cases}
0 & r\le60\\
\frac{r-60}{20} & 60<r<80\\
1 & 80\le r\le100
\end{cases}
\]

#### Inspección reciente

\[
\mu_{reciente}(t)=
\begin{cases}
1 & 0\le t\le10\\
\frac{25-t}{15} & 10<t<25\\
0 & t\ge25
\end{cases}
\]

#### Inspección próxima a vencer

\[
\mu_{por\_vencer}(t)=\operatorname{tri}(t;15,30,45)
\]

#### Inspección vencida

\[
\mu_{vencida}(t)=
\begin{cases}
0 & t\le35\\
\frac{t-35}{15} & 35<t<50\\
1 & 50\le t\le60
\end{cases}
\]

### 8.3 Base mínima de reglas

```text
R1: SI residuo ES alto O inspección ES vencida
    ENTONCES urgencia = 90

R2: SI residuo ES medio Y inspección ES próxima_a_vencer
    ENTONCES urgencia = 60

R3: SI residuo ES bajo Y inspección ES reciente
    ENTONCES urgencia = 20
```

Esta base es deliberadamente pequeña para explicar el cálculo. Antes de usarla en un sistema real habría que verificar cobertura y añadir reglas para combinaciones como residuo bajo con inspección vencida.

### 8.4 Evaluación de un caso

Supóngase:

\[
r=70,\qquad t=40
\]

Pertenencias del residuo:

\[
\mu_{bajo}(70)=0
\]

\[
\mu_{medio}(70)=\frac{80-70}{80-50}=\frac{1}{3}\approx0.333
\]

\[
\mu_{alto}(70)=\frac{70-60}{80-60}=0.5
\]

Pertenencias de la inspección:

\[
\mu_{reciente}(40)=0
\]

\[
\mu_{por\_vencer}(40)=\frac{45-40}{45-30}=\frac{1}{3}
\]

\[
\mu_{vencida}(40)=\frac{40-35}{50-35}=\frac{1}{3}
\]

### 8.5 Activación de reglas

Con `O = máximo` y `Y = mínimo`:

\[
\alpha_1=\max\left(0.5,\frac{1}{3}\right)=0.5
\]

\[
\alpha_2=\min\left(\frac{1}{3},\frac{1}{3}\right)=\frac{1}{3}
\]

\[
\alpha_3=\min(0,0)=0
\]

### 8.6 Salida Sugeno

\[
u=\frac{\alpha_1(90)+\alpha_2(60)+\alpha_3(20)}
{\alpha_1+\alpha_2+\alpha_3}
\]

\[
u=\frac{0.5(90)+\frac{1}{3}(60)}{0.5+\frac{1}{3}}
=\frac{65}{5/6}=78
\]

Una política didáctica podría interpretar:

| Intervalo | Recomendación |
|---:|---|
| \(0\le u<35\) | monitorear |
| \(35\le u\le65\) | revisar evidencia |
| \(65<u\le100\) | inspeccionar y escalar |

Como \(u=78\), el sistema recomienda inspeccionar y escalar. La decisión de bloquear o liberar continúa en manos de la autoridad definida por el proceso.

### 8.7 Lectura de la explicación

El resultado puede explicarse sin afirmar que el sistema “piensa”:

1. el índice 70 activó `alto` con 0.5 y `medio` con 0.333;
2. los 40 minutos activaron `por_vencer` y `vencida` con 0.333;
3. R1 fue la regla dominante con fuerza 0.5;
4. R2 aportó una recomendación intermedia;
5. el promedio ponderado produjo 78.

### 8.8 Relación con evidencia probabilística

Si otro componente estima \(P(C\mid evidencia)=0.269\), ese valor debe conservarse como probabilidad. Puede combinarse en una capa posterior con la urgencia difusa, o convertirse en una variable lingüística sólo si la transformación y su significado se documentan.

No debe informarse:

```text
urgencia = 78 → probabilidad de contaminación = 78 %
```

La primera es una puntuación construida por reglas; la segunda requeriría un modelo probabilístico calibrado.

---

## 9. Implementación de referencia

El siguiente pseudocódigo muestra una implementación pequeña y explícita:

```python
def triangular(x, a, b, c):
    return max(min((x - a) / (b - a),
                   (c - x) / (c - b)), 0.0)

def low_residue(r):
    if r <= 20:
        return 1.0
    if r < 40:
        return (40 - r) / 20
    return 0.0

def high_residue(r):
    if r <= 60:
        return 0.0
    if r < 80:
        return (r - 60) / 20
    return 1.0

def recent_inspection(t):
    if t <= 10:
        return 1.0
    if t < 25:
        return (25 - t) / 15
    return 0.0

def expired_inspection(t):
    if t <= 35:
        return 0.0
    if t < 50:
        return (t - 35) / 15
    return 1.0

def infer_urgency(residue, inspection_age):
    if not 0 <= residue <= 100:
        raise ValueError("residue fuera de [0, 100]")
    if not 0 <= inspection_age <= 60:
        raise ValueError("inspection_age fuera de [0, 60]")

    memberships = {
        "low": low_residue(residue),
        "medium": triangular(residue, 20, 50, 80),
        "high": high_residue(residue),
        "recent": recent_inspection(inspection_age),
        "due": triangular(inspection_age, 15, 30, 45),
        "expired": expired_inspection(inspection_age),
    }

    rules = {
        "R1": max(memberships["high"], memberships["expired"]),
        "R2": min(memberships["medium"], memberships["due"]),
        "R3": min(memberships["low"], memberships["recent"]),
    }

    denominator = sum(rules.values())
    if denominator == 0:
        return {"status": "no_coverage", "memberships": memberships}

    urgency = (
        rules["R1"] * 90
        + rules["R2"] * 60
        + rules["R3"] * 20
    ) / denominator

    return {
        "status": "ok",
        "urgency": urgency,
        "memberships": memberships,
        "rules": rules,
    }
```

En producción habría que añadir control de `NaN`, fecha real de la observación, unidades, versión, autenticación, telemetría y una política segura ante fallas.

---

## 10. Verificación y validación

### 10.1 Pruebas unitarias de pertenencia

Para cada función deben comprobarse:

- extremos del universo;
- inicio y fin del soporte;
- punto de pertenencia máxima;
- puntos de cruce;
- valores inmediatamente a ambos lados de una frontera;
- garantía de que \(0\le\mu(x)\le1\).

Ejemplos:

```text
μ_alto(60) = 0
μ_alto(70) = 0.5
μ_alto(80) = 1
```

### 10.2 Pruebas de reglas

- cada regla debe poder activarse en al menos un caso válido;
- reglas duplicadas o dominadas deben identificarse;
- combinaciones incompatibles deben resolverse de forma explícita;
- un cambio de operador debe detectarse como cambio de comportamiento;
- la traza debe coincidir con el cálculo.

### 10.3 Cobertura

Puede explorarse una malla de valores sobre el universo y medir:

\[
\text{cobertura}(x)=\sum_i\alpha_i(x)
\]

Si la suma es cero, ninguna regla aplica. Una cobertura positiva tampoco garantiza una salida correcta: sólo demuestra que existe activación.

### 10.4 Monotonicidad

Si el conocimiento del dominio afirma que mayor residuo nunca debe reducir la urgencia, se prueba:

\[
r_1\le r_2\Rightarrow u(r_1,t)\le u(r_2,t)
\]

Una violación puede revelar reglas conflictivas, funciones mal ubicadas o una interacción legítima que requiere explicación.

### 10.5 Pruebas de regresión

Antes de publicar una nueva versión se comparan:

- casos de referencia acordados con especialistas;
- superficie completa de salida;
- máximas diferencias entre versiones;
- cambios de recomendación operativa;
- explicaciones y reglas dominantes.

### 10.6 Validación humana y operacional

El sistema debe evaluarse con casos reales y simulados, incluidos casos límite. Los especialistas validan la coherencia semántica; ingeniería valida desempeño y resiliencia; responsables operativos validan que la salida pueda integrarse sin crear una autoridad no prevista.

---

## 11. Errores frecuentes

1. **Interpretar pertenencia como probabilidad.** Cambia por completo el significado del resultado.
2. **Elegir funciones sólo por conveniencia visual.** Las fronteras deben justificarse.
3. **Ocultar unidades o normalizaciones.** Un 70 puede significar cosas distintas.
4. **Suponer que más reglas producen mejor conocimiento.** Pueden aumentar contradicción y mantenimiento.
5. **No definir el caso sin cobertura.** El denominador de Sugeno puede ser cero.
6. **Confundir explicación con validez.** Una regla legible puede ser incorrecta.
7. **Permitir que la salida ejecute acciones críticas sin política.** Inferir no equivale a autorizar.
8. **Ajustar con datos sin restricciones.** Puede mejorarse una métrica y perderse coherencia.
9. **No versionar funciones y reglas.** Impide reproducir decisiones anteriores.
10. **Decir que el sistema “razona como una persona”.** Ejecuta operaciones definidas sobre representaciones diseñadas.

---

## 12. Relación con los temas siguientes

### 12.1 Puente hacia ontologías y grafos de conocimiento

Una ontología puede definir qué son `Pista`, `Inspección`, `Observación` y `Recomendación`, mientras el sistema difuso calcula grados sobre algunas de sus propiedades.

```text
grafo u ontología → contexto, identidad y relaciones
motor difuso      → evaluación gradual
registro          → reglas, versión y procedencia
```

No todo grado difuso debe almacenarse como hecho permanente. Debe indicarse si es una entrada observada, una inferencia derivada o una puntuación temporal.

### 12.2 Puente hacia optimización de procesos

Una puntuación difusa puede alimentar:

- priorización de inspecciones;
- asignación de recursos;
- control adaptativo;
- programación de mantenimiento;
- selección de acciones bajo restricciones.

La optimización debe respetar límites duros. Una función objetivo puede balancear urgencia, costo y tiempo, pero no debería negociar una restricción de seguridad obligatoria.

### 12.3 Puente con sistemas cognitivos

La lógica difusa puede representar categorías graduales dentro de un sistema cognitivo, pero no constituye por sí sola una arquitectura cognitiva. Puede integrarse como mecanismo de percepción, evaluación o selección de acción junto con memoria, aprendizaje y planificación.

---

## 13. Actividades sugeridas

### Actividad 1. Diseñar una variable lingüística

Elegir una magnitud de ingeniería y documentar:

- universo y unidad;
- tres términos lingüísticos;
- funciones de pertenencia;
- justificación de fronteras;
- un caso ambiguo y su interpretación.

### Actividad 2. Comparar lo clásico y lo difuso

Construir un control por umbral y otro difuso para la misma variable. Evaluar valores cercanos a la frontera y explicar cuál cambia de manera más estable.

### Actividad 3. Auditar reglas

Crear entre cinco y nueve reglas, generar una tabla de combinaciones y localizar:

- huecos de cobertura;
- reglas redundantes;
- consecuentes en conflicto;
- casos que requieren una restricción dura.

### Actividad 4. Ejecutar el caso de la pista

Calcular manualmente la urgencia para:

```text
A: r = 10, t = 5
B: r = 50, t = 30
C: r = 85, t = 20
D: r = 25, t = 55
```

Después comparar resultados con la implementación y explicar qué reglas se activaron.

### Actividad 5. Proponer una prueba adversa

Definir qué debería ocurrir con:

- valor fuera de rango;
- unidad incorrecta;
- dato ausente;
- inspección con fecha futura;
- versión de reglas desconocida;
- ninguna regla activada.

---

## 14. Preguntas de comprobación

1. ¿Qué diferencia existe entre un grado de pertenencia y una probabilidad?
2. ¿Por qué un valor puede pertenecer a dos términos lingüísticos al mismo tiempo?
3. ¿Qué decisiones de diseño intervienen entre fuzzificación y salida?
4. ¿En qué se diferencian los consecuentes de Mamdani y Sugeno?
5. ¿Qué significa que una base de reglas no tenga cobertura?
6. ¿Por qué la salida difusa debe separarse de la autoridad operativa?
7. ¿Qué pruebas permiten detectar discontinuidades o comportamiento no monotónico?
8. ¿Cómo puede integrarse un resultado difuso con una ontología?
9. ¿Qué se gana y qué se arriesga al aprender funciones desde datos?
10. ¿Cómo reconstruiría el sistema la explicación de una recomendación?

---

## Síntesis

La lógica difusa ofrece un lenguaje matemático para representar conceptos graduales y convertir reglas lingüísticas en inferencias computables. Sus componentes esenciales son universos de discurso, variables lingüísticas, funciones de pertenencia, operadores, reglas, agregación y mecanismos de salida.

Mamdani prioriza consecuentes lingüísticos; Sugeno favorece eficiencia y modelado funcional. Ninguno es superior en todos los casos: la elección depende de las necesidades de interpretación, control, aprendizaje, desempeño y gobernanza.

En software, el motor difuso debe estar rodeado por validación de datos, contratos explícitos, versionado, pruebas, trazabilidad y una capa de política. La puntuación resultante no es una probabilidad ni una autorización. Es una inferencia cuyo significado depende de las definiciones y reglas utilizadas.

El valor práctico de estos sistemas no proviene de imitar vagamente el pensamiento humano, sino de hacer explícitos criterios graduales que de otro modo quedarían dispersos en lenguaje informal, umbrales arbitrarios o código difícil de auditar.

---

## Referencias y lecturas recomendadas

- Zadeh, L. A. (1965). “Fuzzy Sets”. *Information and Control*, 8(3), 338–353. [DOI](https://doi.org/10.1016/S0019-9958(65)90241-X).
- Zadeh, L. A. (1973). “Outline of a New Approach to the Analysis of Complex Systems and Decision Processes”. *IEEE Transactions on Systems, Man, and Cybernetics*, SMC-3(1), 28–44. [DOI](https://doi.org/10.1109/TSMC.1973.5408575).
- Mamdani, E. H., & Assilian, S. (1975). “An Experiment in Linguistic Synthesis with a Fuzzy Logic Controller”. *International Journal of Man-Machine Studies*, 7(1), 1–13. [DOI](https://doi.org/10.1016/S0020-7373(75)80002-2).
- Takagi, T., & Sugeno, M. (1985). “Fuzzy Identification of Systems and Its Applications to Modeling and Control”. *IEEE Transactions on Systems, Man, and Cybernetics*, SMC-15(1), 116–132. [DOI](https://doi.org/10.1109/TSMC.1985.6313399).
- Jang, J.-S. R. (1993). “ANFIS: Adaptive-Network-Based Fuzzy Inference System”. *IEEE Transactions on Systems, Man, and Cybernetics*, 23(3), 665–685. [DOI](https://doi.org/10.1109/21.256541).
- Mendel, J. M. (2001). *Uncertain Rule-Based Fuzzy Logic Systems: Introduction and New Directions*. Prentice Hall.
- Ross, T. J. (2010). *Fuzzy Logic with Engineering Applications* (3.ª ed.). Wiley.
- IEC. *IEC 61131-7: Programmable Controllers — Fuzzy Control Programming*. Referencia para lenguajes de programación de control difuso.

> **Nota académica:** las reglas, fronteras y políticas del caso de la pista son deliberadamente didácticas. Una aplicación operacional requiere datos validados, criterios normativos, análisis de riesgos, pruebas independientes y autorización institucional.
