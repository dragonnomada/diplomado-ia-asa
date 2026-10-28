# Módulo 1.3 — Lógica difusa e inferencia en entornos de software

> **Inteligencia Artificial**  
> **Módulo 1 — Sistemas cognitivos y representación del conocimiento**  
> **Tema:** Lógica difusa e inferencia en entornos de software

## Introducción

Un sistema de ventilación puede trabajar con tres velocidades: baja, media y alta. La primera solución suele consistir en establecer límites de temperatura y escribir reglas:

- SI la temperatura es menor que 25 °C, ENTONCES velocidad baja.
- SI la temperatura está entre 25 °C y menos de 30 °C, ENTONCES velocidad media.
- SI la temperatura es igual o superior a 30 °C, ENTONCES velocidad alta.

Estas reglas son sencillas de interpretar y verificar. También introducen fronteras: a 29.9 °C el ventilador funciona a velocidad media y a 30 °C cambia a alta. Una diferencia pequeña de temperatura puede provocar un cambio grande de velocidad. Si la medición fluctúa alrededor del límite, la orden podría alternar continuamente.

El primer problema es de **clasificación**: determinar a qué conjunto pertenece una medición. El segundo es de **control**: decidir cómo responder. La **lógica difusa** permite representar conceptos con fronteras graduales, como *temperatura moderada* o *temperatura alta*, y activar varias reglas simultáneamente en diferentes grados. La **inferencia difusa** combina esos grados para construir una salida.

En esta transición se conservan distinciones esenciales: **temperatura** es una medición; **caliente** es un concepto; **pertenencia** es el grado en que una temperatura satisface ese concepto; **activación** es el grado en que se cumple el antecedente de una regla; **salida** es la recomendación del controlador. Ninguna de estas magnitudes equivale automáticamente a probabilidad.

Un controlador real también necesita considerar cuándo se obtuvo la medición. Una temperatura registrada hace veinte minutos puede ser válida como registro histórico, pero no necesariamente como estado actual. Introducir **tiempo, vigencia y retroalimentación** permite conectar el modelo difuso con sistemas cognitivos, representación del conocimiento y toma de decisiones.

La pregunta central es:

> **¿Cómo transformar categorías rígidas y reglas expresadas en lenguaje humano en un controlador gradual, explicable y verificable, sin confundir una recomendación con una garantía de seguridad?**

Al finalizar el tema se podrá distinguir pertenencia de probabilidad, construir y comparar funciones de pertenencia, evaluar reglas difusas, obtener salidas con sistemas Mamdani y Sugeno, reconocer el mecanismo de Tsukamoto y examinar cómo la vigencia de la evidencia afecta una decisión.

---

## 1. Del control clásico al problema de las fronteras

### 1.1 Variables, universos y decisiones

Se considera una habitación con un ventilador regulable.

| Elemento | Símbolo | Valores | Interpretación |
|---|---|---|---|
| Temperatura registrada | $T$ | $20$ a $35$ °C | variable de entrada |
| Velocidad solicitada | $v$ | $0$ a $100$ % | variable de salida |
| Momento de la medición | $t_m$ | instante | procedencia temporal |
| Momento de decisión | $t$ | instante | momento de actuación |

En esta primera aproximación se supone que el sensor es confiable y la temperatura se mantiene dentro del intervalo de trabajo. Los intervalos y velocidades son parámetros de un modelo de referencia; su uso en un equipo físico exigiría especificaciones, protección eléctrica y calibración.

Se define una política rígida:

$$
v_{\mathrm{cl}}(T)=
\begin{cases}
20,&T<25,\\
50,&25\le T<30,\\
90,&T\ge30.
\end{cases}
$$

Por ejemplo, $v_{\mathrm{cl}}(29.9)=50$ y $v_{\mathrm{cl}}(30)=90$. El salto es de 40 puntos porcentuales, aunque la temperatura sólo cambió 0.1 °C.

### 1.2 Conjuntos clásicos y función característica

Sea $X=[20,35]$ el universo de temperaturas. El conjunto clásico de temperaturas altas es

$$
A=\{T\in X:T\ge30\}.
$$

Su función característica indica pertenencia completa o ausencia de pertenencia:

$$
\chi_A(T)=
\begin{cases}
0,&T<30,\\
1,&T\ge30.
\end{cases}
$$

La discontinuidad no es siempre defectuosa: una **restricción obligatoria** debe preservar su frontera. El problema aparece cuando una frontera numérica intenta aproximar un **concepto gradual**, como *caliente*, y ese salto genera respuestas operativas innecesariamente bruscas.

### 1.3 Tres problemas que no deben confundirse

1. **Gradualidad:** ¿en qué grado una temperatura puede considerarse alta?
2. **Incertidumbre:** ¿cuán confiable es la medición o qué probabilidad tiene un evento?
3. **Decisión:** ¿qué velocidad conviene solicitar dadas las metas, costos y restricciones?

La pertenencia difusa responde fundamentalmente a la primera pregunta. Las otras dos requieren mecanismos complementarios.

**Actividad de cálculo.** Comparar la velocidad clásica en 24.9, 25, 29.9 y 30 °C. Identificar discontinuidades y discutir si son restricciones necesarias o simples decisiones de clasificación.

---

