# Módulo 1.3 — Lógica difusa e inferencia en entornos de software

> **Inteligencia Artificial**  
> **Módulo 1 — Sistemas cognitivos y representación del conocimiento**  
> **Tema:** Lógica difusa e inferencia en entornos de software

## Propósito de estas notas

La lógica difusa se comprende mejor cuando se construye como respuesta a un problema y no como una colección de curvas. Esta versión sigue una ruta acumulativa:

1. identificar una decisión operativa;
2. separar la decisión de las observaciones que la sustentan;
3. modelar primero una frontera clásica;
4. estudiar qué ocurre cerca de esa frontera;
5. introducir transiciones graduales;
6. formar términos lingüísticos como bajo, medio y alto;
7. combinar términos mediante reglas;
8. obtener, explicar e implementar una recomendación;
9. validar que la solución se comporta como se espera.

El caso conductor será la evaluación de una pista después de una inspección. El objetivo no es formular un procedimiento aeronáutico real, sino mostrar de principio a fin por qué puede necesitarse lógica difusa y cómo se implementa en software.

---

## 1. Del problema operativo al problema de representación

### 1.1 La decisión original

La pregunta operativa puede expresarse así:

> **¿Existe evidencia suficiente para recomendar una nueva inspección antes de considerar la liberación de la pista?**

La salida administrativa final puede ser binaria:

```text
PISTA LIBERADA
PISTA NO LIBERADA
```

Pero que la decisión final sea binaria no significa que toda la evidencia que la precede también lo sea. Entre una pista evidentemente limpia y una pista evidentemente obstruida existe una región de observaciones ambiguas o graduales.

### 1.2 Liberar una pista no equivale a medir residuos

La **liberación** es una decisión gobernada por un procedimiento. Los **residuos** son sólo una clase posible de evidencia observable. Entre ambos conceptos hay varias capas:

```text
observaciones de inspección
        ↓
indicadores medibles
        ↓
evaluación de condición
        ↓
recomendación del sistema
        ↓
reglas operativas + autoridad competente
        ↓
decisión de liberar, restringir o inspeccionar
```

Por tanto, estas afirmaciones son distintas:

- “se observó un objeto de 4 cm”;
- “el nivel de residuos es moderado”;
- “la urgencia de reinspección es alta”;
- “la pista debe permanecer restringida”.

La lógica difusa puede ayudar en las dos evaluaciones intermedias. No sustituye las restricciones obligatorias ni la autoridad que toma la decisión.

### 1.3 ¿De dónde surge el problema de residuos?

Para construir un ejemplo controlado, se supone que una inspección registra tres características:

| Observación | Símbolo | Escala didáctica | Interpretación |
|---|---:|---:|---|
| cobertura superficial con material extraño | $c$ | $0$ a $100\%$ | extensión observada |
| tamaño máximo de los objetos detectados | $s$ | $0$ a $10$ cm | magnitud física |
| contraste o detectabilidad | $d$ | $0$ a $10$ | claridad de la observación |

Estas variables no son equivalentes. Antes de agregarlas deben normalizarse y justificarse. Para el ejercicio se define:

$$
c_n=\frac{c}{100},\qquad
s_n=\min\left(\frac{s}{10},1\right),\qquad
d_n=\frac{d}{10}
$$

Se construye un **índice didáctico de evidencia de residuos**:

$$
r=100\left(0.5c_n+0.3s_n+0.2d_n\right)
$$

donde $r\in[0,100]$.

Si una inspección reporta $c=40\%$, $s=6$ cm y $d=7$, entonces:

$$
r=100\left(0.5(0.4)+0.3(0.6)+0.2(0.7)\right)=52
$$

Ahora sí puede hablarse de $r=52$: no apareció de forma arbitraria, sino que se obtuvo de observaciones documentadas.

> **Advertencia:** esta fórmula es didáctica. Sus variables, pesos y escalas no representan una norma operacional. En una aplicación real deberían proceder de criterios técnicos, datos validados y análisis de riesgos.

### 1.4 ¿Por qué no aplicar directamente un umbral?

Una primera regla puede ser:

```text
SI r ≥ 50 ENTONCES solicitar reinspección.
```

Con ella:

- $r=49.9$ no solicita reinspección;
- $r=50.0$ sí solicita reinspección.

Aunque la diferencia entre ambas mediciones es mínima, la respuesta cambia por completo. Esto puede ser correcto cuando $50$ es un límite normativo obligatorio. Pero si $50$ sólo intenta representar el concepto vago “residuo considerable”, la frontera rígida puede exagerar diferencias pequeñas y ocultar incertidumbre de medición.

Aquí nace la necesidad que estudiaremos: representar una transición gradual sin renunciar a una decisión operativa clara al final del proceso.

---

## 2. Punto de partida: conjuntos clásicos y función de paso

### 2.1 Pertenencia clásica

Sea $X=[0,100]$ el universo del índice $r$. Definimos el conjunto clásico:

$$
A=\{r\in X\mid r\geq50\}
$$

Su función característica es:

