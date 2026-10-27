# Módulo 1.2 — Glosario de arquitecturas de representación del conocimiento

> **Inteligencia Artificial**  
> **Módulo 1:** Sistemas cognitivos y representación del conocimiento  
> **Tema:** Arquitecturas de representación del conocimiento

## Cómo utilizar este glosario

Los conceptos se presentan en orden alfabético. Cada entrada incluye:

- una explicación breve;
- su relación con otros términos del módulo;
- una referencia o tema para continuar el aprendizaje.

Las referencias priorizan especificaciones, artículos académicos y recursos institucionales. Los ejemplos aeroportuarios son didácticos y no representan procedimientos operacionales.

---

## Arquitectura de representación del conocimiento

Conjunto organizado de lenguajes, estructuras, mecanismos de inferencia y controles que permiten adquirir, almacenar, consultar, actualizar y utilizar conocimiento. Incluye más que una base de datos: define qué significan sus elementos y qué conclusiones pueden derivarse.

Una arquitectura completa suele considerar vocabulario, semántica, inferencia, procedencia, versiones, permisos e interfaces con percepción y decisión.

**Relacionado con:** base de conocimiento, motor de inferencia, semántica, gobernanza.

**Para aprender más:** tema **Knowledge Representation and Reasoning** y el capítulo introductorio de [Knowledge Representation and Reasoning, Brachman y Levesque](https://www.cs.toronto.edu/~hector/Papers/krbook.pdf).

---

## Arquitectura híbrida

Arquitectura que combina dos o más formas de representación, por ejemplo:

- vectores para percepción y recuperación;
- símbolos para entidades y relaciones;
- reglas para restricciones;
- probabilidades para incertidumbre;
- optimización para seleccionar acciones.

La dificultad central no consiste sólo en conectar componentes, sino en definir qué información cruza cada interfaz y cómo se valida. Una similitud vectorial, por ejemplo, no debe convertirse automáticamente en un hecho certificado.

**Relacionado con:** arquitectura neuro-simbólica, embedding, representación simbólica, incertidumbre.

**Para aprender más:** [Neural-Symbolic Computing: An Effective Methodology for Principled Integration of Machine Learning and Reasoning](https://arxiv.org/abs/1905.06088).

---

## Arquitectura neuro-simbólica

Tipo de arquitectura híbrida que integra aprendizaje neuronal con representaciones o procedimientos simbólicos. Un componente neuronal puede reconocer objetos o extraer conceptos, mientras un componente simbólico aplica reglas, ejecuta programas o comprueba restricciones.

Su promesa es combinar generalización perceptual con razonamiento estructurado. Sus principales retos son el *grounding*, la propagación de errores y la evaluación de si el sistema realmente utiliza la estructura simbólica.

**Relacionado con:** grounding, representación distribuida, razonador, arquitectura híbrida.

**Para aprender más:** [The Neuro-Symbolic Concept Learner, Mao et al.](https://openreview.net/pdf/a0f215dd254bc10d946ccc26632ca8e42defee17.pdf).

---

## Base de conocimiento

Colección estructurada de hechos, conceptos, reglas, restricciones y metadatos que un sistema puede consultar o utilizar para inferir conclusiones. A diferencia de una base de datos convencional, su diseño suele hacer explícito el significado de las relaciones y el conocimiento que puede derivarse.

Puede representarse mediante lógica, reglas, marcos, ontologías, grafos o combinaciones de ellos.

**Relacionado con:** hecho, regla, restricción de integridad, motor de inferencia.

**Para aprender más:** tema **knowledge base versus database** y [Knowledge Representation, Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/knowledge-representation/).

---

## Cláusula de Horn

Expresión lógica que contiene como máximo un literal positivo. En programación lógica suele escribirse como una regla:

$$
b_1\land b_2\land\cdots\land b_m\rightarrow h
$$

$b_1,\ldots,b_m$ forman el cuerpo o condiciones; $h$ es la cabeza o conclusión. Su estructura restringida permite mecanismos de inferencia eficientes y fundamenta lenguajes como Prolog y Datalog.

**Relacionado con:** Datalog, regla de producción, encadenamiento, punto fijo.

**Para aprender más:** [The Semantics of Predicate Logic as a Programming Language, van Emden y Kowalski](https://maarten.vanemden.com/Publications/kowVE.pdf).

---

## Compromiso ontológico

Decisión acerca de qué tipos de entidades, propiedades y relaciones se consideran existentes y relevantes dentro de una representación.

Si un modelo distingue entre `Alerta`, `Observación` y `Falla`, se compromete a tratarlas como categorías diferentes. Esta decisión determina qué puede expresarse y qué confusiones puede evitarse.

**Relacionado con:** conceptualización, ontología, vocabulario controlado, esquema.

**Para aprender más:** tema **ontological commitments in knowledge representation** y [Ontological Commitments, Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/ontological-commitment/).

---

## Conceptualización

Modelo abstracto de un dominio: qué objetos se distinguen, qué propiedades poseen y cómo se relacionan. Una ontología formaliza parte de una conceptualización para hacerla explícita y compartible.

Dos sistemas pueden almacenar datos similares y, sin embargo, usar conceptualizaciones incompatibles. Uno puede representar una inspección como evento; otro, como atributo del activo.

**Relacionado con:** compromiso ontológico, ontología, esquema, interoperabilidad semántica.

**Para aprender más:** Gruber, [A Translation Approach to Portable Ontology Specifications](https://tomgruber.org/writing/ontolingua-kaj-1993.pdf).

---

## Conocimiento declarativo

Conocimiento que expresa hechos, relaciones o condiciones sin prescribir necesariamente una secuencia de ejecución.

```text
Toda pista activa es un activo crítico.
SensorS1 monitorea Pista09.
```

Permite preguntar qué es verdadero y separar el conocimiento del procedimiento utilizado para consultarlo.

**Relacionado con:** hecho, lógica, conocimiento procedimental, ontología.

**Para aprender más:** tema **programación declarativa y lógica**.

---

## Conocimiento procedimental

Conocimiento acerca de cómo realizar una tarea: secuencias, habilidades, flujos o políticas de acción.

```text
Bloquear el activo → asignar inspector → registrar evidencia → solicitar autorización.
```

Puede estar representado como código, reglas, planes, procesos o políticas. Separarlo del conocimiento declarativo facilita actualizar procedimientos sin redefinir todo el dominio.

**Relacionado con:** procedimiento, regla de producción, política, flujo de trabajo.

**Para aprender más:** tema **declarative versus procedural knowledge** y **planificación automática**.

---

## Datalog

Lenguaje declarativo basado en cláusulas de Horn, utilizado para consultas recursivas y bases de datos deductivas. Puede expresar relaciones como la clausura transitiva:

```text
alcanza(x,y) ← conecta(x,y)
alcanza(x,z) ← conecta(x,y) ∧ alcanza(y,z)
```

Su sintaxis restringida permite estudiar claramente terminación, semántica de punto fijo y complejidad.

**Relacionado con:** cláusula de Horn, punto fijo, programación lógica, inferencia.

**Para aprender más:** tema **Datalog, bases deductivas y consultas recursivas** y [Datalog: Concepts, History, and Outlook](https://doi.org/10.1007/978-3-319-10587-1_1).

---

## Encadenamiento hacia adelante

Estrategia de inferencia dirigida por datos. Comienza con hechos disponibles, identifica reglas cuyas condiciones se cumplen y agrega sus conclusiones. Se repite hasta alcanzar una meta o hasta que no aparezcan hechos nuevos.

Es apropiada para monitoreo, alertas y materialización de conocimiento derivado. Puede producir conclusiones que ninguna consulta necesita si no se controla su alcance.

**Relacionado con:** motor de inferencia, regla, operador de consecuencia inmediata, punto fijo.

**Para aprender más:** tema **forward chaining y sistemas de producción**.

---

## Encadenamiento hacia atrás

Estrategia de inferencia dirigida por una meta. Parte de la conclusión que se desea demostrar y busca reglas que podrían producirla; después intenta demostrar sus condiciones.

Por ejemplo, para responder `requiereInspeccion(P09)`, el sistema busca qué regla concluye `requiereInspeccion` y qué hechos necesita comprobar.

**Relacionado con:** consulta, demostración, Prolog, encadenamiento hacia adelante.

**Para aprender más:** tema **backward chaining, resolución SLD y programación lógica**.

---

## Entidad

Objeto distinguible al que la arquitectura asigna identidad: una persona, un sensor, una pista, un evento o un documento. Una entidad no es igual a su nombre. Puede tener distintas etiquetas y aparecer en múltiples fuentes.

La resolución de entidades determina si dos registros se refieren al mismo objeto o a objetos diferentes.

**Relacionado con:** identidad, IRI, grafo de conocimiento, resolución de entidades.

**Para aprender más:** tema **entity resolution and record linkage**.

---

## Expresividad

Capacidad de un lenguaje para describir clases de conocimiento, relaciones y restricciones. Cuantificadores, negación, temporalidad, excepciones y cardinalidades aumentan lo que puede expresarse.

Mayor expresividad no siempre es mejor: puede aumentar el costo de inferencia y dificultar validación, interoperabilidad y mantenimiento.

**Relacionado con:** tratabilidad, decidibilidad, lógica descriptiva, perfil de lenguaje.

**Para aprender más:** tema **expressivity–tractability trade-off** y los [perfiles de OWL 2](https://www.w3.org/TR/owl2-profiles/).

---

## Frame o marco

Estructura que agrupa conocimiento sobre una situación u objeto típico mediante ranuras, valores, restricciones y valores por defecto. Un marco de `Inspección` puede incluir activo, responsable, evidencia, fecha y resultado esperado.

Minsky propuso los marcos como estructuras recordadas que se adaptan a una situación concreta modificando detalles.

**Relacionado con:** slot, valor por defecto, red semántica, esquema.

**Para aprender más:** Minsky, [A Framework for Representing Knowledge](https://dspace.mit.edu/entities/publication/0eca0164-cb5f-42de-8c86-43f54b23306d).

---

## Grafo de conocimiento

Representación de entidades y relaciones mediante nodos, aristas o afirmaciones estructuradas. Puede incorporar tipos, restricciones, calificadores, procedencia e inferencia.

El grafo es la instancia de conocimiento; la ontología suele aportar parte del vocabulario y la semántica. No todo grafo es automáticamente una ontología ni toda ontología necesita materializarse como un gran grafo.

**Relacionado con:** entidad, ontología, triple RDF, procedencia.

**Para aprender más:** [Knowledge Graphs, Hogan et al.](https://doi.org/10.1145/3447772) y el tema **1.4 Ontologías y grafos de conocimiento**.

---

## Grounding o fundamentación de símbolos

Problema de conectar un símbolo con percepción, acción o criterios verificables del mundo. Una etiqueta como `contaminación` necesita reglas de observación y uso; no adquiere significado sólo por relacionarse con otros símbolos.

En una arquitectura híbrida, el paso de una señal neuronal a una categoría simbólica es una hipótesis que debe calibrarse y auditarse.

**Relacionado con:** símbolo, percepción, arquitectura neuro-simbólica, semántica.

**Para aprender más:** Harnad, [The Symbol Grounding Problem](https://doi.org/10.1016/0167-2789(90)90087-6).

---

## Hecho

Afirmación que la base de conocimiento trata como disponible dentro de cierto contexto:

```text
monitorea(SensorS1, Pista09)
```

Un hecho operativo debería acompañarse de fuente, tiempo, versión y alcance. Que esté almacenado no garantiza que sea verdadero en todo momento.

**Relacionado con:** afirmación, regla, contexto, procedencia.

**Para aprender más:** tema **facts, assertions and named graphs** en RDF.

---

## Identidad

Mecanismo para distinguir entidades y reconocer cuándo varias referencias apuntan a la misma. Un nombre puede cambiar; un identificador estable busca mantener continuidad.

Los errores de identidad provocan duplicados, fusiones incorrectas y relaciones asignadas al objeto equivocado.

**Relacionado con:** entidad, IRI, resolución de entidades, clave primaria.

**Para aprender más:** tema **identificadores persistentes y gestión de datos maestros**.

---

## Inferencia

Proceso mediante el cual un sistema obtiene conclusiones a partir de conocimiento disponible. Puede ser deductiva, probabilística, abductiva, difusa o basada en similitud, entre otras variantes.

La arquitectura debe especificar qué tipo de inferencia utiliza y qué garantías ofrece. Una deducción lógica y una predicción estadística no tienen el mismo significado.

**Relacionado con:** razonador, regla, entailment, incertidumbre.

**Para aprender más:** tema **knowledge representation and automated reasoning**.

---

## Interoperabilidad semántica

Capacidad de varios sistemas para intercambiar información conservando un significado suficientemente común. No se logra sólo usando el mismo formato; también requiere vocabularios, unidades, identificadores y condiciones de uso compatibles.

**Relacionado con:** ontología, mapeo, vocabulario controlado, RDF.

**Para aprender más:** tema **semantic interoperability and ontology alignment**.

---

## IRI — Identificador Internacionalizado de Recursos

Cadena Unicode utilizada para identificar recursos. RDF permite usar IRIs como sujetos, predicados y objetos, lo que facilita combinar afirmaciones provenientes de diferentes sistemas.

Una IRI identifica; no tiene que mostrar toda la información del recurso ni garantizar que exista una página web recuperable.

**Relacionado con:** RDF, entidad, identidad, URI.

**Para aprender más:** [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf-concepts/).

---

## Lógica descriptiva

Familia de formalismos para representar conceptos, roles, individuos y restricciones con semántica precisa. Permite tareas como:

- comprobar consistencia;
- determinar si una clase es subclase de otra;
- clasificar conceptos;
- recuperar instancias.

Las lógicas descriptivas fundamentan gran parte de OWL 2. Sus variantes equilibran expresividad y tratabilidad.

**Relacionado con:** ontología, OWL, subsunción, razonador.

**Para aprender más:** [The Description Logic Handbook](https://www.cambridge.org/core/books/description-logic-handbook/65B3D92B5D3E7BDF1E1C43D2746C40E8) y [OWL 2 Direct Semantics](https://www.w3.org/TR/owl2-direct-semantics/).

---

## Materialización

Proceso de calcular y almacenar por adelantado hechos derivados. Si la base contiene `Pista ⊑ ActivoCritico` y `Pista(P09)`, puede materializar `ActivoCritico(P09)`.

Mejora algunas consultas, pero obliga a actualizar o invalidar conclusiones cuando cambian hechos o reglas.

**Relacionado con:** encadenamiento hacia adelante, cierre inferencial, vista materializada, actualización incremental.

**Para aprender más:** tema **materialized inference and incremental reasoning**.

---

## Monotonicidad

Propiedad según la cual agregar conocimiento no invalida conclusiones ya obtenidas:

$$
K\models q\quad\Rightarrow\quad K\cup K'\models q
$$

La lógica clásica es monotónica. Esta propiedad simplifica el razonamiento incremental, pero no representa de forma natural excepciones y conclusiones revisables.

**Relacionado con:** razonamiento no monotónico, entailment, lógica clásica.

**Para aprender más:** tema **monotonic logic and belief revision**.

---

## Motor de inferencia

Componente que aplica reglas o procedimientos de razonamiento sobre una base de conocimiento. Puede administrar coincidencias, agenda de reglas, prioridades, demostraciones y detección de conflictos.

Separar el motor del conocimiento permite reutilizar el mecanismo de inferencia en distintos dominios, aunque las garantías dependen del lenguaje aceptado.

**Relacionado con:** base de conocimiento, encadenamiento, razonador, regla de producción.

**Para aprender más:** tema **production system architecture and rule engines**.

---

## Ontología

Especificación formal de conceptos, relaciones y restricciones de un dominio compartido. Ayuda a que personas y sistemas utilicen términos con significados compatibles.

Puede definir, por ejemplo, que toda `Pista` es un `Activo`, que `monitorea` relaciona un `Sensor` con un `Activo` y que ciertos tipos son incompatibles.

**Relacionado con:** conceptualización, lógica descriptiva, OWL, grafo de conocimiento.

**Para aprender más:** Gruber, [A Translation Approach to Portable Ontology Specifications](https://tomgruber.org/writing/ontolingua-kaj-1993.pdf), y el tema **1.4**.

---

## Operador de consecuencia inmediata

Operador matemático que agrega a una interpretación las conclusiones de todas las reglas cuyas condiciones se cumplen:

$$
T_R(I)=I\cup\{h\theta\mid(b_1\land\cdots\land b_m\rightarrow h)\in R,\{b_1\theta,\ldots,b_m\theta\}\subseteq I\}
$$

Aplicarlo repetidamente permite calcular el cierre de una base de reglas positivas.

**Relacionado con:** punto fijo, cláusula de Horn, Datalog, encadenamiento hacia adelante.

**Para aprender más:** van Emden y Kowalski, [The Semantics of Predicate Logic as a Programming Language](https://maarten.vanemden.com/Publications/kowVE.pdf).

---

## OWL — Web Ontology Language

Lenguaje del W3C para representar ontologías con semántica formal. Permite expresar clases, propiedades, individuos, equivalencias, disyunciones, cardinalidades y otras restricciones.

OWL 2 dispone de perfiles con diferentes compromisos entre capacidad expresiva y costo de razonamiento.

**Relacionado con:** RDF, ontología, lógica descriptiva, razonador.

**Para aprender más:** [OWL 2 Web Ontology Language — Document Overview](https://www.w3.org/TR/owl-overview/).

---

## Procedencia

Información que describe el origen y la historia de un dato o conclusión: fuente, autor, tiempo, transformación, regla aplicada y versión.

Permite responder no sólo “¿qué concluyó el sistema?”, sino “¿a partir de qué evidencia y bajo qué configuración?”.

**Relacionado con:** trazabilidad, auditoría, grafo nombrado, versión.

**Para aprender más:** [PROV-O: The PROV Ontology, W3C](https://www.w3.org/TR/prov-o/).

---

## Punto fijo

Estado de una iteración en el que volver a aplicar el operador no produce cambios:

$$
I^*=T_R(I^*)
$$

En una base finita de reglas positivas, el menor punto fijo representa todos los hechos que pueden derivarse mediante esas reglas.

**Relacionado con:** operador de consecuencia inmediata, cierre inferencial, Datalog.

**Para aprender más:** tema **least fixed-point semantics**.

---

## RDF — Resource Description Framework

Modelo del W3C para representar información como triples sujeto–predicado–objeto. Un grafo RDF es un conjunto de triples y un *dataset* RDF puede contener un grafo predeterminado y varios grafos nombrados.

RDF define una estructura común para enlazar información, pero los vocabularios y reglas adicionales determinan buena parte de su significado de dominio.

**Relacionado con:** triple, IRI, grafo de conocimiento, OWL.

**Para aprender más:** [RDF 1.1 Concepts and Abstract Syntax](https://www.w3.org/TR/rdf-concepts/).

---

## Razonador

Software que calcula consecuencias semánticas, comprueba consistencia o responde consultas a partir de una representación formal. Un razonador OWL puede clasificar conceptos; un motor de reglas puede aplicar producciones; un sistema probabilístico puede actualizar creencias.

El término no implica un único método. Siempre debe especificarse qué semántica y qué reglas utiliza.

**Relacionado con:** motor de inferencia, entailment, ontología, consulta.

**Para aprender más:** tema **automated reasoning and ontology reasoners**.

---

## Razonamiento no monotónico

Razonamiento en el que nueva información puede retirar una conclusión anterior. Es necesario para representar reglas por defecto, excepciones y conocimiento revisable.

```text
Por defecto, un activo disponible puede asignarse.
Nueva evidencia: su inspección está vencida.
Conclusión revisada: no puede asignarse.
```

**Relacionado con:** monotonicidad, excepción, supuesto de mundo cerrado, revisión de creencias.

**Para aprender más:** [Non-monotonic Logic, Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/logic-nonmonotonic/).

---

## Red semántica

Representación mediante nodos conceptuales y relaciones etiquetadas. Permite visualizar asociaciones, jerarquías e instancias.

Las primeras redes semánticas podían resultar ambiguas porque relaciones visualmente parecidas no siempre tenían una semántica formal común. Las lógicas descriptivas buscaron precisar varias de estas relaciones.

**Relacionado con:** frame, grafo de conocimiento, herencia, KL-ONE.

**Para aprender más:** Brachman y Schmolze, [An Overview of the KL-ONE Knowledge Representation System](https://doi.org/10.1207/s15516709cog0902_1).

---

## Regla de producción

Estructura condicional que vincula condiciones con una conclusión o acción:

```text
SI alerta(s) Y verificado(s) Y monitorea(s,x)
ENTONCES sospechaContaminacion(x)
```

En un sistema de producción, un motor detecta reglas aplicables y administra el orden de ejecución. Las reglas facilitan explicación local, pero sus interacciones pueden crecer rápidamente.

**Relacionado con:** encadenamiento, motor de inferencia, agenda, sistema experto.

**Para aprender más:** tema **rule-based expert systems** y los experimentos de MYCIN.

---

## Representación distribuida

Representación en la que un concepto se codifica mediante un patrón distribuido entre muchas dimensiones o unidades, no mediante un único símbolo localizado.

Las representaciones distribuidas facilitan similitud y generalización, pero sus dimensiones no suelen corresponder directamente con conceptos editables por una persona.

**Relacionado con:** embedding, red neuronal, representación vectorial, arquitectura híbrida.

**Para aprender más:** Hinton, [Learning Distributed Representations of Concepts](https://repositories.cdlib.org/uc/item/79w838g1).

---

## Representación simbólica

Representación basada en símbolos discretos, estructuras y relaciones explícitas. Incluye lógica, reglas, marcos, ontologías y programas.

Permite manipulación y explicación estructurada, pero requiere decidir cómo se obtienen y fundamentan los símbolos.

**Relacionado con:** símbolo, grounding, lógica, arquitectura neuro-simbólica.

**Para aprender más:** McCarthy, [Programs with Common Sense](https://www-formal.stanford.edu/jmc/mcc59/mcc59.html).

---

## Representación vectorial o embedding

Asignación de una entidad, palabra o relación a un vector de números:

$$
e(x)\in\mathbb{R}^d
$$

La geometría del espacio permite medir similitud y recuperar elementos cercanos. Algunos métodos de grafos representan relaciones como transformaciones; TransE aproxima un triple válido mediante $\mathbf{h}+\mathbf{r}\approx\mathbf{t}$.

Un embedding conserva regularidades aprendidas, pero no garantiza verdad, causalidad ni cumplimiento de restricciones.

**Relacionado con:** representación distribuida, similitud, grafo de conocimiento, TransE.

**Para aprender más:** Bordes et al., [Translating Embeddings for Modeling Multi-relational Data](https://proceedings.neurips.cc/paper/2013/hash/1cecc7a77928ca8133fa24680a88d2f9-Abstract.html).

---

## Restricción de integridad

Condición que una base debería satisfacer para conservar coherencia operacional o semántica. Ejemplo:

$$
\neg\big(liberada(x)\land bloqueada(x)\big)
$$

Si la restricción se viola, la arquitectura debe decidir si rechaza la actualización, registra el conflicto o solicita revisión.

**Relacionado con:** consistencia, validación, regla, gobernanza.

**Para aprender más:** tema **database constraints, SHACL y validación de grafos RDF**; véase [SHACL, W3C](https://www.w3.org/TR/shacl/).

---

## Semántica

Relación entre las expresiones de un lenguaje y aquello que significan bajo una interpretación. Define cuándo una afirmación se considera verdadera y qué conclusiones se siguen de ella.

Dos archivos pueden tener la misma sintaxis y asignar significados distintos a una propiedad. Compartir formato no basta para compartir semántica.

**Relacionado con:** sintaxis, interpretación, entailment, pragmática.

**Para aprender más:** [RDF 1.1 Semantics](https://www.w3.org/TR/rdf11-mt/).

---

## Sintaxis

Reglas que determinan qué expresiones están bien formadas. En RDF, Turtle y JSON-LD son formas concretas de serializar estructuras; en lógica, la sintaxis define predicados, variables y conectores permitidos.

Una expresión sintácticamente válida puede ser falsa, contradictoria o inútil para una tarea.

**Relacionado con:** semántica, serialización, lenguaje formal.

**Para aprender más:** tema **formal syntax versus model-theoretic semantics**.

---

## Slot o ranura

Campo de un frame que representa una propiedad o relación. Puede contener un valor, un tipo esperado, una restricción, un valor por defecto o un procedimiento asociado.

Ejemplo: el frame `Inspección` puede incluir las ranuras `activo`, `responsable`, `fecha`, `evidencia` y `resultado`.

**Relacionado con:** frame, atributo, valor por defecto, esquema.

**Para aprender más:** Minsky, [A Framework for Representing Knowledge](https://dspace.mit.edu/entities/publication/0eca0164-cb5f-42de-8c86-43f54b23306d).

---

## Subsunción

Relación mediante la cual un concepto es más general que otro. Si toda pista es un activo crítico:

$$
Pista\sqsubseteq ActivoCritico
$$

entonces `ActivoCritico` subsume a `Pista`. Los razonadores de lógicas descriptivas utilizan subsunción para construir jerarquías de clases.

**Relacionado con:** lógica descriptiva, clase, ontología, clasificación.

**Para aprender más:** tema **concept subsumption and ontology classification**.

---

## Supuesto de mundo abierto

Supuesto según el cual la ausencia de una afirmación no implica que sea falsa. Si no se conoce el responsable de una inspección, el sistema conserva el valor como desconocido.

Es común en integración de conocimiento distribuido, donde ninguna fuente se considera completa.

**Relacionado con:** RDF, OWL, incompletitud, negación.

**Para aprender más:** [OWL 2 Primer](https://www.w3.org/TR/owl2-primer/) y el tema **open-world assumption**.

---

## Supuesto de mundo cerrado

Supuesto según el cual los hechos que no aparecen en una base completa pueden tratarse como falsos. Es frecuente en sistemas transaccionales y consultas de bases de datos.

Sólo resulta seguro cuando la cobertura de la base está controlada. No encontrar un incidente en una fuente parcial no demuestra que nunca ocurrió.

**Relacionado con:** negación por falla, base de datos, razonamiento no monotónico.

**Para aprender más:** tema **closed-world assumption and negation as failure**.

---

## Trazabilidad

Capacidad de reconstruir el recorrido entre evidencia, transformación, inferencia y decisión:

```text
fuente → hecho → regla → conclusión → acción
```

La procedencia describe el origen de cada elemento; la trazabilidad permite seguir la cadena completa y reproducirla.

**Relacionado con:** procedencia, explicación, auditoría, versión.

**Para aprender más:** tema **lineage, provenance and decision audit trails**.

---

## Tratabilidad

Propiedad práctica relacionada con el tiempo y memoria necesarios para resolver un problema. Un lenguaje puede ser decidible y aun así resultar demasiado costoso para cierta escala o latencia.

La selección de perfiles, restricciones sintácticas e inferencia aproximada busca conservar las capacidades necesarias con costos manejables.

**Relacionado con:** expresividad, complejidad computacional, decidibilidad, perfil OWL.

**Para aprender más:** [OWL 2 Web Ontology Language Profiles](https://www.w3.org/TR/owl2-profiles/).

---

## Triple

Unidad de afirmación con tres componentes:

```text
sujeto — predicado — objeto
```

Ejemplo:

```text
Pista09 — tieneSensor — SensorS1
```

En RDF, el sujeto es una IRI o nodo en blanco; el predicado es una IRI; el objeto puede ser una IRI, un nodo en blanco o un literal.

**Relacionado con:** RDF, grafo, entidad, predicado.

**Para aprender más:** sección [RDF Triples](https://www.w3.org/TR/rdf-concepts/#section-triples).

---

## Valor por defecto

Valor o conclusión utilizada mientras no exista evidencia contraria. Permite representar expectativas ordinarias sin enumerar todos los casos.

Los valores por defecto requieren mecanismos de excepción. Si se asume que un activo disponible puede asignarse, una inspección vencida debe retirar esa conclusión.

**Relacionado con:** frame, razonamiento no monotónico, excepción, revisión de creencias.

**Para aprender más:** tema **default logic** y [Non-monotonic Logic, Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/logic-nonmonotonic/).

---

## Vocabulario controlado

Conjunto administrado de términos y definiciones para describir un dominio de forma consistente. Puede incluir sinónimos, códigos, jerarquías y reglas de uso.

Es menos expresivo que una ontología formal, pero ayuda a reducir ambigüedad y preparar interoperabilidad.

**Relacionado con:** taxonomía, ontología, terminología, interoperabilidad semántica.

**Para aprender más:** tema **controlled vocabularies, taxonomies and thesauri**.

---

## Referencias generales

- Brachman, R. J. y Levesque, H. J. *Knowledge Representation and Reasoning*. <https://www.cs.toronto.edu/~hector/Papers/krbook.pdf>
- Brachman, R. J. y Schmolze, J. G. (1985). “An Overview of the KL-ONE Knowledge Representation System”. <https://doi.org/10.1207/s15516709cog0902_1>
- Gruber, T. R. (1993). “A Translation Approach to Portable Ontology Specifications”. <https://tomgruber.org/writing/ontolingua-kaj-1993.pdf>
- Minsky, M. (1974). “A Framework for Representing Knowledge”. <https://dspace.mit.edu/entities/publication/0eca0164-cb5f-42de-8c86-43f54b23306d>
- van Emden, M. H. y Kowalski, R. A. (1976). “The Semantics of Predicate Logic as a Programming Language”. <https://maarten.vanemden.com/Publications/kowVE.pdf>
- W3C. *RDF 1.1 Concepts and Abstract Syntax*. <https://www.w3.org/TR/rdf-concepts/>
- W3C. *OWL 2 Web Ontology Language*. <https://www.w3.org/TR/owl-overview/>

### Nota de uso académico

Las definiciones se simplificaron para facilitar su uso en el curso. Cada formalismo posee variantes, supuestos y limitaciones que deben revisarse antes de emplearlo en un sistema real.