## 2. Construcción gradual de conjuntos difusos

### 2.1 Del paso a una rampa

Un conjunto difuso $A$ sobre $X$ se define por una función de pertenencia

$$
\mu_A:X\longrightarrow[0,1].
$$

La rampa ascendente con extremos $a<b$ se expresa como

$$
R_{\uparrow}(x;a,b)=
\begin{cases}
0,&x\le a,\\
\dfrac{x-a}{b-a},&a<x<b,\\
1,&x\ge b.
\end{cases}
$$

La rampa descendente es $R_{\downarrow}(x;a,b)=1-R_{\uparrow}(x;a,b)$.

En el controlador se propone:

$$
\mu_{\mathrm{alta}}(T)=R_{\uparrow}(T;25,30).
$$

Así, $\mu_{\mathrm{alta}}(27)=0.4$. Significa que 27 °C satisface en grado 0.4 **esta definición del concepto** *temperatura alta*. No significa que exista 40 % de probabilidad de calor, ni de falla.

Una rampa es continua, aunque no es derivable en sus puntos de unión con los segmentos horizontales. El paso y la rampa representan criterios distintos; no hay obligación matemática de suavizar una condición normativa.

### 2.2 Dos rampas y un concepto intermedio: el triángulo

Un concepto como *moderada* puede aumentar hacia un valor prototípico y disminuir al alejarse de él:

$$
\operatorname{tri}(x;a,b,c)=
\begin{cases}
0,&x\le a,\\
\dfrac{x-a}{b-a},&a<x\le b,\\
\dfrac{c-x}{c-b},&b<x<c,\\
0,&x\ge c,
\end{cases}
\quad a<b<c.
$$

Por ejemplo:

$$
\mu_{\mathrm{moderada}}(T)=\operatorname{tri}(T;20,25,30).
$$

A 27 °C: $\mu_{\mathrm{moderada}}(27)=0.6$ y $\mu_{\mathrm{alta}}(27)=0.4$. **Un dato puede satisfacer simultáneamente varios términos.** La suma de las pertenencias no necesita ser uno, aunque algunas particiones se construyen deliberadamente para cumplirlo.

### 2.3 La meseta y el trapecio

Si todos los valores de un intervalo son prototípicos, se usa una función trapezoidal:

$$
\operatorname{trap}(x;a,b,c,d)=
\begin{cases}
0,&x\le a,\\
\dfrac{x-a}{b-a},&a<x<b,\\
1,&b\le x\le c,\\
\dfrac{d-x}{d-c},&c<x<d,\\
0,&x\ge d,
\end{cases}
\quad a<b\le c<d.
$$

Una forma equivalente, para parámetros no degenerados, es

$$
\operatorname{trap}(x;a,b,c,d)=
\max\left(0,\min\left(1,\frac{x-a}{b-a},\frac{d-x}{d-c}\right)\right).
$$

Este `min` y `max` describe la **geometría de una función**; más adelante esas operaciones también servirán para interpretar condiciones lógicas, pero son usos conceptualmente distintos.

### 2.4 De segmentos a curvas suaves

La **función logística** puede reemplazar una transición monotónica por una curva derivable:

$$
\mu_{\mathrm{alta}}^{\mathrm{log}}(T)
=\frac{1}{1+e^{-k(T-m)}},
\qquad k>0.
$$

En $T=m$, la pertenencia es 0.5. El parámetro $k$ controla la pendiente. La logística es una alternativa suave a una rampa, pero no tiene necesariamente tramos exactamente iguales a cero o uno.

Para conceptos centrados puede emplearse una **gaussiana**:

$$
\mu_{\mathrm{moderada}}^{\mathrm{gauss}}(T)
=\exp\left[-\frac{(T-c)^2}{2\sigma^2}\right].
$$

Su valor máximo es uno en $T=c$; $\sigma>0$ determina su anchura. No representa una distribución de probabilidad por el mero hecho de tener forma gaussiana: aquí su máximo se normaliza a uno como función de pertenencia, no su integral.

También se utiliza la campana generalizada:

$$
\mu(x)=\frac{1}{1+\left|\frac{x-c}{a}\right|^{2b}},
\quad a\ne0,\ b>0.
$$

**Marco de selección:** las rampas expresan transiciones monotónicas con extremos explícitos; los triángulos tienen un prototipo puntual; los trapecios tienen un intervalo central; la logística y la gaussiana aportan suavidad, aunque pueden complicar la interpretación de fronteras. La forma debe responder a un significado verificable, no sólo a una preferencia estética.

### 2.5 Soporte, núcleo, frontera y corte alfa

Para un conjunto difuso $A$:

$$
\operatorname{supp}(A)=\{x:\mu_A(x)>0\},
\quad
\operatorname{core}(A)=\{x:\mu_A(x)=1\},
$$

$$
\operatorname{bd}(A)=\{x:0<\mu_A(x)<1\},
\quad
A_{\alpha}=\{x:\mu_A(x)\ge\alpha\}.
$$

El **soporte** contiene los valores con pertenencia positiva; el **núcleo**, los plenamente compatibles; la **frontera difusa**, los intermedios; el **corte alfa** recupera un conjunto clásico a un nivel de pertenencia determinado.