$$
\chi_A(r)=
\begin{cases}
0, & r<50\\
1, & r\geq50
\end{cases}
$$

La función es un **paso discontinuo**. La pertenencia salta de 0 a 1 en $r=50$.

### 2.2 Cuándo es apropiado el paso

Una función de paso es apropiada cuando la frontera forma parte de la definición del problema:

- mayoría de edad establecida por ley;
- voltaje máximo permitido por una especificación;
- fecha de vencimiento de una certificación;
- restricción obligatoria ante la presencia de cierto objeto.

La lógica difusa no debe suavizar automáticamente una prohibición o una condición de seguridad. Primero debe distinguirse entre:

- **restricción dura:** no admite compensación;
- **criterio gradual:** admite grados y transición;
- **incertidumbre de medición:** exige modelar confiabilidad, no sólo gradualidad.

### 2.3 El problema en la frontera

Si “alto” es una categoría descriptiva y no un límite obligatorio, el paso presenta tres dificultades:

1. valores casi iguales reciben etiquetas opuestas;
2. el sistema no expresa casos intermedios;
3. una pequeña variación del sensor puede alternar la salida.

La siguiente transformación reemplaza el salto por una transición.

---

## 3. Del paso a la rampa

### 3.1 Una transición lineal

Supongamos que por debajo de 40 el residuo no se considera alto, y a partir de 60 se considera plenamente alto. Entre ambos valores se introduce una rampa:

$$
\mu_{alto}^{\text{rampa}}(r)=
\begin{cases}
0, & r\leq40\\
\dfrac{r-40}{20}, & 40<r<60\\
1, & r\geq60
\end{cases}
$$

Ejemplos:

| $r$ | $\mu_{alto}(r)$ | Lectura |
|---:|---:|---|
| 35 | 0.00 | no satisface “alto” |
| 45 | 0.25 | lo satisface débilmente |
| 50 | 0.50 | caso de transición |
| 55 | 0.75 | lo satisface considerablemente |
| 65 | 1.00 | satisface plenamente “alto” |

La pertenencia no indica una probabilidad. Para $r=50$:

$$
\mu_{alto}(50)=0.5
$$

significa que el valor 50 ocupa la mitad de la transición definida para el concepto “alto”. No significa que exista 50 % de probabilidad de encontrar residuos.

### 3.2 Forma general de una rampa ascendente

Para los puntos $a<b$:

$$
\operatorname{rampa\_asc}(x;a,b)=
\begin{cases}
0, & x\leq a\\
\dfrac{x-a}{b-a}, & a<x<b\\
1, & x\geq b
\end{cases}
$$

La rampa descendente es:

$$
\operatorname{rampa\_desc}(x;a,b)=
\begin{cases}
1, & x\leq a\\
\dfrac{b-x}{b-a}, & a<x<b\\
0, & x\geq b
\end{cases}
$$

### 3.3 Qué se ganó y qué no

La rampa ofrece continuidad y una explicación directa. Sin embargo:

- sigue teniendo cambios bruscos de pendiente en sus extremos;
- sólo describe un concepto creciente o decreciente;
- no representa por sí sola un término intermedio como “moderado”.

Para modelar términos intermedios es necesario unir varios segmentos.

---

## 4. De la rampa a triángulos y trapecios

### 4.1 Conceptos de borde y conceptos intermedios

En una escala ordenada suelen existir:

- un término de borde izquierdo: **bajo**;
- uno o más términos intermedios: **medio**;
- un término de borde derecho: **alto**.

`Bajo` puede modelarse con una rampa descendente y `alto` con una ascendente. Para `medio`, la pertenencia debe aumentar y después disminuir.

### 4.2 Función triangular

La unión de una rampa ascendente y una descendente produce un triángulo:

$$
\operatorname{tri}(x;a,b,c)=
\begin{cases}
0, & x\leq a\\
\dfrac{x-a}{b-a}, & a<x\leq b\\
\dfrac{c-x}{c-b}, & b<x<c\\
0, & x\geq c
\end{cases}
$$

donde:

- $a$ inicia el soporte;
- $b$ es el prototipo o valor con pertenencia máxima;
- $c$ termina el soporte.

Para el residuo medio puede definirse:

$$
\mu_{medio}(r)=\operatorname{tri}(r;25,50,75)
$$

Así, $r=50$ es plenamente medio, mientras que 25 y 75 ya no pertenecen al término.

### 4.3 Función trapezoidal

En ocasiones no existe un único prototipo. Un intervalo completo puede representar adecuadamente el concepto. Se introduce entonces una meseta:

$$
\operatorname{trap}(x;a,b,c,d)=
\begin{cases}
0, & x\leq a\\
\dfrac{x-a}{b-a}, & a<x<b\\
1, & b\leq x\leq c\\
\dfrac{d-x}{d-c}, & c<x<d\\
0, & x\geq d
\end{cases}
$$

Una definición posible de “residuo medio” sería:

$$
\mu_{medio}(r)=\operatorname{trap}(r;25,40,60,75)
$$

Los valores entre 40 y 60 son plenamente compatibles con el término medio.

### 4.4 Relación con máximo y mínimo

La función trapezoidal también puede verse como una composición limitada por mínimo y máximo:

$$
\operatorname{trap}(x;a,b,c,d)=
\max\left(
0,
\min\left(
\frac{x-a}{b-a},
1,
\frac{d-x}{d-c}
\right)
\right)
$$

Esta expresión compacta funciona cuando $a<b\leq c<d$. Para trapecios de hombro, donde $a=b$ o $c=d$, conviene usar una definición por tramos y evitar divisiones entre cero.

### 4.5 Una partición lingüística completa

Para $r\in[0,100]$ se propone:

$$
\mu_{bajo}(r)=
\begin{cases}
1, & r\leq20\\
\dfrac{40-r}{20}, & 20<r<40\\
0, & r\geq40
\end{cases}
$$

$$
\mu_{medio}(r)=\operatorname{tri}(r;25,50,75)
$$

$$
\mu_{alto}(r)=
\begin{cases}
0, & r\leq60\\
\dfrac{r-60}{20}, & 60<r<80\\
1, & r\geq80
\end{cases}
$$

Esta partición permite solapamiento, pero también revela una decisión de diseño: entre 40 y 60 sólo domina `medio`, y entre 60 y 75 se superponen `medio` y `alto`. El diseñador debe revisar si esa geometría corresponde con el dominio.

### 4.6 El solapamiento es una característica, no un error

Para $r=70$:

$$
\mu_{bajo}(70)=0
$$

$$
\mu_{medio}(70)=\frac{75-70}{75-50}=0.2
$$

$$
\mu_{alto}(70)=\frac{70-60}{80-60}=0.5
$$

El mismo valor puede ser parcialmente medio y parcialmente alto. Así se conserva la transición entre conceptos. Los grados no necesitan sumar uno, porque no son probabilidades de categorías mutuamente excluyentes.

---

## 5. De los segmentos lineales a curvas suaves

### 5.1 ¿Por qué suavizar?

Triángulos y trapecios son fáciles de explicar y calcular. Sin embargo, tienen esquinas donde cambia abruptamente la pendiente. En control, optimización o aprendizaje puede ser conveniente utilizar funciones diferenciables.

La suavización no hace automáticamente mejor al modelo. Cambia sus propiedades matemáticas y puede reducir su transparencia.

### 5.2 Función logística o sigmoide

Una transición creciente suave puede definirse como:

$$
\mu_{alto}^{\text{logística}}(r)=
\frac{1}{1+e^{-k(r-m)}}
$$

donde:

- $m$ es el punto central, para el cual $\mu(m)=0.5$;
- $k$ controla la pendiente;
- un $k$ grande aproxima un paso;
- un $k$ pequeño crea una transición más amplia.

Si $m=50$ y $k=0.2$:

$$
\mu_{alto}(50)=\frac{1}{1+e^0}=0.5
$$

La sigmoide es una versión suave de la rampa o del paso para conceptos monotónicos como alto, rápido o urgente.

### 5.3 Función gaussiana

Para un concepto intermedio y simétrico puede usarse:

$$
\mu_{medio}^{\text{gauss}}(r)=
\exp\left(-\frac{(r-c)^2}{2\sigma^2}\right)
$$

donde:

- $c$ es el centro;
- $\sigma$ controla la anchura.

Si $c=50$ y $\sigma=15$, la pertenencia máxima está en 50 y disminuye suavemente al alejarse.

### 5.4 Campana generalizada

Otra forma suave y ajustable es:

$$
\mu(x)=\frac{1}{1+\left|\dfrac{x-c}{a}\right|^{2b}}
$$

donde $c$ determina el centro, $a$ la anchura y $b$ la forma de la pendiente.

### 5.5 Marco para elegir una función

La elección no debe reducirse a enumerar formas. Debe responder a propiedades requeridas:

| Necesidad del concepto | Forma inicial razonable | Motivo |
|---|---|---|
| frontera obligatoria | paso | conserva una regla dura |
| transición monotónica interpretable | rampa | parámetros con significado directo |
| término con un prototipo | triángulo | centro y soporte visibles |
| término con intervalo prototípico | trapecio | meseta de pertenencia plena |
| transición monotónica suave | logística | continuidad y derivabilidad |
| término central suave | gaussiana | simetría y derivabilidad |
| forma flexible aprendida | campana u otra parametrización | ajuste con restricciones |

Antes de elegir deben formularse estas preguntas:

1. ¿El concepto es de borde o intermedio?
2. ¿Existe un punto prototípico o un intervalo prototípico?
3. ¿Se necesita derivabilidad?
4. ¿Los parámetros pueden explicarse a un especialista?
5. ¿Hay datos suficientes para ajustar la forma?
6. ¿Qué comportamiento se espera fuera de la zona observada?

---

## 6. Marco formal de conjuntos difusos

### 6.1 Conjunto difuso

Un conjunto difuso $A$ sobre un universo $X$ se caracteriza por:

$$
\mu_A:X\rightarrow[0,1]
$$

Cada $x\in X$ recibe un grado de compatibilidad con el concepto representado por $A$.

### 6.2 Soporte, núcleo y frontera

- **soporte:** valores con pertenencia positiva;

$$
\operatorname{supp}(A)=\{x\in X\mid\mu_A(x)>0\}
$$

- **núcleo:** valores con pertenencia completa;

$$
\operatorname{core}(A)=\{x\in X\mid\mu_A(x)=1\}
$$

- **frontera difusa:** valores con pertenencia estrictamente intermedia;

$$
\operatorname{bd}(A)=\{x\in X\mid0<\mu_A(x)<1\}
$$

### 6.3 Altura y normalidad

La altura de $A$ es:

$$
h(A)=\sup_{x\in X}\mu_A(x)
$$

El conjunto es **normal** si $h(A)=1$. No todos los conjuntos difusos tienen que ser normales, pero una partición lingüística suele diseñarse con términos normales para facilitar la interpretación.

### 6.4 Corte alfa

Para $\alpha\in(0,1]$:

$$
A_\alpha=\{x\in X\mid\mu_A(x)\geq\alpha\}
$$

En la rampa alta definida entre 40 y 60, el corte $\alpha=0.5$ contiene los valores $r\geq50$.

### 6.5 Complemento, intersección y unión

Operadores estándar:

$$
\mu_{\neg A}(x)=1-\mu_A(x)
$$

$$
\mu_{A\cap B}(x)=\min(\mu_A(x),\mu_B(x))
$$

$$
\mu_{A\cup B}(x)=\max(\mu_A(x),\mu_B(x))
$$

Mínimo y máximo no son las únicas opciones. Las generalizaciones son:

- **t-norma** $T(a,b)$ para conjunción;
- **s-norma** $S(a,b)$ para disyunción.

Ejemplos:

| Operación | Opción | Fórmula |
|---|---|---|
| conjunción | mínimo | $T(a,b)=\min(a,b)$ |
| conjunción | producto | $T(a,b)=ab$ |
| disyunción | máximo | $S(a,b)=\max(a,b)$ |
| disyunción | suma algebraica | $S(a,b)=a+b-ab$ |

La elección del operador afecta la inferencia y debe formar parte de la especificación del modelo.

### 6.6 Variable lingüística

Una variable lingüística puede describirse por la tupla:

$$
V=(N,T,X,G,M)
$$

donde:

- $N$ es el nombre de la variable;
- $T$ es el conjunto de términos lingüísticos;
- $X$ es el universo de discurso;
- $G$ contiene reglas para formar términos compuestos;
- $M$ asigna a cada término una función de pertenencia.

En el ejemplo:

```text
N = evidencia_de_residuos
T = {baja, media, alta}
X = [0, 100]
M = {μ_baja, μ_media, μ_alta}
```

---

## 7. De una variable difusa a un sistema de inferencia

### 7.1 Segunda entrada: antigüedad de la inspección

El residuo observado no es el único factor. Una inspección pierde vigencia con el tiempo porque las condiciones pueden cambiar. Se introduce:

$$
t=\text{minutos desde la última inspección válida},\qquad t\in[0,60]
$$

Se definen tres términos:

$$
\mu_{reciente}(t)=
\begin{cases}
1, & t\leq10\\
\dfrac{25-t}{15}, & 10<t<25\\
0, & t\geq25
\end{cases}
$$

$$
\mu_{intermedia}(t)=\operatorname{tri}(t;15,30,45)
$$

$$
\mu_{antigua}(t)=
\begin{cases}
0, & t\leq35\\
\dfrac{t-35}{15}, & 35<t<50\\
1, & t\geq50
\end{cases}
$$

### 7.2 Salida: prioridad de reinspección

Se define una salida numérica:

$$
u\in[0,100]
$$

donde $u$ representa **prioridad de reinspección**, no probabilidad de contaminación.

Para mantener el cálculo transparente se utiliza un sistema Sugeno de orden cero. Cada regla asigna una constante de salida.

### 7.3 Base de reglas razonada

| Regla | Antecedente | Consecuente | Justificación didáctica |
|---|---|---:|---|
| R1 | residuo alto | $u=90$ | evidencia material alta exige atención |
| R2 | inspección antigua | $u=80$ | una observación antigua pierde vigencia |
| R3 | residuo medio Y inspección intermedia | $u=60$ | combinación que amerita revisión |
| R4 | residuo bajo Y inspección reciente | $u=15$ | condición compatible con baja prioridad |
| R5 | residuo bajo Y inspección antigua | $u=65$ | poco residuo no compensa evidencia obsoleta |
| R6 | residuo medio Y inspección reciente | $u=45$ | evidencia media con observación vigente |

Las reglas muestran dos ideas:

1. varias condiciones pueden apoyar simultáneamente la salida;
2. una entrada favorable no debe cancelar automáticamente otra desfavorable.