**Actividad de pizarrón y Excel.** Para $T=24,25,26,27,28,29,30$, calcular $\mu_{\mathrm{moderada}}$ y $\mu_{\mathrm{alta}}$. Repetir con una sigmoide usando $m=27.5$ y $k=1$. Comparar interpretación, facilidad de cálculo y continuidad.

---

## 3. Del vocabulario a las reglas

### 3.1 Variable lingüística

Una variable lingüística reúne el nombre, el universo y términos que se interpretan mediante funciones. Para la temperatura:

$$
V_T=(\text{temperatura},X,\{\text{baja, moderada, alta}\},M).
$$

Aquí $M$ vincula cada término con su función de pertenencia. Para completar una partición sencilla y continua sobre el intervalo de trabajo se adopta:

$$
\mu_{\mathrm{baja}}(T)=R_{\downarrow}(T;20,25),\quad
\mu_{\mathrm{moderada}}(T)=\operatorname{tri}(T;20,25,30),\quad
\mu_{\mathrm{alta}}(T)=R_{\uparrow}(T;25,30).
$$

En el intervalo [20,30], esta elección da $\mu_{\mathrm{baja}}+\mu_{\mathrm{moderada}}+\mu_{\mathrm{alta}}=1$, y para $T\ge30$, la pertenencia alta es uno. **Es una propiedad de esta elección, no un requisito universal de los conjuntos difusos.**

### 3.2 Operaciones lógicas con grados

Los operadores estándar de Zadeh se expresan como:

$$
\neg a=1-a,\qquad a\land b=\min(a,b),
\qquad a\lor b=\max(a,b).
$$

La conjunción se puede generalizar mediante una **t-norma**, como $T(a,b)=ab$; la disyunción mediante una **s-norma**, como $S(a,b)=a+b-ab$. Cambiar operadores cambia los resultados, por lo que deben especificarse y validarse.

Una regla:

> SI la temperatura es alta Y la ocupación es alta, ENTONCES la ventilación debe ser alta.

con grados 0.4 y 0.7 tendrá fuerza $\alpha=\min(0.4,0.7)=0.4$ bajo conjunción mínimo. No significa que haya 40 % de probabilidad de que la regla sea verdadera.

### 3.3 De reglas excluyentes a reglas simultáneas

En el controlador clásico sólo una condición de temperatura determina la salida. En un controlador difuso pueden activarse varias reglas:

| Regla | Antecedente | Consecuente numérico |
|---|---|---:|
| R1 | temperatura baja | $v=20$ % |
| R2 | temperatura moderada | $v=50$ % |
| R3 | temperatura alta | $v=90$ % |

Los consecuentes son **constantes de salida**: esta elección corresponde a un sistema **Sugeno de orden cero**.

Para $T=27$:

$$
(\alpha_1,\alpha_2,\alpha_3)=(0,0.6,0.4).
$$

La velocidad se obtiene mediante el promedio de las salidas ponderadas por activación:

$$
v^*=\frac{\sum_i \alpha_i z_i}{\sum_i\alpha_i}
=\frac{0(20)+0.6(50)+0.4(90)}{0+0.6+0.4}
=\boxed{66\%}.
$$

Aquí el mecanismo difuso **interpola respuestas de reglas**. Para esta partición particular se obtiene $v=50+8(T-25)$ entre 25 y 30 °C. La interpolación clásica podría producir el mismo resultado; el interés de las reglas difusas consiste en conservar una estructura interpretable que puede ampliarse a múltiples condiciones.

### 3.4 Comparación con las reglas rígidas

| $T$ | $v_{\mathrm{cl}}$ | $\mu_{\mathrm{mod}}$ | $\mu_{\mathrm{alta}}$ | $v_{\mathrm{difuso}}$ |
|---:|---:|---:|---:|---:|
| 25 | 50 | 1 | 0 | 50 |
| 26 | 50 | 0.8 | 0.2 | 58 |
| 27 | 50 | 0.6 | 0.4 | 66 |
| 28 | 50 | 0.4 | 0.6 | 74 |
| 29 | 50 | 0.2 | 0.8 | 82 |
| 30 | 90 | 0 | 1 | 90 |

La continuidad de la salida reduce saltos en el comando, pero **no garantiza** por sí sola estabilidad dinámica, ahorro energético ni seguridad del equipo.

### 3.5 Segunda variable: ocupación

Se incorpora ocupación $O\in[0,10]$, en número de personas. Para simplificar:

$$
\mu_{\mathrm{ocup\ baja}}(O)=R_{\downarrow}(O;2,8),\qquad
\mu_{\mathrm{ocup\ alta}}(O)=R_{\uparrow}(O;2,8).
$$

Ahora $O=5$ activa ambos términos con grado 0.5.

Puede construirse una tabla completa de $3\times2=6$ reglas, con salidas en porcentaje:

| Temperatura / Ocupación | Baja | Alta |
|---|---:|---:|
| Baja | 20 | 35 |
| Moderada | 50 | 70 |
| Alta | 80 | 95 |

Para reglas con dos antecedentes se usa $\min$. Si $T=27$ y $O=5$, las cuatro reglas con temperatura moderada o alta tienen activaciones $0.5,0.5,0.4,0.4$. Sus salidas correspondientes son 50, 70, 80 y 95:

$$
v^*=\frac{0.5(50)+0.5(70)+0.4(80)+0.4(95)}
{0.5+0.5+0.4+0.4}
=\frac{130}{1.8}\approx\boxed{72.22\%}.
$$

Se ve el valor de las reglas: las condiciones de temperatura y ocupación se combinan sin exigir que cada medición se clasifique primero en una única categoría.

**Nota de consistencia:** al utilizar mínimos, la salida es un promedio ponderado de activaciones no necesariamente normalizadas. Por eso no debe reemplazarse automáticamente esta fórmula por una combinación bilineal de pertenencias.

**Actividad en Excel.** Construir columnas para datos $T,O$, pertenencias, seis activaciones `MIN`, seis productos activación×consecuente y suma de activaciones. Calcular `SUMAPRODUCTO(activaciones;salidas)/SUMA(activaciones)`. Verificar los casos extremos y el punto $T=27,O=5$.

---

## 4. Anatomía de un sistema de inferencia difusa

El flujo general distingue:

```text
mediciones y unidades
       ↓
validación y vigencia
       ↓
funciones de pertenencia (fuzzificación)
       ↓
reglas SI–ENTONCES (activación)
       ↓
consecuentes y combinación
       ↓
salida numérica / conjunto de salida
       ↓
restricciones, actuación y registro
```

No todos los sistemas realizan el último cálculo de igual forma. Existen distintas familias de inferencia.

### 4.1 Mamdani: consecuentes difusos

En **Mamdani**, tanto los antecedentes como los consecuentes son términos difusos:

> SI temperatura alta Y ocupación alta ENTONCES velocidad muy alta.

Cada regla activada produce un conjunto difuso de salida. Con implicación por recorte:

$$
\mu_{B_i'}(v)=\min(\alpha_i,\mu_{B_i}(v)).
$$

Las salidas de las reglas pueden agregarse mediante máximo:

$$
\mu_B(v)=\max_i\mu_{B_i'}(v).
$$

Si se requiere una orden numérica, puede emplearse **desfuzzificación** por centroide:

$$
v^*=\frac{\int_0^{100}v\,\mu_B(v)\,dv}
{\int_0^{100}\mu_B(v)\,dv},
$$

siempre que el denominador sea positivo. Para trabajo manual, las integrales pueden aproximarse mediante una tabla de valores discretos. El sistema conserva conceptos lingüísticos también en la salida, pero requiere definir la geometría de los conjuntos resultantes y una forma de convertirlos en número.

### 4.2 Takagi–Sugeno: consecuentes constantes o funcionales

En **Takagi–Sugeno**, cada regla entrega una constante o función de las entradas:

$$
R_i:\quad \text{SI }T\text{ es }A_i \text{ Y } O\text{ es }B_i
\text{ ENTONCES }z_i=p_iT+q_iO+r_i.
$$

La salida es:

$$
v^*=\frac{\sum_i\alpha_i z_i}{\sum_i\alpha_i}.
$$

Si $p_i=q_i=0$, es Sugeno de **orden cero**, como el controlador calculado en la sección anterior. Si el consecuente es afín en las entradas, suele llamarse de primer orden. Su cálculo es eficiente y permite aproximar comportamientos no lineales mediante modelos locales.

### 4.3 Tsukamoto: una salida numérica por cada regla monotónica

En **Tsukamoto**, el consecuente de cada regla es un conjunto difuso **monotónico**, de modo que se pueda invertir su función de pertenencia:

$$
\mu_{B_i}(z_i)=\alpha_i,\qquad
z_i=\mu_{B_i}^{-1}(\alpha_i).
$$

Cada regla genera así un valor $z_i$; después se combinan:

$$
v^*=\frac{\sum_i\alpha_i z_i}{\sum_i\alpha_i}.
$$

Ejemplo: para un consecuente de velocidad creciente

$$
\mu_{\mathrm{velocidad\ alta}}(v)=R_{\uparrow}(v;50,100),
$$

una activación $\alpha=0.6$ implica $z=50+0.6(50)=80$. Es importante usar funciones monotónicas invertibles en la región de interés; un consecuente triangular completo no satisface directamente esa condición.

### 4.4 Comparación de modelos

| Propiedad | Mamdani | Sugeno | Tsukamoto |
|---|---|---|---|
| Consecuente de regla | conjunto difuso | constante o función | conjunto difuso monotónico |
| Producto por regla | conjunto activado | valor numérico | valor numérico invertido |
| Combinación | agregación + desfuzzificación | promedio ponderado | promedio ponderado |
| Expresión lingüística de salida | directa | menor en consecuentes funcionales | directa, con restricción de monotonicidad |
| Cálculo inicial a mano | tabla discreta | sencillo | intermedio |
| Uso habitual | control explicable | control, identificación y aproximación funcional | inferencia con salidas monotónicas |

No existe un modelo superior para todos los problemas. La selección depende de la representación deseada, la facilidad de inspección, el costo y el comportamiento que se deba preservar.

---

## 5. Vigencia de la evidencia y dimensión temporal

### 5.1 El problema de una medición que envejece

El controlador anterior supone que $T$ y $O$ describen **ahora** la habitación. Pero una lectura tiene un momento de adquisición $t_m$, y su edad es

$$
\Delta t=t-t_m\ge0.
$$

Una lectura de temperatura 30 °C tomada hace diez minutos no es equivalente a una lectura de 30 °C tomada hace un segundo. **La pertenencia a “temperatura alta” puede ser idéntica, pero la vigencia de la observación no.**

Eso no vuelve difusa la temperatura: introduce otra variable y otra cuestión de gestión de evidencia.

### 5.2 Un conjunto difuso temporal

Para una regla de operación que exige evidencia reciente, se propone el conjunto *medición reciente*:

$$
\mu_{\mathrm{reciente}}(\Delta t)=
\begin{cases}
1,&0\le\Delta t\le2,\\
\dfrac{10-\Delta t}{8},&2<\Delta t<10,\\
0,&\Delta t\ge10,
\end{cases}
$$

con $\Delta t$ en minutos. Los valores 2 y 10 son decisiones de diseño que deberán justificarse según la dinámica de la habitación y la frecuencia de muestreo.

A los 6 minutos: $\mu_{\mathrm{reciente}}(6)=0.5$.

La conjunción:

> SI temperatura alta Y lectura reciente, ENTONCES recomendar ventilación alta

tendría activación $\min(\mu_{\mathrm{alta}}(T),\mu_{\mathrm{reciente}}(\Delta t))$.

### 5.3 No confundir pérdida de vigencia con permiso para reducir ventilación

Hay una trampa importante. Si una lectura envejece, disminuir su activación y después promediar sólo las reglas restantes puede **reducir la ventilación sin evidencia de que la habitación se haya enfriado**. Eso sería una mala política.

Por tanto, la vigencia no debe añadirse ciegamente como otro peso. Se separan:

1. **Estimación:** velocidad recomendada a partir de lecturas recientes.
2. **Validez de evidencia:** si las lecturas permiten una recomendación confiable.
3. **Política de contingencia:** qué ocurre si falta evidencia: solicitar medición, mantener un estado conservador previamente autorizado, generar alerta o detener control automático.

Una solución segura ante datos ausentes o caducados requiere reglas de contingencia independientes; **nunca debe inferirse que “sin dato” equivale a “temperatura baja”**.

### 5.4 Estado y retroalimentación

Para mostrar la extensión temporal del control, puede representarse la evolución de la temperatura mediante un modelo de primer orden:

$$
T_{k+1}=T_k+\Delta\tau\,[a(T_{\mathrm{ext},k}-T_k)+q_k-b\,v_k],
$$

donde $T_k$ es la temperatura interior, $T_{\mathrm{ext},k}$ la exterior, $q_k$ una aportación térmica, $v_k$ el nivel de ventilación y $a,b$ parámetros compatibles con las unidades elegidas. Este modelo es una **aproximación**, no una ley universal: el efecto real de ventilación depende de temperatura exterior, caudal, ocupación y equipo. En particular, mayor ventilación no siempre enfría si el aire exterior es más caliente.

El sistema completo se convierte en un ciclo:

$$
\text{medir}\to\text{validar}\to\text{inferir }v_k
\to\text{actuar}\to\text{observar }T_{k+1}\to\text{ajustar}.
$$

Puede añadirse un límite de variación entre órdenes:

$$
|v_{k+1}-v_k|\le d_{\max}
$$

para restringir cambios excesivamente rápidos. Ese límite es una **restricción operativa**, no un grado de pertenencia.

### 5.5 Actividad de análisis temporal

Tres registros reportan la misma temperatura: 30 °C, obtenidos hace 1, 6 y 12 minutos. Calcular la pertenencia a “medición reciente” y decidir cuál evidencia puede utilizarse según una política enunciada. Después discutir por qué la velocidad no debe disminuir de forma automática al agotarse la vigencia de la lectura.

---

## 6. Cinco preguntas de investigación

Las respuestas representan un punto de partida y dejan cuestiones de diseño o validación abiertas.

### Pregunta 1. ¿Cómo determinar funciones de pertenencia que no sean arbitrarias?

**Respuesta parcial.** Pueden construirse a partir del lenguaje y experiencia de especialistas, límites observados, preferencias declaradas o datos históricos. Las curvas no se justifican por ser suaves; deben preservar el significado que se quiere expresar. El trabajo seminal de Zadeh formalizó la pertenencia gradual, pero no convirtió la elección de funciones en un procedimiento universal.

**Reto:** solicitar a tres operadores que determinen cuándo una habitación es “caliente”, comparar las fronteras y definir un criterio para resolver diferencias. ¿Conviene una función compartida o funciones condicionadas por contexto?

**Referencia:** [Zadeh, *Fuzzy Sets* (1965)](https://doi.org/10.1016/S0019-9958(65)90241-X).

### Pregunta 2. ¿Por qué utilizar reglas difusas si una interpolación convencional puede producir la misma salida?

**Respuesta parcial.** Con una única variable y una partición sencilla, una interpolación explícita puede ser suficiente. Las reglas se vuelven útiles cuando un especialista puede explicar comportamientos mediante varios antecedentes y consecuentes locales, especialmente si deben modificarse y auditarse. Aun así, no eliminan la necesidad de probar la superficie global.

**Reto:** construir una ecuación directa para temperatura únicamente; compararla con la tabla de seis reglas temperatura–ocupación y justificar cuál resulta más fácil de mantener cuando se introduce otra variable.

**Referencia:** [Takagi y Sugeno, identificación difusa (1985)](https://doi.org/10.1109/TSMC.1985.6313399).

### Pregunta 3. ¿Cómo elegir entre Mamdani, Sugeno y Tsukamoto?

**Respuesta parcial.** Mamdani representa directamente términos lingüísticos en la salida; Sugeno facilita consecuentes numéricos y cálculo; Tsukamoto asocia cada regla con un valor obtenido de un consecuente monotónico. La elección depende de explicabilidad, eficiencia y posibilidad de validación, no de una clasificación de “más avanzado”.

**Reto:** expresar una regla de ventilación en las tres formas y comparar qué conocimiento se conserva y qué parámetros adicionales deben establecerse.

**Referencias:** [Mamdani y Assilian (1975)](https://doi.org/10.1016/S0020-7373(75)80002-2); [Takagi y Sugeno (1985)](https://doi.org/10.1109/TSMC.1985.6313399).

### Pregunta 4. ¿Puede aprenderse automáticamente una base de reglas sin perder significado?

**Respuesta parcial.** Modelos neurodifusos como ANFIS permiten ajustar parámetros mediante observaciones de entrada y salida. Mejorar el ajuste no garantiza que las reglas aprendidas continúen siendo entendibles o tengan comportamiento adecuado fuera de muestra.

**Reto:** proponer restricciones de monotonicidad: con la misma ocupación, una temperatura mayor no debería solicitar menos ventilación **si las condiciones físicas hacen apropiada esa política**. ¿Cómo comprobarlo en una tabla?

**Referencia:** [Jang, ANFIS (1993)](https://doi.org/10.1109/21.256541).

### Pregunta 5. ¿Cómo se verifica un sistema difuso cuando cambian el entorno y el tiempo?

**Respuesta parcial.** Se requieren pruebas de cobertura de reglas, continuidad, monotonicidad esperada, saturaciones, falta de datos, antigüedad de mediciones y restricciones físicas. Un sistema que ofrece una salida numérica para todos los valores puede seguir siendo incorrecto si las reglas se contradicen o actúan sobre datos caducados.

**Reto:** diseñar una matriz de pruebas con temperatura mínima, máxima, valores de cruce, ocupación extrema y pérdida de comunicación durante 12 minutos. Separar resultados de inferencia de autorizaciones operativas.

**Referencias de partida:** [Mamdani y Assilian (1975)](https://doi.org/10.1016/S0020-7373(75)80002-2); [Jang (1993)](https://doi.org/10.1109/21.256541).

---

## 7. Tres casos históricos de estudio

### Caso 1. Zadeh y los conjuntos difusos (1965): representar categorías graduales

**Problema.** Los conjuntos ordinarios modelan pertenencia binaria, mientras muchos conceptos de uso común tienen transiciones graduales.

**Contribución.** Lotfi A. Zadeh formalizó conjuntos caracterizados por funciones con grados de pertenencia continuos entre cero y uno y extendió operaciones como unión, intersección y complemento.

**Lección.** El avance inicial fue representacional: describir conceptos graduales matemáticamente. Un conjunto difuso, por sí mismo, todavía no constituye un controlador.

**Pregunta:** ¿qué parte del significado de “caliente” puede formalizarse con una curva y qué parte depende de contexto y preferencias?

**Fuente:** [Zadeh (1965), *Information and Control*](https://doi.org/10.1016/S0019-9958(65)90241-X).

### Caso 2. Mamdani y Assilian (1975): de la experiencia del operador al control

**Problema.** Construir una estrategia de control para un modelo de planta industrial —una máquina de vapor— a partir de reglas heurísticas formuladas por un operador humano.

**Contribución.** Mostraron un controlador que convertía reglas lingüísticas en una estrategia automática de actuación. La aplicación conectó vocabulario, reglas, inferencia y respuesta de una planta dinámica.

**Lección.** Un conjunto de reglas comprensibles puede describir una política de control, pero su resultado debe contrastarse con el comportamiento físico y la estabilidad del sistema.

**Pregunta:** ¿qué parte del conocimiento de un operador se puede formular como reglas y qué parte requiere observar cambios de estado a lo largo del tiempo?

**Fuente:** [Mamdani y Assilian (1975), *International Journal of Man-Machine Studies*](https://doi.org/10.1016/S0020-7373(75)80002-2).

### Caso 3. Takagi y Sugeno (1985): modelos locales de procesos industriales

**Problema.** Identificar el comportamiento de procesos mediante datos de entrada y salida y emplear el resultado para modelado y control.

**Contribución.** Plantearon reglas cuyos antecedentes describen regiones difusas del espacio de entradas, mientras los consecuentes contienen relaciones funcionales. El artículo incluye aplicaciones a limpieza de agua y a un convertidor en la producción de acero.

**Lección.** La inferencia difusa no se limita a frases lingüísticas para la salida: puede combinar modelos matemáticos locales que aproximan una respuesta no lineal.

**Pregunta:** ¿cuándo conviene usar constantes de salida fáciles de explicar y cuándo expresiones lineales que describan mejor el proceso?

**Fuente:** [Takagi y Sugeno (1985), *IEEE Transactions on Systems, Man, and Cybernetics*](https://doi.org/10.1109/TSMC.1985.6313399).

---

## 8. Línea de tiempo: avances e hitos

| Año | Hito | Relevancia |
|---:|---|---|
| 1920–1930 | desarrollo de lógicas multivaluadas | amplía la discusión sobre valores de verdad más allá de la dicotomía clásica |
| 1965 | Zadeh publica *Fuzzy Sets* | formaliza los grados de pertenencia |
| década de 1970 | desarrollo de variables lingüísticas y razonamiento aproximado | conecta lenguaje y representación matemática gradual |
| 1975 | Mamdani y Assilian publican un controlador lingüístico | muestran inferencia difusa aplicada a un proceso dinámico |
| finales de 1970 | desarrollo de métodos de inferencia asociados con Tsukamoto | consolida la obtención de salidas por inversión de consecuentes monotónicos |
| 1985 | Takagi y Sugeno presentan identificación difusa de sistemas | emplea regiones difusas con modelos funcionales locales |
| décadas de 1980–1990 | extensión de controladores difusos a sistemas industriales y de consumo | evidencia fortalezas prácticas y problemas de ajuste |
| 1993 | Jang publica ANFIS | combina reglas difusas y aprendizaje paramétrico |
| 1990–2000 | investigación en conjuntos difusos tipo 2 | incorpora incertidumbre sobre la propia pertenencia |
| 2000–presente | sistemas híbridos, neurodifusos y técnicas de optimización | estudian ajuste, interpretabilidad y adaptación |

La cronología muestra la coexistencia de distintas representaciones, no la sustitución obligatoria de una por otra.

---

## 9. Modelo matemático integrado: de reglas rígidas a control temporal

### 9.1 Definición del sistema

Se define un sistema de inferencia de ventilación:

$$
\mathcal F=(X_T,X_O,\{\mu\},\mathcal R,\mathcal A,\mathcal P),
$$

donde $X_T=[20,35]$, $X_O=[0,10]$, $\{\mu\}$ son las pertenencias especificadas, $\mathcal R$ es la tabla de seis reglas, $\mathcal A$ fija la conjunción mínimo y $\mathcal P$ combina los consecuentes mediante promedio ponderado.

Para cada regla $(i,j)$, con término térmico $i$, término de ocupación $j$ y salida $z_{ij}$:

$$
\alpha_{ij}(T,O)=\min\{\mu_{T_i}(T),\mu_{O_j}(O)\}.
$$

La superficie de respuesta es:

$$
\boxed{V(T,O)=
\frac{\sum_{i,j}\alpha_{ij}(T,O)z_{ij}}
{\sum_{i,j}\alpha_{ij}(T,O)}}
$$

cuando el denominador es positivo. En las particiones escogidas, hay cobertura del dominio en todas las entradas válidas. La fórmula define una **superficie de decisiones** sobre dos variables medidas; no modela por sí sola la dinámica térmica.

### 9.2 Cálculo reproducible

Con $T=27$, $O=5$:

| Regla | $\alpha$ | $z$ | $\alpha z$ |
|---|---:|---:|---:|
| baja / baja | 0 | 20 | 0 |
| baja / alta | 0 | 35 | 0 |
| moderada / baja | 0.5 | 50 | 25 |
| moderada / alta | 0.5 | 70 | 35 |
| alta / baja | 0.4 | 80 | 32 |
| alta / alta | 0.4 | 95 | 38 |
| **Total** | **1.8** | | **130** |

$$
V(27,5)=130/1.8\approx72.22.
$$

En Excel es suficiente construir una tabla con temperaturas y ocupaciones, calcular pertenencias con `SI`, `MAX` y `MIN`, evaluar las seis activaciones y aplicar `SUMAPRODUCTO/SUMA`. No se necesitan bibliotecas ni programación.

### 9.3 Pruebas de propiedades

Se deben evaluar al menos:

- **Cobertura:** $\sum_{ij}\alpha_{ij}>0$ para todas las entradas admisibles.
- **Acotación:** la salida ponderada se mantiene entre los consecuentes mínimo y máximo si todas las activaciones son no negativas.
- **Continuidad:** verificar cambios pequeños en $T$ y $O$ alrededor de las fronteras.
- **Monotonicidad esperada:** aumentar temperatura u ocupación no debería disminuir la orden en el régimen donde se haya definido tal objetivo.
- **Robustez:** comparar resultados para perturbaciones de ±0.1 °C.
- **Restricciones:** comprobar que el actuador soporta los valores solicitados.
- **Vigencia:** rechazar o escalar lecturas antiguas según política explícita.

### 9.4 Modelo temporal y decisiones

Se registran $(T_k,O_k,t_k)$. Antes de calcular $V(T_k,O_k)$, se valida la antigüedad. Si la medición es válida, se calcula la recomendación y se aplica una restricción de cambio:

$$
v_{k+1}=
\operatorname{clip}
\left(V(T_k,O_k),\ v_k-d_{\max},\ v_k+d_{\max}\right),
$$

donde `clip` limita la orden al intervalo indicado. Si la lectura no es válida, se sigue una política de contingencia **separada** que no presuponga un estado seguro.

Finalmente se observa $T_{k+1}$ para evaluar la respuesta del sistema. Una secuencia de mediciones permite identificar si la ventilación consiguió un cambio de temperatura, si existen oscilaciones o si las reglas deben revisarse.

### 9.5 Ejercicios integradores

1. Elaborar una tabla de las velocidades rígidas para $T=24,25,26,27,28,29,30$ y compararla con el sistema de tres reglas Sugeno.
2. Recalcular las seis reglas para $T=28,O=7$. Identificar las reglas activadas y justificar qué aporta la variable de ocupación.
3. Sustituir la conjunción mínimo por producto y comparar cómo cambia la superficie de respuesta.
4. Diseñar en papel tres conjuntos difusos de **velocidad** y explicar cómo Mamdani recortaría y combinaría sus consecuentes.
5. Para $T=30$ °C medidos hace 1, 6 y 12 minutos, calcular la pertenencia temporal y definir una respuesta cuando la lectura no sea vigente.
6. Proponer un control de cambio máximo de 10 puntos porcentuales por periodo. ¿Qué orden real se emitiría si la recomendación cambia de 40 % a 90 %? ¿Qué ocurriría si persiste la nueva condición?

**Conclusión matemática:** las funciones de pertenencia representan conceptos; las reglas construyen un campo de actuación; el promedio ponderado da una recomendación numérica; y la dimensión temporal obliga a separar inferencia, estado, vigencia, restricciones y retroalimentación.

---

## 10. Conexiones con los demás temas y módulos

### Con 1.1 — Fundamentos de sistemas cognitivos

La ventilación automática ejemplifica el ciclo **percepción → representación → inferencia → acción → retroalimentación**. Tener reglas difusas no implica por sí mismo aprendizaje, conciencia ni autonomía general.

### Con 1.2 — Arquitecturas de representación del conocimiento

Las funciones de pertenencia amplían la representación de categorías; la tabla de reglas es una base de conocimiento explícita. Se conserva la distinción entre hecho, regla, restricción, temporalidad y procedencia.

### Con 1.4 — Ontologías y grafos de conocimiento

Los conceptos `Sensor`, `Habitación`, `Medición`, `Ventilador` y `ReglaDeControl` pueden asociarse mediante relaciones como `mide`, `ubicadoEn`, `actúaSobre` o `vigenteEn`. El grafo identifica fuentes y relaciones; la lógica difusa agrega grados a conceptos relevantes.

### Con 1.5 — Optimización de procesos

Una recomendación de ventilación puede confrontarse con objetivos de confort, consumo eléctrico, desgaste, límites de equipo y disponibilidad. **Inferir una velocidad no equivale a demostrar que sea óptima**.

### Con probabilidad, estadística y ciencia de datos

La pertenencia no es una probabilidad. Una distribución de temperaturas estima frecuencias o probabilidades de observaciones; una función de pertenencia describe qué tan compatible es cada temperatura con un concepto. Ambas pueden relacionarse sin confundirse.

### Con aprendizaje automático y sistemas híbridos

Los datos pueden servir para ajustar parámetros de funciones y consecuentes, pero hacen falta restricciones y validación. Modelos como ANFIS conectan inferencia difusa con aprendizaje; un sistema híbrido podría utilizar predicción estadística y reglas de operación explícitas.

---

## 11. Síntesis

Una regla clásica selecciona una categoría mediante condiciones binarias. Un conjunto difuso admite pertenencia gradual. Una regla difusa se activa en un grado que depende de sus antecedentes. Un sistema de inferencia combina múltiples reglas y ofrece una salida numérica o un conjunto difuso de salida.

La utilidad de la lógica difusa no consiste en reemplazar todas las condiciones exactas por curvas. Consiste en ofrecer una representación computable de **conceptos graduales** y una forma estructurada de **combinar comportamientos locales expresados mediante reglas**.

El control de ventilación ilustra el recorrido completo:

$$
\boxed{\text{medir}\rightarrow\text{clasificar}\rightarrow\text{graduar}
\rightarrow\text{activar reglas}\rightarrow\text{combinar}\rightarrow\text{actuar}\rightarrow\text{verificar}}
$$

La extensión temporal recuerda que una recomendación sólo es tan útil como la evidencia y las restricciones que la sostienen.

---

## Referencias principales

1. Zadeh, L. A. (1965). *Fuzzy Sets*. **Information and Control**, 8(3), 338–353. https://doi.org/10.1016/S0019-9958(65)90241-X
2. Mamdani, E. H., & Assilian, S. (1975). *An Experiment in Linguistic Synthesis with a Fuzzy Logic Controller*. **International Journal of Man-Machine Studies**, 7(1), 1–13. https://doi.org/10.1016/S0020-7373(75)80002-2
3. Takagi, T., & Sugeno, M. (1985). *Fuzzy Identification of Systems and Its Applications to Modeling and Control*. **IEEE Transactions on Systems, Man, and Cybernetics**, SMC-15(1), 116–132. https://doi.org/10.1109/TSMC.1985.6313399
4. Jang, J.-S. R. (1993). *ANFIS: Adaptive-Network-Based Fuzzy Inference System*. **IEEE Transactions on Systems, Man, and Cybernetics**, 23(3), 665–685. https://doi.org/10.1109/21.256541