En una aplicación real también existirían restricciones duras previas, por ejemplo: “si se confirma un objeto prohibido, mantener restricción”, sin importar la puntuación difusa.

### 7.4 Fuzzificación de un caso completo

Retomemos la observación:

```text
cobertura c = 40 %
tamaño s = 6 cm
detectabilidad d = 7/10
antigüedad t = 40 minutos
```

Ya se calculó:

$$
r=52
$$

Con las funciones de residuo:

$$
\mu_{bajo}(52)=0
$$

$$
\mu_{medio}(52)=\frac{75-52}{75-50}=0.92
$$

$$
\mu_{alto}(52)=0
$$

Para $t=40$:

$$
\mu_{reciente}(40)=0
$$

$$
\mu_{intermedia}(40)=\frac{45-40}{45-30}=\frac{1}{3}
$$

$$
\mu_{antigua}(40)=\frac{40-35}{50-35}=\frac{1}{3}
$$

### 7.5 Activación de reglas

Se utiliza mínimo para `Y`:

$$
\alpha_1=\mu_{alto}(52)=0
$$

$$
\alpha_2=\mu_{antigua}(40)=\frac{1}{3}
$$

$$
\alpha_3=\min\left(0.92,\frac{1}{3}\right)=\frac{1}{3}
$$

$$
\alpha_4=\min(0,0)=0
$$

$$
\alpha_5=\min\left(0,\frac{1}{3}\right)=0
$$

$$
\alpha_6=\min(0.92,0)=0
$$

### 7.6 Combinación de salidas

La salida Sugeno es:

$$
u=\frac{\sum_i\alpha_i z_i}{\sum_i\alpha_i}
$$

Para las reglas activas:

$$
u=
\frac{\frac{1}{3}(80)+\frac{1}{3}(60)}
{\frac{1}{3}+\frac{1}{3}}
=70
$$

El sistema produce prioridad 70. Una capa de política didáctica puede interpretar:

| Puntuación | Recomendación |
|---:|---|
| $0\leq u<35$ | mantener monitoreo |
| $35\leq u<65$ | revisión documental o visual |
| $65\leq u\leq100$ | solicitar reinspección y escalar |

La salida es:

```text
Prioridad de reinspección: 70/100
Recomendación: solicitar reinspección y escalar
Reglas dominantes: R2 y R3
```

Todavía no se ha liberado ni bloqueado la pista. El sistema generó una recomendación explicable para alimentar el procedimiento.

---

## 8. Implementación práctica desde cero

### 8.1 Separación de componentes

Una implementación mantenible separa:

```text
observaciones → construcción del índice → fuzzificación
             → reglas → combinación → política → respuesta explicada
```

Esto permite cambiar una función de pertenencia sin modificar la captura de datos, o cambiar una política sin reinterpretar los conjuntos difusos.

### 8.2 Implementación en Python sin biblioteca externa

```python
from math import isfinite


def clamp(value, lower=0.0, upper=1.0):
    return max(lower, min(value, upper))


def triangle(x, a, b, c):
    if not a < b < c:
        raise ValueError("Se requiere a < b < c")
    if x <= a or x >= c:
        return 0.0
    if x <= b:
        return (x - a) / (b - a)
    return (c - x) / (c - b)


def residue_low(r):
    if r <= 20:
        return 1.0
    if r < 40:
        return (40 - r) / 20
    return 0.0


def residue_high(r):
    if r <= 60:
        return 0.0
    if r < 80:
        return (r - 60) / 20
    return 1.0


def inspection_recent(t):
    if t <= 10:
        return 1.0
    if t < 25:
        return (25 - t) / 15
    return 0.0


def inspection_old(t):
    if t <= 35:
        return 0.0
    if t < 50:
        return (t - 35) / 15
    return 1.0


def build_residue_index(coverage_pct, size_cm, detectability):
    values = (coverage_pct, size_cm, detectability)
    if not all(isfinite(value) for value in values):
        raise ValueError("Las observaciones deben ser finitas")
    if not 0 <= coverage_pct <= 100:
        raise ValueError("coverage_pct fuera de [0, 100]")
    if not 0 <= size_cm <= 10:
        raise ValueError("size_cm fuera de [0, 10]")
    if not 0 <= detectability <= 10:
        raise ValueError("detectability fuera de [0, 10]")

    coverage = coverage_pct / 100
    size = size_cm / 10
    clarity = detectability / 10
    return 100 * (0.5 * coverage + 0.3 * size + 0.2 * clarity)


def infer_reinspection_priority(residue_index, inspection_age_min):
    if not 0 <= residue_index <= 100:
        raise ValueError("residue_index fuera de [0, 100]")
    if not 0 <= inspection_age_min <= 60:
        raise ValueError("inspection_age_min fuera de [0, 60]")

    membership = {
        "residue_low": residue_low(residue_index),
        "residue_medium": triangle(residue_index, 25, 50, 75),
        "residue_high": residue_high(residue_index),
        "inspection_recent": inspection_recent(inspection_age_min),
        "inspection_intermediate": triangle(
            inspection_age_min, 15, 30, 45
        ),
        "inspection_old": inspection_old(inspection_age_min),
    }

    rules = {
        "R1": {"strength": membership["residue_high"], "output": 90},
        "R2": {"strength": membership["inspection_old"], "output": 80},
        "R3": {
            "strength": min(
                membership["residue_medium"],
                membership["inspection_intermediate"],
            ),
            "output": 60,
        },
        "R4": {
            "strength": min(
                membership["residue_low"],
                membership["inspection_recent"],
            ),
            "output": 15,
        },
        "R5": {
            "strength": min(
                membership["residue_low"],
                membership["inspection_old"],
            ),
            "output": 65,
        },
        "R6": {
            "strength": min(
                membership["residue_medium"],
                membership["inspection_recent"],
            ),
            "output": 45,
        },
    }

    total_strength = sum(rule["strength"] for rule in rules.values())
    if total_strength == 0:
        return {
            "status": "no_rule_coverage",
            "membership": membership,
            "rules": rules,
        }

    priority = sum(
        rule["strength"] * rule["output"]
        for rule in rules.values()
    ) / total_strength

    if priority < 35:
        recommendation = "monitor"
    elif priority < 65:
        recommendation = "review"
    else:
        recommendation = "reinspect_and_escalate"

    return {
        "status": "ok",
        "priority": priority,
        "recommendation": recommendation,
        "membership": membership,
        "rules": rules,
    }


def evaluate_inspection(coverage_pct, size_cm, detectability, age_min):
    residue_index = build_residue_index(
        coverage_pct, size_cm, detectability
    )
    result = infer_reinspection_priority(residue_index, age_min)
    result["residue_index"] = residue_index
    result["inputs"] = {
        "coverage_pct": coverage_pct,
        "size_cm": size_cm,
        "detectability": detectability,
        "inspection_age_min": age_min,
    }
    result["model_version"] = "runway-teaching-fis-2.0"
    return result


case = evaluate_inspection(
    coverage_pct=40,
    size_cm=6,
    detectability=7,
    age_min=40,
)
```

### 8.3 Resultado esperado

El resultado aproximado conserva cada etapa:

```json
{
  "status": "ok",
  "residue_index": 52.0,
  "priority": 70.0,
  "recommendation": "reinspect_and_escalate",
  "membership": {
    "residue_low": 0.0,
    "residue_medium": 0.92,
    "residue_high": 0.0,
    "inspection_recent": 0.0,
    "inspection_intermediate": 0.333,
    "inspection_old": 0.333
  },
  "model_version": "runway-teaching-fis-2.0"
}
```

La implementación demuestra la aplicación práctica porque permite reconstruir:

1. las observaciones originales;
2. el índice derivado;
3. cada grado de pertenencia;
4. la fuerza de cada regla;
5. la combinación numérica;
6. la política que produjo la recomendación;
7. la versión del modelo.

### 8.4 Dónde colocar restricciones duras

Las restricciones no negociables deben evaluarse fuera o antes del promedio difuso:

```python
if confirmed_prohibited_object:
    return {
        "status": "hard_constraint",
        "recommendation": "keep_restricted",
        "reason": "confirmed_prohibited_object",
    }
```

Así se evita que una condición favorable compense matemáticamente una prohibición.

---

## 9. Cómo validar el modelo

### 9.1 Validar la transformación inicial

Antes de validar las reglas difusas debe preguntarse:

- ¿las tres observaciones son realmente relevantes?;
- ¿sus escalas y unidades están documentadas?;
- ¿los pesos 0.5, 0.3 y 0.2 tienen fundamento?;
- ¿puede una variable compensar indebidamente a otra?;
- ¿conviene mantener las variables separadas en lugar de construir $r$?

Este último punto es importante: el índice simplifica el ejemplo, pero también pierde información. En un sistema real puede ser preferible usar cobertura, tamaño y detectabilidad como entradas difusas independientes.

### 9.2 Probar las funciones de pertenencia

Casos mínimos:

```text
μ_bajo(20) = 1
μ_bajo(30) = 0.5
μ_bajo(40) = 0

μ_medio(25) = 0
μ_medio(50) = 1
μ_medio(75) = 0

μ_alto(60) = 0
μ_alto(70) = 0.5
μ_alto(80) = 1
```

Además debe verificarse:

$$
0\leq\mu_A(x)\leq1
$$

para todo valor válido.

### 9.3 Probar continuidad y fronteras

Comparar valores inmediatamente antes y después de cada punto:

```text
39.999, 40.000, 40.001
59.999, 60.000, 60.001
```

La función puede cambiar de pendiente, pero no debería presentar saltos no intencionales.

### 9.4 Probar cobertura de reglas

Se recorre una malla de valores de $r$ y $t$. Para cada combinación:

$$
\sum_i\alpha_i>0
$$

Si la suma es cero, el sistema no tiene una regla aplicable. Debe añadirse conocimiento o definirse una respuesta segura `no_rule_coverage`.

### 9.5 Probar propiedades del dominio

Si el dominio establece que más residuo nunca debe disminuir la prioridad:

$$
r_1\leq r_2\Rightarrow u(r_1,t)\leq u(r_2,t)
$$

Si una inspección más antigua nunca debe disminuirla:

$$
t_1\leq t_2\Rightarrow u(r,t_1)\leq u(r,t_2)
$$

Estas propiedades deben probarse sobre toda la superficie, no sólo en ejemplos elegidos.

### 9.6 Comparar contra el modelo clásico

La solución difusa debe compararse con el umbral original:

| Criterio | Umbral clásico | Sistema difuso |
|---|---|---|
| interpretación | muy directa | requiere funciones y reglas |
| transición | abrupta | gradual |
| número de parámetros | bajo | mayor |
| explicación cerca de la frontera | limitada | detallada |
| mantenimiento | sencillo | exige gobierno de reglas |
| comportamiento con varias entradas | reglas adicionales | combinación gradual |

La lógica difusa se justifica sólo si la gradualidad y la combinación de criterios aportan valor suficiente para asumir esa complejidad.

---

## 10. Mamdani y Sugeno dentro del marco

### 10.1 Mamdani

Mamdani usa un conjunto difuso como consecuente:

```text
SI residuo ES alto
ENTONCES prioridad ES muy_alta
```

Cada regla genera una región difusa de salida; las regiones se agregan y después se desfuzzifican. El centroide se calcula como:

$$
u^*=\frac{\int u\,\mu_{salida}(u)\,du}
{\int\mu_{salida}(u)\,du}
$$

Su principal ventaja es que antecedente y consecuente conservan términos lingüísticos.

### 10.2 Sugeno

Sugeno utiliza una constante o función en el consecuente:

```text
SI residuo ES alto
ENTONCES prioridad = 90
```

Su salida es:

$$
u^*=\frac{\sum_i\alpha_i f_i(x)}{\sum_i\alpha_i}
$$

En estas notas se eligió Sugeno de orden cero porque permite calcular e implementar el caso completo sin introducir todavía discretización del universo de salida.

### 10.3 La elección depende del propósito

| Necesidad | Mamdani | Sugeno |
|---|---:|---:|
| consecuentes lingüísticos | fuerte | limitado |
| cálculo eficiente | medio | fuerte |
| integración con optimización | media | fuerte |
| explicación verbal completa | fuerte | media |
| aproximación de funciones | media | fuerte |

Los modelos no son familias de curvas de pertenencia. Son arquitecturas de inferencia que determinan qué produce cada regla y cómo se combinan sus resultados.

---

## 11. Cinco preguntas para profundizar

### 1. ¿Una transición suave siempre es preferible a un umbral?

No. El umbral es correcto cuando representa una definición o restricción dura. La transición difusa es útil cuando la frontera intenta representar un concepto gradual. El primer trabajo consiste en distinguir ambos casos.

### 2. ¿Cómo se determinan los puntos de una rampa o un trapecio?

Pueden derivarse de conocimiento experto, normas, ejercicios de clasificación, datos históricos o una combinación. Después deben someterse a análisis de sensibilidad: cuánto cambia la salida cuando se mueve cada punto.

### 3. ¿Por qué no usar siempre gaussianas?

Porque suavidad matemática no equivale a validez semántica. Una gaussiana tiene soporte teórico en todo el eje y parámetros menos directos para algunos usuarios. Triángulos y trapecios suelen ser más fáciles de auditar.

### 4. ¿Conviene construir un índice de residuos?

Sólo si la agregación tiene fundamento y la pérdida de información es aceptable. El índice facilita enseñanza y operación, pero puede ocultar que dos combinaciones muy distintas producen el mismo valor. Otra solución es conservar cada observación como variable de entrada.

### 5. ¿Cómo saber si el sistema difuso aporta valor?

Debe compararse contra alternativas simples mediante casos reales: umbrales, tablas de decisión, modelos probabilísticos o reglas clásicas. Se evalúan coherencia, estabilidad, tasa de errores, esfuerzo de mantenimiento, explicación y utilidad operacional.

---

## 12. Tres estudios breves de aplicación

### 12.1 Control de temperatura

Un termostato clásico enciende al cruzar un umbral y puede alternar repetidamente cerca de él. Un controlador difuso combina `temperatura baja`, `error` y `cambio del error` para graduar la potencia. El beneficio no es etiquetar la temperatura, sino producir una acción suave.

### 12.2 Priorización de mantenimiento

La urgencia de mantenimiento puede depender de vibración, temperatura, antigüedad y criticidad. Las reglas difusas expresan criterios como:

```text
SI vibración ES alta Y criticidad ES alta
ENTONCES prioridad ES muy_alta
```

Las restricciones obligatorias siguen siendo reglas duras independientes.

### 12.3 Reinspección de pista

El caso desarrollado ilustra una cadena completa:

```text
cobertura + tamaño + detectabilidad
                ↓
índice didáctico de evidencia
                ↓
pertenencias baja, media y alta
                +
vigencia de inspección
                ↓
reglas Sugeno
                ↓
prioridad explicada
                ↓
política y autoridad operacional
```

El aprendizaje central es la separación entre observación, representación, inferencia, recomendación y decisión.

---

## 13. Línea de tiempo conceptual

| Año | Hito | Aporte a la ruta de aprendizaje |
|---:|---|---|
| 1920–1930 | lógicas multivaluadas | muestran que pueden existir valores distintos de verdadero y falso |
| 1965 | Zadeh formaliza conjuntos difusos | introduce grados de pertenencia sobre un universo |
| 1973 | variables lingüísticas | relacionan términos humanos con conjuntos difusos |
| 1975 | Mamdani y Assilian | convierten reglas lingüísticas en control práctico |
| 1985 | Takagi y Sugeno | combinan regiones difusas con modelos funcionales |
| 1993 | ANFIS | permite ajustar parámetros mediante aprendizaje adaptativo |
| actualidad | sistemas híbridos y explicables | integran reglas, datos, restricciones y trazabilidad |

---

## 14. Actividad integradora

### Parte A. Construir la necesidad

Elegir una variable con un umbral y responder:

1. ¿el umbral es obligatorio o descriptivo?;
2. ¿qué ocurre inmediatamente antes y después?;
3. ¿existe error de medición?;
4. ¿una transición gradual tendría significado?

### Parte B. Construir las funciones

Representar el mismo término con:

1. paso;
2. rampa;
3. sigmoide.

Después representar un término intermedio con:

1. triángulo;
2. trapecio;
3. gaussiana.

Comparar parámetros, continuidad e interpretación.

### Parte C. Construir la inferencia

1. definir dos entradas y una salida;
2. crear entre cuatro y seis reglas;
3. calcular manualmente un caso;
4. implementar las funciones;
5. devolver una traza;
6. localizar un caso sin cobertura;
7. probar una propiedad monotónica.

### Parte D. Cuestionar el modelo

Explicar qué decisiones del diseño son:

- conocimiento del dominio;
- simplificaciones didácticas;
- parámetros aprendibles;
- restricciones duras;
- políticas modificables;
- responsabilidades humanas.

---

## 15. Síntesis de la ruta

La lógica difusa no comienza con un valor arbitrario como $x=70$. Comienza cuando un problema contiene un concepto gradual cuya frontera clásica resulta insuficiente.

La construcción progresiva es:

$$
\text{paso}
\rightarrow
\text{rampa}
\rightarrow
\text{triángulo o trapecio}
\rightarrow
\text{curva suave si se necesita}
$$

Cada transformación responde a una necesidad:

- el paso representa pertenencia binaria;
- la rampa representa transición monotónica;
- el triángulo representa un prototipo intermedio;
- el trapecio representa un intervalo prototípico;
- la logística y la gaussiana aportan suavidad y derivabilidad.

Después, las variables lingüísticas se conectan mediante reglas. Mamdani conserva consecuentes difusos; Sugeno produce constantes o funciones combinadas por peso. En ambos casos, la salida necesita validación, trazabilidad y una capa de política.

En el caso de la pista, los residuos no son sinónimo de liberación. Son evidencia construida a partir de observaciones. El sistema difuso transforma esa evidencia y la vigencia de la inspección en una prioridad de reinspección. La decisión final permanece separada y sujeta al procedimiento correspondiente.

---

## Referencias y lecturas recomendadas

- Zadeh, L. A. (1965). “Fuzzy Sets”. *Information and Control*, 8(3), 338–353. [DOI](https://doi.org/10.1016/S0019-9958(65)90241-X).
- Zadeh, L. A. (1973). “Outline of a New Approach to the Analysis of Complex Systems and Decision Processes”. *IEEE Transactions on Systems, Man, and Cybernetics*, SMC-3(1), 28–44. [DOI](https://doi.org/10.1109/TSMC.1973.5408575).
- Mamdani, E. H., & Assilian, S. (1975). “An Experiment in Linguistic Synthesis with a Fuzzy Logic Controller”. *International Journal of Man-Machine Studies*, 7(1), 1–13. [DOI](https://doi.org/10.1016/S0020-7373(75)80002-2).
- Takagi, T., & Sugeno, M. (1985). “Fuzzy Identification of Systems and Its Applications to Modeling and Control”. *IEEE Transactions on Systems, Man, and Cybernetics*, SMC-15(1), 116–132. [DOI](https://doi.org/10.1109/TSMC.1985.6313399).
- Jang, J.-S. R. (1993). “ANFIS: Adaptive-Network-Based Fuzzy Inference System”. *IEEE Transactions on Systems, Man, and Cybernetics*, 23(3), 665–685. [DOI](https://doi.org/10.1109/21.256541).
- Ross, T. J. (2010). *Fuzzy Logic with Engineering Applications* (3.ª ed.). Wiley.

> **Nota académica:** las variables, pesos, límites y reglas del caso de la pista son deliberadamente didácticos. No deben interpretarse como criterios aeronáuticos ni utilizarse para tomar decisiones operacionales.
