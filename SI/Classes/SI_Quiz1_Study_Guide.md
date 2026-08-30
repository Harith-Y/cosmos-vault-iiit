# Spatial Informatics (GS2.401) — Quiz 1 Study Guide

**Course:** Spatial Informatics, IIIT Hyderabad
**Instructors:** Dr. R. C. Prasad and Dr. Kuldeep Kurte (Lab for Spatial Informatics)
**Covers:** 31 Jul, 4 Aug, 7 Aug, 11 Aug, 14 Aug, 18 Aug, 21 Aug
**Syllabus block for Quiz 1:** Introduction → Spatial Data and its applications → Data Collection & error corrections

> How to use this: Sections 1–3 are the "Introduction" lecture. Sections 4–9 are "GIS Data Models" (Classes on 4/7/11 Aug). Sections 10–17 are "Spatial Data Collection" (Classes on 14/18/21 Aug). Section 18 is rapid-revision tables. Section 19 is a self-test question bank with answers.

---

## PART A — INTRODUCTION TO SPATIAL INFORMATICS (31 July)

### 1. What is Spatial Informatics?

**Spatial** + **Informatics**. Two halves:
- **Spatial** = the data has a location component (where things are on/near the Earth's surface).
- **Informatics** = the *extraction of information from that data for an application*. Not just collecting data — storing it, cleaning errors, and running analysis/algorithms on it to answer a question.

Course tagline: **"Everything is Spatial."**

**Key distinction the instructor pushed:**
- Collecting satellite images, maps, GPS points is only the raw input.
- The *informatics* part is: routing algorithms (shortest path), density of points-of-interest, spatial patterns, prediction. It is about **data + analysis together**.

**Two views of whether data is "spatial":**
- **Semantic view:** an Excel sheet of house names *could* be linked to locations, so it "is" spatial in principle.
- **Systems view:** if the location is **not explicitly encoded** (no coordinates, no polygon of the city), the system cannot use it — so it is *not* spatial from a systems perspective.
- Conclusion: whether data counts as spatial **depends on the application and how the data is stored.**

### 2. Location Is Important — and Spatio-Temporal

**"Something always happens somewhere."** Knowing *where* something happened helps you understand:
- **What** happened, **When** it happened, **How** it happened, **Why** it happened.
- Straightforward: *what / when / where*. Harder and more valuable: *why / how* (cause–effect, influencing factors nearby).

**Location data in daily life** (memorize this list — classic MCQ fodder):
Navigation, real-time traffic, weather forecast for *your* location, sharing live location, food delivery, ride-sharing, fitness tracking (GPS run paths), "find nearby places" (ATM, hospital, fuel), emergency services, banking/security (fraud = login from a new location).

**Three questions almost every digital service answers:**
1. **Where am I?**
2. **What is around me?**
3. **How do I get there?**

**Spatial data is inherently spatio-temporal.** Every activity we do carries *both* location and time. You cannot cleanly separate them.
- Example: a photo's metadata carries **location AND timestamp**.
- Example: GPS logs of a city bus every 10 seconds → location is explicit, time is explicit → **spatio-temporal**.
- Minkowski (1905): *"space by itself and time by itself are doomed to fade away… only a union of the two preserves an independent reality."*
- The "space-time aquarium" (Parkes & Thrift 1980) diagram: a person's daily trajectory drawn as a path rising through a vertical time axis (home → school → shop → home).

**Classify the data (worked examples from the slides):**
| Use case | Classification | Why |
|---|---|---|
| Daily electricity bills for 5,000 households, 2025 | **Temporal / non-spatial** (attribute) | Time series, no explicit location |
| GPS logs of city buses every 10 s | **Spatio-temporal** | Explicit location + time |
| Customer DB: name, age, income, yearly spend | **Non-spatial** | No location encoded |
| Satellite scans a river basin every month in monsoon | **Spatio-temporal** | Repeated imagery of a place over time |
| Police records: locality + exact date/time of crime | **Spatio-temporal** | Locality (coarse location) + time |
| City land-use map from a one-time 2018 survey | **Spatial** (static) | Location, essentially no time dimension |

### 3. Cognitive / Mental Maps

- We all carry a **cognitive (mental) map** of environments we know. *"Your mental map of a place represents your awareness about that place."*
- When you direct a friend to a canteen, you give **specific pointers** (roundabout, turn right, 100 m) — not every tree. You abstract to the relevant landmarks and route.
- Mental maps **vary person to person** — they depend on experience and familiarity with the place.
- There is a need to get this spatial awareness into a **digital form** so a system can process it → motivation for GIS.

### 3a. Types of Geographic Questions GIS Answers

Six categories (know these — a "match the question to the type" item is likely):
1. **Geographic location** — Where is it? Why is it here/there? How much of it is here?
2. **Geographic distribution** — Local or global? Clustered or dispersed? Where are the boundaries?
3. **Geographic association** — What else is near it? What occurs with it? What is absent in its presence?
4. **Geographic interaction** — Is it linked to something else? Nature of the association? How much interaction between locations?
5. **Geographic change** — Has it always been here? How has it changed over time and space? What drives its diffusion/contraction?
6. (These map onto the layered/analysis workflow later.)

### 3b. History of Spatial Analysis & GIS

- **John Snow, 1854, Soho, London — cholera outbreak.** 500 deaths in 10 days, one neighbourhood. Prevailing theory: cholera is *airborne*. Snow plotted deaths on a **street map** as a spatial bar chart (count of deaths per house). The cluster pointed to **one water pump** (Broad Street). Two water companies served the area with different intakes; the dense cluster was served by the contaminated supply. Removing the pump handle helped end the outbreak.
  → **First real use of spatial analysis in epidemiology — decades before the term "GIS" existed.**
- **Roger Tomlinson — "father of GIS."** ~1960, built the first true operational GIS (Canada Geographic Information System) for regional/land-use planning. First published the term *"geographic information system"* in his paper *"A Geographic Information System for Regional Planning."*
- **Survey of India** — national mapping organisation since the 18th century; detailed authoritative maps (buildings, electrical lines, streams), high cost, statutory mandate.
- Key GIS milestones: British Ordnance Survey begins 1747; Great Trigonometrical Survey of India 1802–1871; Snow's map 1854; US Census DIME 1960s; ESRI founded 1969; ARC/INFO 1980s.

### 3c. Evolution of Geospatial Technology (5 eras — likely a sequencing question)

| Era | Period | Characteristics |
|---|---|---|
| 1. **Field survey & analog mapping** | Pre-1990s | Field measurements, GPS/total stations, radiometers, **paper maps**. Data shared as paper, then tapes/CDs by courier. |
| 2. **Sensing systems & digital image processing** | 1990s | Aerial photogrammetry, **remote sensing** satellites, digital data models, **change studies** (forest degradation, urban sprawl). Data on tapes/discs. |
| 3. **Digital maps — desktop to web** | 2000s | CAD, GIS, **interactive maps**, web mashups. Static maps became interactive: pick & choose the subset you want, download only that. |
| 4. **Geo Services** | 2010s | **Location as a variable**, consumerisation of maps, **standard web services (WMS, WFS, WCS, CSW)**, interoperability. You don't download data — you send a region+time, the provider processes remotely and returns the output (e.g. "change detection as a service"). |
| 5. **GeoAI** | 2020s+ | Spatio-temporal data science, AI/ML/deep learning, **real-time & predictive** insights. You write a query in **natural language**; a geospatial agent decides which data, subsetting, model, and runs it. |

Overall arc: *Measurements & Maps → Digital Data → Web & Services → Users & Communities → Intelligence & Impact.*
"Better Data → Better Insights → Better Decisions → Better World."

### 3d. Sources of Spatial Data (6 — memorize with the "key idea")

1. **Remote Sensing (Satellite & Aerial)** — Sentinel/Landsat for floods, crops, urban growth; drones for high-res site mapping. *Key idea: synoptic view, repeated observations, large-area coverage.*
2. **GNSS / GPS** — tracks from phones, vehicles, delivery fleets, wildlife collars, fitness apps. *Key idea: point locations, trajectories, high temporal resolution.*
3. **Survey & Field Data** — borewells, trees, buildings via handheld GPS; geotagged household surveys. *Key idea: high accuracy, but sparse and costly.*
4. **Administrative & Government Data** — census aggregated at village/ward/district; land records, cadastral maps, zoning. *Key idea: authoritative, structured, often spatially aggregated.* Only specific authorities (e.g. Survey of India) may draw & publish boundaries.
5. **Sensors & IoT Networks** — weather stations, air-quality sensors; farm sensors (soil moisture, humidity, temperature) reporting via a local station (star topology) to a central server. *Key idea: fixed locations + continuous time → spatio-temporal streams.* Traction ~2010 onward.
6. **Crowdsourced / Volunteered Geographic Information (VGI)** — OpenStreetMap roads & buildings; geotagged social-media posts during disasters; Google Maps traffic reports / hazard reports added by users; Waze-style crash/slowdown reports. *Key idea: large-scale, dynamic, variable quality.* Here the **data consumer is also the data source** — the provider only supplies the platform. **OpenStreetMap** = community-driven equivalent of Google Maps; anyone can digitize a missing feature; moderators verify before it's published for all.

**Pokémon GO case study** — a game that became one of the largest **crowdsourced geospatial data collection platforms**: player GPS + movement + visited points of interest + AR scans of real-world objects → movement/density heatmaps, pathways, POIs. Data is anonymised/aggregated; the same company (Niantic, ex-Google) monetises the collected spatial data.

### 3e. Layered Architecture / Map Layers ("crux of how we visualize geospatial data")

- The real world is represented as an **overlay of thematic layers**, each layer = one theme (customers, streets, parcels, elevation, land use…).
- **You do not mix feature types in one layer.** Customers are **points**; streets are **lines**; parcels/regions are **polygons**. Different geospatial **data types** → stored separately, at different layers, with their own theme.
- Detail also differs by layer — land-usage data is pixelated/abstract; parcels are crisp. *"One kind of information can be represented one way but not another."*
- A **line** structure that represents a street **cannot** represent rainfall/temperature — those are *amorphous/continuous* phenomena needing a different representation; streets are *discrete*.

### 3f. Geometry — the Fundamental Concept

All representations are built on **geometry**: **Point, Line, Polygon** (+ combinations).
- **Point** — feature too small to be a line/area (SBI ATM). Recorded as an (x, y) pair.
- **Line** — feature too narrow to be an area (IIIT main road, River Ganges). Ordered series of (x, y).
- **Polygon** — closed area (football ground, District of Hyderabad). First point = last point.
- **Multi-polygon** — one geometry made of several polygons treated as a unit. Example: **India including Andaman & Nicobar / Lakshadweep islands** — mainland + islands = one multi-polygon; an intersection/selection operates on the whole thing as a single geometry.
- **Dimension:** an *area* consists of *lines* (1-D), which consist of *points* (0-D), which consist of a *coordinate pair*.

### 3g. Map Components (every map you produce must have these)

Essential elements — spotting what's *missing* on a map is a classic question (the Cyclone Michaung map example):
- **Title**
- **Legend** (what the symbols/colours mean)
- **Scale** (bar scale — without it you can't judge area/distance)
- **North arrow / direction** (the element most often forgotten)
- Creator/source information, coordinate grid, inset locator map.
- Instructor's rule: **never just take a screenshot** — generate a proper map with at least legend + scale + north + title.

### 3h. What Do We Do With Spatial Data? (4 capability levels)

1. **Visualize / depict** — draw the features (static map is fine). E.g. show location of ATMs, River Ganges, Hyderabad district.
2. **Query / locate / identify** — interactive; extract more info about a location. "Give me the population density at this point," "capacity of this building." Static maps can't do this.
3. **Analysis** — spatial relationships, cause–effect, co-occurrence, heat maps of movement → popular places, **Urban Heat Island** and its spatial factors.
4. **Spatial Modelling** — build a mathematical model to **predict / simulate**: cyclone trajectory, disease-spread modelling, urban-sprawl modelling.

### 3i. GIScience vs GISystems vs GIServices (Longley et al. 2001)

| Term | Focus |
|---|---|
| **GI Science** | The *science*: query algorithms, spatial patterns, data mining, analysis & modelling, estimation. From geographers + scientists. |
| **GI Systems** | The *tools/tech*: how you **store and process** the data (database vs shapefile), formats, data structures. |
| **GI Services** | The *data & services* delivered to users; you don't worry about storage/formats, only the capability/service provided. |

They cannot be isolated — you need all three, hand in hand. "Data & More Data" flows into GI Services.

### 3j. Application Glimpses (know one line each)

- **LULC mapping (Bhuvan, NRSC/ISRO web service)** — Land Use / Land Cover.
  - **Land cover** = physical/natural features (forest, water). **Land use** = anthropogenic / what we built it for (built-up, agriculture).
  - Interactive: click a polygon → returns feature ID, area, description. Pan the map → statistics update.
  - A **water body changes size seasonally** (bigger in rains, smaller in summer). A published map is *one snapshot* — so you must decide (from the science) whether to map post-monsoon extent, average, etc.
- **COVID-19 dashboard (Johns Hopkins)** — bubble map: bubble **centre = location**, bubble **radius = severity (number of cases)**. Naively plotting every case point makes no pattern; you must intelligently choose which dimensions to show and which to suppress. (Same idea as Snow's cholera bars.)
- **Urban Sprawl Analysis** — Landsat imagery for 1995/2005/2015/2025 → preprocess + Random Forest classification → 4 LULC maps → quantitative (transition matrix, Shannon entropy, patch density, compactness ratio), qualitative (UEI typology), inferential (KS test) → zonal & directional analysis. *Why?* Urban development authority policy (e.g. "new airport in 10 years") drives growth; analysis tells policymakers whether growth follows policy and whether zoning is needed to contain uncontrolled sprawl.
- **Digital Twin** — a virtual replica of the physical world built on a GIS foundation. Key characteristics: **geospatial**, **time-aware** (historic/current/future states, not just a 3-D model), **scalable** (streams lots of real-time sensor data). E.g. a digital twin of Boston integrating zoning, transport, public safety.

---

## PART B — GIS DATA MODELS (4 Aug, 7 Aug, 11 Aug — "Class 2")

### 4. GIS and Data Models — Fundamentals

**GIS** = a database management system in which the data is **geographic information**, supporting: **capture, edit, display/visualize, validate, manipulate (analysis), and edit/store** the data. (The whole course maps to: capture → display → manipulate → edit/model.)

**A GIS data model is a model of the earth.** The essential job of spatial data is to **subdivide the earth's surface into entities/objects that can be characterized.**

Components of a geographic feature:
- **Spatial data** — the geometry / location.
- **Non-spatial data (attribute data)** — the descriptive table records tied to each feature.
- These two are **kept in separate files**, linked by a **DBMS** (e.g. point location (x,y) in one table; "depth" and "amount" attributes in another, linked by Point No).

### 4a. Spatial Data Types (by phenomenon — memorize the examples)

- **Continuous:** elevation, rainfall, ocean salinity. *Amorphous, varies smoothly, no natural boundary* → needs raster.
- **Areas:**
  - **Unbounded:** land use, market areas, soils, rock type (fuzzy transitions — you can't draw a hard line where ocean salinity or a rainfall pattern "ends"; "something very vast which is changing").
  - **Bounded:** city/county/state boundaries, ownership parcels, zoning (crisp closed borders).
- **Networks:** roads, transmission lines, streams.
- **Points:**
  - **Fixed:** wells, street lamps.
  - **Moving:** cars, fish, deer.

### 4b. Levels of Abstraction — Reality → Conceptual → Logical → Physical → (Computer)

*Increasing abstraction going down. Top is human-oriented, bottom is computer-oriented.* Using the **road** example:

| Model | What it does | Road example |
|---|---|---|
| **Reality** | The actual complex real world | An actual road: centre line, edge/width, shoulder, lanes, one/two-way, speed limit, pavement, underground structure, intersections, dates. |
| **Conceptual model** | **Human-oriented.** Identify the geographic **features** and the **relationships** between them. | Road decomposed into: Line (centre line, network → intersection), Area (main section, shoulder), Attributes (speed limit, no. of lanes). "What is the relationship between entities" (e.g. distance between two, borders on, comprises). |
| **Logical model** | Choose the **representation** — vector vs raster; define tables/records and links. | Road{Line-id, Area-id, Road No., Name} → Line{Line-id, S-Node, E-Node, Vertices, Length} → Vertices{x,y…}; Area{Area-id, Left edge, Right edge, Pavement, Area}. |
| **Physical model** | How it is actually **stored** — files, records, database structures on disk. | Database "Road" holding files Road / R-line / R-area; File Road = records (Record 1: Line-id, Area-id, Road No., Name …); File R-line = records (S-Node, E-Node, Vertices, Length …). |
| **Computer model** | Making the system understand "this is F, this is O" — comes from the physical model. | — |

Mnemonic: **R-C-L-P** (Reality, Conceptual, Logical, Physical).
- Conceptual = **features + relationships**
- Logical = **representation (vector/raster) + tables**
- Physical = **storage / database design**

### 5. Types of Geographical Data Models Used in GIS

| Data model | Application |
|---|---|
| **Computer-Aided Design (CAD)** | Simple mapping; engineering drawings. **No relationships between objects.** |
| **Graphical (non-topological)** | Simple maps / cartographic representation without relationships. |
| **Image** | Image processing & simple grid analysis. Grid of pixels (satellite images). |
| **Raster / Grid** | **Spatial analysis and modelling.** Grid of cells. |
| **Vector / Geo-relational / Topological** | **Operations on vector geometric features.** Points, lines, polygons **with relationships**. |
| **Network** | **Network analysis** (connected systems — roads, rivers). |
| **Triangulated Irregular Network (TIN)** | **Terrain analysis** (3-D surface from triangles). |
| **Object** | Operations on all entity types — "smart" geographic objects with properties and behavior; good for 3-D. |

### 6. Vector Data Model

**Definition / properties (frequently tested):**
- One model for representing geographic space.
- **Spatial locations are EXPLICIT** (stored coordinates).
- **Relationships between entities are IMPLICIT** (must be derived / built as topology).
- Provides **precise positioning** of features.
- Based on **analytical geometry**; builds complex representations from primitives: **points, lines, areas.**
- Summary definition: *a vector is a quantity with a **starting coordinate** and an associated **displacement and direction**.*

**Primitives:**
- **Point (0-D):** feature too small for line/area; stored as (x, y) + attribute table. A **node** is a *topological* point where two or more arcs connect. Examples: wells, lamp posts, settlements, sampling stations.
- **Line / Arc (1-D):** feature too narrow for an area; ordered (x, y) series; stored by first & last node + attributes. Examples: roads, rivers/drainage (stored with FNODE#, TNODE#, LPOLY#, RPOLY#, LENGTH).
- **Polygon (2-D):** homogeneous area; **closed** sequence of lines (first point = last point). Unlike a **polyline** (open sequence of line segments), a polygon is always closed. Geometric attributes like **area and perimeter** are derived easily. Examples: forest-type polygons, administrative regions.

### 6a. Attribute (Non-spatial) Data Types — MEASUREMENT SCALES (very likely on quiz)

Two broad types: **Qualitative (nonnumeric)** and **Quantitative (numeric)**.

| Scale | Type | Meaning | Operations that make sense | Example |
|---|---|---|---|---|
| **Nominal** | Qualitative | Names/categories, **no order** | Equality only (=, ≠); count | Land-cover class, gender, "yes/no", city name |
| **Ordinal** | Qualitative | **Ranked** order, but gaps not meaningful | Order (<, >), ranking | Low / moderate / high biodiversity; "good/better/best"; education level |
| **Interval** | Quantitative | Numeric, ordered, equal intervals, **no true zero**; differences meaningful but **ratios not** | +, −  (difference) | Temperature in °C; a year/date. "Twice as much" is meaningless |
| **Ratio** | Quantitative | Numeric with a **true zero**; both differences AND ratios meaningful | +, −, ×, ÷; "twice as much" | Rainfall (mm), population, income, area, distance |
| **Cyclic** | Special | Direction-type values that wrap around | Circular statistics | **Wind direction, slope aspect** |

Worked example (from slide Table 7.2): a table of 4 people — *Age* = **Ratio**, *Sex* = **Nominal**, *Ethnicity* = **Nominal**, *Education* = **Ordinal**, *Income* = **Interval** (as marked on the slide). Note: the course generally treats income as ratio, but memorize the slide's labels for this specific table.

Focus: the course mostly focuses on **nominal and ratio**; **cyclic** (wind direction, aspect) doesn't fit any of the four and is a favourite "gotcha."

### 6b. Data Symbolization (Bertin's graphical variables)

You can vary point/line/area symbols by: **size, value (lightness), grain (texture), colour, orientation, shape.** Match the visual variable to the data type (e.g. size for quantities, colour hue for nominal categories).

### 7. Vector Data Structures / Models (7 Aug — how vectors are actually stored)

Two families:

**A. Non-topological**
1. **Spaghetti** — every feature stored independently as a list of coordinates. A shared boundary between two polygons is **stored twice** (once for each polygon) → **redundancy**, no relationships. Format: `A, 6` (polygon id, #vertices) then each vertex `1,3 / 1.8,2.6 / …` then repeat first vertex to close; `B, 1` (point) `4,4`; `C, 4` (line) `1,2 / 3.5,2 / …`.
2. **Vertex dictionary** — two files: File 1 = every unique vertex once with (X, Y); File 2 = each feature as an ordered list of vertex IDs (`polygon A: i, ii, iii, iv, v, vi`). **No coordinate duplication**, BUT **still no topology.**

**B. Topological**
3. **DIME (Dual Independent Map Encoding)** — developed by the **US Census Bureau, 1968**, for demographic analysis (storing addresses & urban maps). Line segments assumed **straight**; curves = a sequence of straight segments. Each segment stored with **three essentials**: a **segment name**, **node identifiers** for the *from* and *to* endpoints, and **identifiers for the polygons on the left and right** of the segment. Stores map vectors **non-redundantly** — great for defining boundaries of **adjacent polygons** (the shared segment is stored once, with left-poly and right-poly recorded).
4. **Arc–Node structure** — the **dominant vector structure in modern GIS.** Often called an **"intelligent data structure"** because spatial relationships are easily derived. Incorporates **network relationships along with coordinate measurements** (Chrisman 1997). Typically stored as several linked tables:
   - **Node table:** Node ID, Easting, Northing.
   - **Arc table:** Arc ID, From-Node, To-Node, **Left-Poly, Right-Poly**.
   - **Polygon table:** Polygon ID, Arc list.
   - Plus feature-attribute tables for nodes, arcs, polygons.
   - Coordinates of vertices for each arc are stored once; polygons are defined by their bounding arcs; adjacency (which polygons share an arc) and connectivity (which arcs meet at a node) are explicit.

**Topology** = the explicit storage of spatial relationships: **adjacency** (which polygons share an edge), **connectivity** (how lines link at nodes), **containment** (point inside polygon). Needed for network routing, watershed delineation, overlay, and error-checking (gaps/overlaps). *"The computer cannot see the real world, so relations like belong to, comprise, located in/on, border on must be specified explicitly."*

**Planar enforcement** — a topology rule: polygons in a coverage must not overlap and must not leave gaps; every point in the plane belongs to exactly one polygon.

### 8. Raster Data Model (11 Aug)

**Definition:** A **grid** defines geographic space as a **matrix of identically-sized square cells**. Each **cell holds a single numeric value** measuring a geographic attribute (e.g. elevation) for that unit of space.

**Structure / characteristics:**
- Defined by: **number of rows, number of columns, cell size (resolution), origin (X,Y of a corner), NODATA value.**
- ASCII raster header: `ncols`, `nrows`, `xllcorner`, `yllcorner`, `cellsize`, `NODATA_value` (default −9999), then the grid of values.
- Typically **8 bits per cell → 256 possible values (0–255)** (though continuous data can be float).
- **Single value per cell**; each layer = one attribute (one "spreadsheet"). A **look-up table** maps codes to meaning (1 = forest, 2 = cultivated, 3 = water, 4 = bare rock).
- Spatial relationships are **IMPLICIT** because the grid is regular — you don't store them. **Adjacency & connectivity** (4-connectivity / 8-connectivity) are **derived from the array** (e.g. "minimum value around this cell," fire-spread day-by-day).
- Coordinate of a pixel is implied by its row/column + origin + cell size.

**Raster types:** satellite imagery, Digital Elevation Model (DEM), scanned map / USGS DRG, scanned soil-line drawings.

**Classification of a raster** — assign each pixel to a class (e.g. elevation 0–100 = 1, 101–500 = 2, >500 = 3). Result is a **classified raster** storing a single integer class code per cell; reduces data size; displayed with distinct colours ("unique values" palette). Original continuous values are lost.

**Visualization:**
- Single-band **grayscale** for elevation (darker = lower).
- **Pseudo-colour** — apply a colour palette to a single grayscale band (low = dark, high = bright) to reveal subtle variation; also used for indices like NDVI.
- **False-colour composite** — assign 3 bands to R/G/B display channels; e.g. **Sentinel-2 B4(red)-B3(green)-B2(blue)** = true colour; NIR-Red-Green = false colour (healthy vegetation → bright red).
- Load `.qml` / `.sld` **style files** via Layer Properties → Style → Load Style to restore symbology.

### 8a. Raster Storage Formats — Band Interleaving (near-certain quiz item)

For a multi-band image (e.g. blue, green, red, NIR):
| Format | Ordering | Best for |
|---|---|---|
| **BSQ — Band Sequential** | Store the **entire first band**, then the entire second band, … | Processing **one band at a time** (e.g. a filter on just NIR) |
| **BIL — Band Interleaved by Line** | For **each line/row**: all bands' values for that line, then next line | **Line-by-line** processing; good compromise |
| **BIP — Band Interleaved by Pixel** | For **each pixel**: all bands' values together, then next pixel | **Per-pixel multi-band** math (e.g. **NDVI = (NIR−Red)/(NIR+Red)**) — most I/O-efficient |

### 8b. Raster Compression

- **Cell-by-cell array (conventional):** every pixel gets a value; **no compression** even when neighbours are identical. Typical for **float continuous surface** data (DEM).
- **Run-Length Encoding (RLE):** encode runs as (count, value) pairs. Row-by-row: `CCCCCBB…` → `5C 2B 1D …`. Example: 7×8 array = **56 entries** raw → **22 pairs (44 entries)** with RLE. **Lossless.** Works well when many neighbouring pixels **share a value** (low-res / classified data); **useless for DEM** or data where neighbours almost always differ.
- **Quadtree:** recursively subdivide the grid into NW/NE/SW/SE quadrants; stop subdividing where a block is homogeneous. Compact for data with large uniform regions.

**Compression principle:** compression works best on **redundant / repeated values** (low resolution, classified). **High-resolution data with many unique values compresses poorly.**

### 8c. Resolution vs Detail vs Storage (core trade-off)

- **Smaller pixel (finer resolution)** → captures **more spatial detail** BUT **many more pixels → much larger file, more processing.**
- **Larger pixel (coarser resolution)** → **less detail** (small features vanish, big lakes still visible) BUT **compact, fast.**
- Slide examples: 100 m vs 30 m vs 5 m of the same city; 1 km = low res, 4 m = high res, sub-metre/cm = ultra-high res.
- **Raster needs less processing than vector but consumes more storage.** Scanning sensors on satellites store data in raster natively.
- Raster **does not provide precise locational information** (DeMers 1997) — can seem undesirable for cadastral/legal work.

### 9. Vector vs Raster — Comparison & Conversion

**"Raster is faster, but vector is corrector."** — Joseph Berry

| Aspect | Vector | Raster |
|---|---|---|
| Location | Explicit coordinates; **precise at all scales** | Implicit (row/col); precision limited by cell size |
| Relationships / topology | Can be explicit → **good for network analysis** | Implicit in the grid; derived on the fly |
| Storage | **Compact** for discrete features (roads, boundaries) | Large, esp. high-res; but **simple data structure** |
| Best for | **Discrete** features, precise boundaries, cadastral/legal, networks | **Continuous** surfaces (elevation, temperature); quantitative modelling; **fast arithmetic/overlay** |
| Data mixing | one feature type per layer | can hold **both discrete and continuous** |
| Point / line / area | point = (x,y); line = ordered pts; polygon = closed line | point = 1 cell; line = connected cells (length); area = group of connected cells (shape) |
| Graphic output | more aesthetically pleasing; cartographic quality | grid-cell output usually not high cartographic quality |
| Analysis algorithms | complex, processing-intensive; topology is static → editing needs topology **rebuild**; needs **extensive data cleaning** | easy and fast computation; well suited to quantitative modelling |

**Vector advantages:** good entity representation, compact, explicit topology (network analysis), accurate at all scales, retrieval/updating/generalization of graphics & attributes possible, aesthetic output.
**Vector disadvantages:** each vertex stored explicitly; must be converted to topology (processing-intensive, needs cleaning); topology static → editing = rebuild; complex analysis algorithms limit large datasets; **continuous data (elevation) not well represented** — needs heavy generalization/interpolation.
**Raster advantages:** easy & fast computation; good for quantitative modelling (basic arithmetic); integrates discrete + continuous data.
**Raster disadvantages:** cell size fixes resolution; usually one attribute per layer; most input is vector → needs **vector-to-raster conversion**; output maps don't meet high cartographic standards.

**Inter-conversion (both lose something — "loss of data, reduction in accuracy"):**
- **Rasterization (V→R)** — **relatively easy.** Points → cells; line → sequence of cells; polygon → zone of cells. Introduces **pixelation / stair-step edges**, loses positional accuracy (a 1 m road forced into a 30 m cell is widened/displaced).
- **Vectorization (R→V)** — **much harder.** Polygonize contiguous same-value cells → polygons; may need simplification (smoothing jagged edges); can create noisy "speckle" polygons at high resolution.
- **Dominant / "winner-takes-all" rule** — when a cell is covered by several vector features, assign the value of the feature covering the **largest area** (or whose centroid falls in the cell). Works when one feature clearly dominates; misleading for mixed cells (40% residential / 35% commercial / 25% park all become "residential"). Alternative: fractional/proportional raster, or majority-vote with a threshold ("mixed" if none > 60%).

### 9a. Thematic Mapping & Attribute Classification (7 Aug)

**Why classify?** A map of raw district boundaries is uninformative; random colours are noise; **classifying districts by an attribute (e.g. literacy rate) reveals patterns.** Classification groups values into a few classes to simplify and expose spatial structure. Choosing the **number of classes** (2 vs 5 vs 9 ranges) trades detail against readability.

**Choropleth map** — *a thematic map in which polygon features are shaded/coloured by the value of an attribute.* Best for **rate/ratio/normalized** attributes (literacy %, population density people/km², forest cover %, rainfall mm, unemployment %).
**A choropleth requires TWO decisions:** (1) **which attribute** to map, and (2) **how to classify** the values.

**Classification methods** (know good-for / disadvantage of each):

| Method | How it works | Good for | Disadvantage |
|---|---|---|---|
| **Equal Interval** | Divide the value range into classes of equal width | Non-technical audiences; familiar units like % | If data is skewed/clustered, many features land in one class, others empty |
| **Pretty Breaks** | Like equal interval but rounds class limits to neat numbers (10, 20, 50, 100) | Readable legends, neat boundaries | Breaks may not match the data's natural distribution; can split clusters or merge dissimilar values |
| **Quantile (Equal Count)** | Each class has the **same number of features** | Emphasizing **relative position** (top 20%, middle 20%, bottom 20%) | Similar values can be split into different classes (exaggerates difference); wide value ranges can be lumped together (hides difference) |
| **Standard Deviation** | Classes defined by distance above/below the **mean** in SD units | Showing which features are **above/below average**; **normally distributed** data | Doesn't show actual values, only distance from mean; outliers skew the mean |
| **Natural Breaks (Jenks)** | Minimizes within-class variance, maximizes between-class variance (implied by "natural clusters" discussion) | Data with natural groupings | Class breaks are dataset-specific, hard to compare maps |

**Other thematic representations:**
- **Graduated symbols** — symbol size steps by class (e.g. population by CD block).
- **Proportional symbols** — symbol area **directly proportional** to the value (continuous, not classed).
- **Dot distribution map** — each dot = a fixed count (1 dot = 100 persons); density of dots shows distribution.
- **Isopleth / isoline map** — lines/bands of equal value over a **continuous surface** (contours, temperature, coffee production density).

---

## PART C — SPATIAL DATA COLLECTION (14 Aug, 18 Aug, 21 Aug — "Class 3")

### 10. Data Collection — Overview

- **One of the most time-consuming and expensive GIS tasks** — typically **15–50% of total project cost** (Kennedy & Guinn 1975: "a large portion of the investment will be in obtaining, converting and storing new data").
- GIS layer contents to collect: **Spatial data, Coordinate-system info, Attribute data, Metadata, Symbology.**
- Data can be **digital or analog**.
- **Main data sources for GIS:** existing reference & thematic maps (digital/hardcopy); ground survey & positioning; remote sensing; census/sampling, reports & publications.

**Data collection workflow (cycle):** **Planning** (type of data, required accuracy, access & storage, staff) → **Preparation** (obtaining data, redrafting, software) → **Digitizing** (data conversion) → **Editing / Improvement** (cleaning, maintenance) → **Evaluation** → back to Planning.

### 10a. Types of Data Collection

**Two broad types:**
1. **Data capture (direct collection)** — two capture methods:
   - **Primary:** **direct measurement** (new data collected for this purpose).
   - **Secondary:** **indirect derivation from existing sources** (data reused from earlier studies).
2. **Data transfer** — importing existing digital data from other sources.

Plus: capturing **attribute data** separately.

**Vector & raster capture techniques (know this 2×2):**
| | **Raster** | **Vector** |
|---|---|---|
| **Primary** | Digital remote-sensing images; digital aerial photographs | Survey (total station) measurements; GPS measurements |
| **Secondary** | Scanned maps; scanned photographs | Topographic surveys / digitized from maps |

### 11. Remote Sensing

**Remote Sensing Process (7 steps):** 1. Sun light → 2. Atmosphere → 3. Earth features → 4. Satellite/sensor → 5. Antenna/receiver → 6. Computer analyst → 7. Application.

- Sensors detect **reflected** radiation (from sunlight) and/or **emitted** radiation (thermal, from the object's own heat).
  - **Daytime:** both reflectance and emitted radiation occur.
  - **Night:** only **emitted (thermal)** radiation is observed.
- **Atmospheric effects** (clouds, scattering) add **noise** → lower the **Signal-to-Noise Ratio (SNR)**. Atmospheric conditions are the **dominant noise source** in RS.

**Spectral signatures / reflectance curves (know the shapes):**
- **Vegetation:** low reflectance in **visible red** (chlorophyll absorbs), **very high in near-infrared (NIR)** (leaf cell structure scatters NIR) → sharp "**red edge**."
- **Water:** strongly **absorbs NIR and SWIR**; very low reflectance overall; deep absorption dips around **1.4 µm** (and ~1.95 µm).
- **Soil:** gradual rise from visible to NIR; flatter curve; no NIR peak, no deep water-style valleys. Dry soil (5% water) reflects more than wet soil (20% water).
- Selecting the right **bands** (or building composites) enhances feature discrimination.

**True-colour vs false-colour composite:**
- **True colour:** sensor Red→display Red, Green→Green, Blue→Blue (mimics human vision).
- **False colour:** e.g. NIR→Red, Red→Green, Green→Blue. Healthy **vegetation appears bright red**, water dark, soil brown. In the single-band example: BLUE (0.4–0.5 µm), GREEN (0.5–0.6 µm), RED (0.6–0.7 µm), NIR (0.7–0.9 µm); sand/vegetation/water separate best in specific bands (water is very dark in NIR).

### 11a. Three Types of Resolution (near-certain quiz item)

| Resolution | Definition | Example |
|---|---|---|
| **Spatial** | Ground area represented by one pixel (ground sample distance) | 1 km = low res; 30 m = medium; **4 m = high res**; sub-metre / cm = ultra-high. Indian sensors: Cartosat-1 (500–850 nm PAN), LISS-IV, LISS-III, LISS-I, AWiFS, PAN (500–750 nm) |
| **Spectral** | **Number and width of wavelength bands** a sensor records | 3 bands (R, G, IR) vs many narrow bands (hyperspectral); visible / NIR / SWIR / microwave |
| **Temporal** | **Revisit frequency** — how often the sensor images the same location | Compare Hyderabad: MSS-1976, TM-1989, ETM-2001, AWiFS-2001; Andaman LISS-III Mar 1999 vs Feb 2005 → monitor urban expansion, forest change |
| *(Radiometric)* | Bit depth — number of brightness levels (8-bit vs 16-bit) | affects ability to distinguish subtle intensity differences |

**Application-driven sensor selection:** coarse + frequent revisit for large-scale monitoring; high-res multispectral or SAR for detailed mapping (agriculture, urban expansion, hydrology).

### 11b. Pre-processing (error corrections — the "error corrections" part of the syllabus)

Common problems: atmospheric noise, cloud cover, sensor distortion, geometric distortion (platform pitch/roll/yaw, Earth curvature), varying pixel sizes.
Corrections needed before analysis:
- **Geometric correction / georeferencing** — assign a coordinate system, correct sensor tilt & Earth curvature, align to a common projection. Older images have no embedded coordinates → use **Ground Control Points (GCPs)** from toposheets or **GPS / DGPS**.
- **Radiometric correction / normalization** — adjust for sensor differences, atmosphere, sun angle, season; convert DN → surface reflectance; histogram matching so multi-date images are comparable.
- **Atmospheric correction.**

**Change-detection workflow:** (a) define study area + required resolution → (b) acquire multi-temporal imagery → (c) preprocess & co-register/align → (d) classify or compute indices → (e) compare to quantify change.

### 12. Aerial Photography

- **SR (satellite RS) and AP (aerial photography) are technically similar** — the difference is in **capturing and interpretation.**
- AP normally collected with an **analog optical camera**, then **rasterized by scanning the film negative**.
- Cameras mounted in the **nose or underbelly** of an aircraft flying at **low altitude (3,000–9,000 m)**.
- May be **panchromatic or colour**; can be used as a **map or a photo**; suited to **detailed surveying & mapping.**
- Both satellite images and aerial photos must be **georeferenced** before use (toposheets, GCPs via GPS/DGPS).

### 12a. Platforms — Satellite vs Aircraft vs Drone (UAV)

Altitude bands: **Satellite ≈ 160–42,164 km**; **Aircraft ≈ 200–1,000 m** (some slides say up to a few km); **Drone ≈ up to ~120 m**.

| Platform | Coverage | Revisit | Spatial res | Atmospheric noise / issues |
|---|---|---|---|---|
| **Satellite** | Regional / global | Consistent (days–weeks); but **limited temporal res** | Coarse→high (30 m → sub-m); **limited** vs drone | Views through whole atmosphere → cloud cover, scattering, shadow; **low SNR** |
| **Aircraft** | Medium-scale | Mission-scheduled (not continuous); **repeat = expensive** | High (often <1 m) | Moderate atmospheric noise; **geometric distortion** from aircraft motion → needs orthorectification; moderate SNR |
| **Drone / UAV** | Small-area, fine-scale | On-demand, **cheap repeat** | **Very high (cm-scale)** | **Least atmospheric noise, no cloud cover** (flies below clouds), still shadow; **highest spatial res, high SNR**; limited by battery, regulations, small swath |

**Drone sensor payloads (know function + limitation):**
| Sensor | Function | Limitation |
|---|---|---|
| **RGB camera** | Visible light, high-res colour imagery | Daylight only |
| **Multispectral camera** | Multiple spectral bands → vegetation ID & classification (NDVI) | Limited spatial resolution |
| **IR / thermal camera** | Detects infrared radiation → temperature | Cannot detect geology directly; limited spatial resolution |
| **SAR** | Penetrates clouds & darkness → all-weather, day/night | Lower spatial resolution, complex processing |
| **LiDAR** | Laser pulses → **direct 3-D terrain model** | Affected by atmospheric conditions; costly |

### 13. LiDAR (18 Aug)

- **LiDAR = Light Detection And Ranging** (laser radar). **Active** sensor — emits its own light (laser) and detects the returned energy. Laser wavelength ≈ **1064 nm (near-infrared)**. Can be collected **day or night**.
- **System components:** aircraft-mounted **LiDAR scanner** + **GPS/IMU** on the platform + a **ground GPS base station**. The base station provides a high-accuracy GPS reference so systematic errors (satellite clock, atmosphere) are corrected → centimetre-level XYZ for each returned pulse. A standalone receiver on the platform alone would be far less accurate.
- Mission parameters example: flight height ~975 m AGL, swath ~594 m, ~1.5 m point spacing (~444,000 points/km²), 30% side overlap, ~30 km base-station radius.

**Multiple returns per pulse:**
- **First (early) returns** = highest surface hit — **canopy top, buildings, clouds/birds** → used for **canopy height models**, structure mapping, **DSM**.
- **Last return** = lowest surface hit — usually the **ground** → used to build a bare-earth **DEM/DTM**.
- Removing the first returns / non-ground returns strips buildings & vegetation to expose the topography.
- **Leaf-on vs leaf-off:** more ground returns penetrate a **deciduous** tree in leaf-off season; a **coniferous** tree blocks more year-round.

**From point cloud to surface models:**
- **DEM (Digital Elevation Model)** — bare-earth elevation (ground only).
- **DSM (Digital Surface Model)** — includes trees, buildings (raw LiDAR reflections from tops); used for vegetation canopy models, 3-D urban models.
- **DTM (Digital Terrain Model)** — bare earth, often with breaklines; supports derivatives: **contours, slope, aspect** (aspect = N/NE/E/…/flat).
- **TIN** — Triangulated Irregular Network built from the points (Delaunay-style triangles) → 3-D surface for terrain analysis.
- Ground points are interpolated (TIN, Kriging, IDW) onto a regular grid to make the DEM.

**LiDAR advantage:** much **higher spatial resolution** than wavelength-based passive RS; captures detailed elevation of buildings & terrain; sees the ground **under vegetation** where optical sensors fail.

**Error sources:** GPS positioning error, IMU drift, timing errors, atmospheric effects, sensor noise, misclassification of returns (mistaking a roof for ground), multi-path reflections, vegetation penetration.

### 14. Radar / SAR

- **RADAR** — active microwave sensor. **SAR = Synthetic Aperture Radar.**
- Certain (longer-wavelength) radar bands **penetrate clouds and rain** → data collection during **monsoon / cloudy** conditions, day or night.
- **Doppler Weather Radar** — reflectivity images (e.g. Hyderabad radar, max range ~250 km).
- **Polarization** — the antenna transmits and receives in horizontal (H) or vertical (V):
  - **Co-polarized: HH, VV** — sensitive to **surface roughness & geometry**; strong returns from smooth surfaces and oriented man-made structures (double-bounce from buildings/tree trunks).
  - **Cross-polarized: HV, VH** (transmit one, receive orthogonal) — dominated by **volume scattering** (tree canopies, crops), because complex 3-D targets rotate the polarization. Good for vegetation structure, moisture.
  - Combining polarizations (e.g. HV/HH ratio) → vegetation density, forest type, biomass, deforestation detection.
  - "HV" notation = **H transmit, V receive.**

### 15. Sonar / Bathymetry

- Underwater analogue of LiDAR: an acoustic pulse travels down, reflects off the seabed, returns to a hydrophone.
- **Distance = (speed of sound in water × two-way travel time) / 2.** Speed of sound ≈ **1500 m/s**, varies with temperature, salinity, pressure.
- Used for **bathymetry** (mapping ocean/lake floor) where optical & radar cannot penetrate.
- **Error sources:** sound-speed variability (bad T/S/pressure assumptions bias depth), **multipath** reflections (off surface/debris), wide beam angle → large footprint → averaging over rough terrain, rough seas & bubbles → scattering, instrument timing errors. Mitigate with CTD sound-speed profiles, narrow/multibeam systems, signal filtering, calibration against tide gauges.

### 16. Other Field / Mobile Collection

- **Digital field cameras & Mobile Mapping Systems (MMS)** — a vehicle with a **mobile laser scanner** or **digital camera array** + **GPS antenna + GPS receiver + INS (IMU) + DMI** (distance-measuring instrument) → produces a **LiDAR point cloud** or **geo-referenced street-level images** (street-view style).
- **Wireless Sensor Networks (WSN)** — many in-situ nodes (soil/leaf humidity, air temperature, moisture, pH, pollution, nutrients, pest) reporting to a cloud; smart-agriculture systems. Data is **fixed-location + continuous-time → spatio-temporal.**

### 17. GPS / GNSS (21 Aug)

**GPS = Global Positioning System.** Three segments:
1. **Space segment** — **24+ satellites** (21 in use + 3 spares), **6 orbital planes** (4 per plane), **altitude 20,200 km**, **~12-hour orbit**, 55° inclination, carrying **atomic clocks** (Hydrogen Maser).
2. **Control segment** — a **Master Control Station** (Falcon AFB, Colorado Springs) + monitor stations worldwide (Hawaii, Ascension, Diego Garcia, Kwajalein) + ground antennas. Continuously receives telemetry, checks satellite health, maintains precise timing.
3. **User segment** — receivers that decode satellite signals; select satellites, acquire signals, measure & track. Used by ships, aircraft, ground vehicles, individuals.

**How GPS works — RATE × TIME = DISTANCE:**
- **RATE** = speed of light ≈ **300,000 km/s** (GPS signals are radio/microwave).
- **TIME** = how long the signal takes to travel from satellite to receiver (satellite atomic clock timestamps transmission; receiver compares to reception time).
- Each measured distance (pseudo-range) puts you on a sphere around that satellite. Intersect **≥3** spheres (plus a 4th satellite to solve the receiver-clock bias) → **(X, Y, Z)** position. Related geometry idea from the slide: **triangulation / law of sines** using known satellite positions as triangle vertices and pseudo-ranges as sides.
- **Timing is critical: a 1 ms clock error → ~300 km position error** (0.001 s × 300,000 km/s). Nanosecond accuracy needed for metre-level positioning.

**Signal transmission problems (errors):**
- **Blocked signal** — obstruction; you need **≥3 satellites in unobstructed view** to fix a position → problems in **forests** and **urban areas with tall buildings**.
- **Multipath error** — signal reflects off buildings/terrain before reaching the antenna → wrong travel time. Modern receivers/antennas detect & reject reflected signals.
- Other error sources: satellite clock drift, ionospheric & tropospheric delay, ephemeris (orbit) errors.

**DGPS — Differential GPS:**
- A **base station at a precisely surveyed (known) location** receives the same satellite signals, computes its position, and finds the **error** (difference between measured and known). This error vector (satellite-clock + ionospheric + tropospheric + ephemeris + multipath components) is **broadcast as corrections** (often **RTCM** format) to nearby **rover** receivers.
- The rover subtracts the common-mode error from its own raw measurements → **centimetre-level** accuracy instead of several metres.
- Base and rover must be in the **same area** (errors must be common). Corrections can be real-time (radio/cellular/internet) or applied in **post-processing**.
- Slide's phrasing: *"two GPS operating at the same time to minimize the error."*
- **GPS applications:** navigation, topographic surveys, natural-resource management, other surveys; provides GCPs for georeferencing.

### 17a. Ground Surveying (primary vector capture)

- **Direct measurement** in the field: point coordinates, distances, elevations, angles, attribute data.
- Instruments: **theodolite** → **total station** (automatically logs data; sophisticated ones create vector point/line/polygon objects in the field with direct validation).
- A traverse: measured interior angles and side lengths between stations A–B–C–D–E.
- Data entry: **import** if already digital; else **manual entry**.

### 17b. Secondary Raster Data Capture

1. **Digital scanning** — scanned maps/documents used extensively as background maps and data stores (e.g. seismic zones of India map). Output quality depends on **source map quality** and the **scanning process** (spatial + spectral/bit-depth resolution).
2. **Rasterization** — vector → raster conversion (e.g. forest-type map of North Andaman).
3. **Spatial interpolation** — estimate the unknown value of a cell from **sample point values weighted by distance**. Input = point features → output = continuous raster surface. Methods: **IDW (simple)**, **Kriging (smart, statistical)**. Example: rainfall/precipitation surface from gauge points.
4. **Resampling / Grid aggregation** — change resolution (e.g. 10 m → 20 m → 30 m; 250 m → 1 km). Merges adjacent similar pixels; representative value = mean/median/mode. Also needed when changing coordinate systems. Resampling methods: **nearest-neighbour, bilinear, cubic**. Justified when the analysis only needs broad regional trends (e.g. a 30 m DEM is enough for watershed runoff; a 1 m DEM is wasteful).
   - **Resolution** = smallest ground distance a cell represents; **cell size** = physical dimension of the grid cell. Changing either requires resampling because the old pixel grid no longer aligns with the new grid.

### 17c. Secondary Vector Data Capture — Digitization

**Digitization** = converting continuous lines into discrete points so they can be stored in a computer.

- **Manual (tablet) digitizing** — trace features on a **digitizing board / tablet** with a puck; an electromagnetic coil in the puck transmits a pulse picked up by grid wires under the tablet → converted to (x, y). Tools: light table, digitizing board.
  - **Major problems:** the paper map **stretches/shrinks** day to day (new points slightly off from old); the **source map itself has errors**; **discrepancies across adjacent map sheets** → disconnectivity; **operators make many errors** while digitizing.
- **Heads-up (on-screen) digitizing** — source map/image is **scanned and georeferenced**, then features are **traced on screen** with the mouse; attributes entered manually.
- **Automated digitizing / vectorization** — map scanned on a large-format drum scanner → converted to a **binary image** → software traces lines (**semi-automatic** or fully **automatic / batch** mode).

**Typical human digitizing errors (error corrections — know these terms):**
- **Undershoot** — a line stops short of the feature it should meet (gap).
- **Overshoot / dangle** — a line extends past the intersection (dangling segment).
- **Sliver polygons** — thin gap/overlap polygons where two boundaries that should coincide don't quite.
- **Invalid polygons** — polygon doesn't close properly.
- **Mismatches** across map-sheet edges.

**Fixing errors — topology tools (QGIS workflow):**
- Create a new polygon layer with the correct **CRS**; digitize the outline.
- Use the **Snapping tool** (magnet icon) — forces new vertices to snap to existing vertices/edges within a **tolerance** (e.g. 0.6 m), eliminating gaps/overlaps.
- Run the **Topology Checker** with rules like **"must not have gaps"** and **"must not overlap"** (also "must not have dangles"); violations are highlighted.
- Fix with **Snap Geometry** (batch) or the **Vertex tool** (move/add/delete individual vertices), then **re-validate** until clean.
- Why it matters: overlay operations (intersect, union) need clean boundaries — gaps cause missing values, overlaps cause double-counting; overlapping lines create ambiguous connectivity → wrong routing.

### 17d. Data Transfer (importing existing digital data)

**Raster data that can be transferred:** satellite imagery (Landsat, Sentinel-2), DEM/DTM (elevation raster), aerial imagery (orthophoto), climate surfaces (temperature, rainfall), thematic rasters (land use, soil, population density), scanned maps (TIFF/JPEG).

**Vector data transfer methods:**
- **File-based:** Shapefile (.shp), **GeoPackage (.gpkg)**, GeoJSON (.geojson), KML/KMZ, GML.
- **Database:** PostGIS, SpatiaLite, Oracle Spatial, SQL Server Spatial.
- **Web-based:** **WFS (Web Feature Service)**, APIs, online GIS platforms. (Raster equivalent: WMS / WCS.)
- **Direct software-to-software:** QGIS imports Shapefile/GeoJSON/KML/GeoPackage and exports to another format.
- **GNSS/GPS data transfer:** **GPX**, CSV, GeoJSON.

**Attribute data capture:** import from GIS databases (ArcGIS, MapInfo), import from general databases (MS Access, Oracle), manual entry, **derive new attributes from existing data** (classification, computation), import from field observations.
- **Socio-economic data** — widely available from national/local government; product of censuses & population surveys. Combined with other datasets → **neighbourhood profiles / Geodemographics** (classifying areas for marketing).

### 17e. Participatory / Community-based Collection (recap from Intro)

- **VGI** — geographic data voluntarily contributed by individuals (OpenStreetMap features).
- **Crowdsourcing** — collecting from many people via apps/platforms (citizens reporting road closures, flood locations).
- **Citizen science** — public participation in scientific data collection (bird observations via **eBird**; environmental conditions).
- **Text coordinate importing** — a spreadsheet with Long/Lat columns + attributes (e.g. algae species by island) imported and plotted as points.

---

## 18. RAPID-REVISION TABLES

### 18.1 Geometry cheat-sheet
| Feature | Dim | Stored as | Example |
|---|---|---|---|
| Point | 0-D | (x, y) + attributes | ATM, well, lamp post |
| Line/Arc | 1-D | ordered (x,y); first & last node | road, river |
| Polygon | 2-D | closed line (first pt = last pt) | district, lake |
| Multi-polygon | 2-D | several polygons as one geometry | India + island territories |

### 18.2 Measurement scales
| Scale | Order? | Equal intervals? | True zero? | Example |
|---|---|---|---|---|
| Nominal | No | – | – | land-cover class |
| Ordinal | Yes | No | – | low/med/high |
| Interval | Yes | Yes | **No** | temp °C, year |
| Ratio | Yes | Yes | **Yes** | rainfall, population |
| Cyclic | wraps | – | – | wind direction, aspect |

### 18.3 Vector structures
| Structure | Topology? | Redundancy | Note |
|---|---|---|---|
| Spaghetti | No | High (shared edges twice) | simplest |
| Vertex dictionary | No | None | vertices stored once |
| DIME | **Yes** | None | US Census 1968; segment + from/to nodes + left/right polygons |
| Arc–Node | **Yes** | None | dominant modern GIS structure; node/arc/polygon tables |

### 18.4 Raster band interleaving
| Format | Order | Best for |
|---|---|---|
| BSQ | whole band, then next band | single-band processing |
| BIL | all bands per line, then next line | line processing / compromise |
| BIP | all bands per pixel, then next pixel | per-pixel math (NDVI) |

### 18.5 Choropleth classification
| Method | One-liner |
|---|---|
| Equal interval | equal-width classes; bad for skewed data |
| Pretty breaks | rounded limits; readable; may miss real distribution |
| Quantile | equal count per class; shows rank; can split/merge similar values |
| Standard deviation | above/below mean in SD units; needs normal data |
| Natural breaks (Jenks) | minimise within-class variance; dataset-specific |

### 18.6 Three resolutions
| Type | = | Trade-off |
|---|---|---|
| Spatial | pixel ground size | finer = more detail, more storage |
| Spectral | number/width of bands | more bands = better discrimination |
| Temporal | revisit frequency | shorter = better change monitoring |

### 18.7 Surface models from LiDAR
| Model | Contains | Built from |
|---|---|---|
| DEM / DTM | bare earth (ground only) | last returns |
| DSM | ground + buildings + canopy | first returns |
| TIN | triangulated surface | irregular points |

### 18.8 GPS numbers to memorize
- 24+ satellites (21 + 3 spare), 6 planes, 4 per plane
- Altitude 20,200 km, 12-hour orbit, 55° inclination
- Signal speed = speed of light ≈ 300,000 km/s
- Need ≥ 3 satellites for a fix (4th solves clock bias)
- 1 ms clock error ⇒ ~300 km position error
- DGPS ⇒ cm-level; standalone ⇒ few metres

### 18.9 Digitizing errors
| Error | Meaning |
|---|---|
| Undershoot | line stops short of target (gap) |
| Overshoot / dangle | line extends past intersection |
| Sliver polygon | thin gap/overlap between two boundaries |
| Invalid polygon | polygon fails to close |

---

## 19. SELF-TEST QUESTION BANK (with answers)

**Conceptual / definition**
1. Define spatial informatics. → Spatial data + informatics = the *extraction of information from spatial data for an application* (storage, error correction, analysis), not just collection.
2. Why is spatial data "inherently spatio-temporal"? → Every activity carries both location and time (photo metadata, bus GPS logs); Minkowski — space and time only have meaning in union.
3. From the systems perspective, when is data NOT spatial? → When the location is not explicitly encoded (no coordinates/polygon), even if semantically it refers to a place.
4. What did John Snow do, and why is it significant? → 1854 Soho cholera: plotted deaths on a street map, traced the cluster to the Broad Street water pump — first use of spatial analysis in epidemiology, before "GIS" existed.
5. Who is the "father of GIS"? → Roger Tomlinson (Canada GIS, ~1960; coined "geographic information system").
6. Three questions almost every digital service answers? → Where am I? What is around me? How do I get there?
7. Name the 5 eras of geospatial technology evolution. → Field survey & analog mapping → sensing & digital image processing → digital maps desktop-to-web → geo services → GeoAI.
8. Six sources of spatial data + one key idea each. → Remote sensing (synoptic, repeated); GNSS/GPS (trajectories, high temporal); survey/field (accurate but sparse/costly); administrative/government (authoritative, aggregated); sensors/IoT (fixed location + continuous time = spatio-temporal); VGI/crowdsourced (large-scale, dynamic, variable quality).
9. Land cover vs land use? → Cover = physical/natural (forest, water); use = anthropogenic purpose (built-up, agriculture).
10. Essential map components? → Title, legend, scale, north arrow/direction (+ source, grid). Direction is the most-forgotten.
11. GIScience vs GISystems vs GIServices? → Science = analysis/patterns/modelling; Systems = tools, storage, formats; Services = data & capabilities delivered to users.
12. Four things you can do with spatial data? → Visualize, query/identify, analyze, model/simulate.

**Data models**
13. Order the levels of abstraction and what each does. → Reality → Conceptual (features + relationships) → Logical (representation vector/raster + tables) → Physical (storage/database) → Computer.
14. In the vector model, what is explicit and what is implicit? → Location explicit; relationships (topology) implicit.
15. Polygon vs polyline? → Polygon is always closed (first point = last point); polyline is an open sequence of segments.
16. Give an example of a multi-polygon. → India including Andaman & Nicobar / Lakshadweep — mainland + islands as one geometry.
17. Classify: temperature in °C; rainfall in mm; "low/medium/high"; land-cover class; wind direction. → Interval; ratio; ordinal; nominal; cyclic.
18. Why can't interval data be multiplied/ratioed? → No true zero (0 °C is not "no temperature"), so "twice as hot" is meaningless.
19. Which vector structures have topology? → DIME and Arc–Node. Spaghetti and vertex dictionary do not.
20. What three things does DIME store per line segment? → Segment name; from/to node identifiers; left-polygon and right-polygon identifiers. (US Census Bureau, 1968.)
21. Define topology and its three relationships. → Explicit storage of spatial relationships: adjacency, connectivity, containment.
22. What is the dominant vector data structure in modern GIS? → Arc–Node ("intelligent data structure").
23. In a raster, why are spatial relationships implicit? → The grid is regular; adjacency/connectivity are derived from row/column position, not stored.
24. BSQ vs BIL vs BIP — which is best for computing NDVI and why? → BIP: all bands for a pixel are contiguous, so per-pixel math (NIR & Red together) needs no file seeks.
25. Which compression suits a classified low-resolution raster? A DEM? → RLE (or quadtree) for the classified raster (many repeated values); a DEM barely compresses (cell-by-cell array) because neighbours differ.
26. What does raster classification do to the original values? → Replaces continuous values with discrete class codes (1 integer/cell); original values are lost.
27. "Raster is faster but vector is ___." → corrector (Joseph Berry).
28. Which conversion is easy, which is hard? → Rasterization (V→R) easy; vectorization (R→V) hard.
29. State the dominant / winner-takes-all rule and when it misleads. → Assign the cell the value of the feature covering the largest area / containing the centroid; misleads for mixed cells where no class dominates.
30. Two decisions a choropleth map requires? → Which attribute to map; how to classify the values.
31. Best classification method to show "which districts are in the top 20%"? → Quantile (equal count).
32. Disadvantage of equal-interval classification? → With skewed/clustered data, most features fall in one class and others are empty.
33. When is standard-deviation classification appropriate? → Normally distributed data; to show above/below the mean.
34. Proportional vs graduated symbols? → Proportional: symbol area directly proportional to value (continuous). Graduated: symbol size stepped by class.
35. What is an isopleth/isoline map for? → Continuous surfaces — lines of equal value (contours, temperature).

**Data collection**
36. Roughly what fraction of GIS project cost is data collection? → 15–50%.
37. Primary vs secondary data capture? → Primary = direct measurement (new); secondary = derived from existing sources.
38. Fill the 2×2 capture table. → Primary raster = digital RS images / aerial photos; primary vector = survey (total station) / GPS; secondary raster = scanned maps/photos; secondary vector = digitized from maps / topographic surveys.
39. Name the three (four) types of resolution. → Spatial (pixel ground size), spectral (number/width of bands), temporal (revisit frequency), (radiometric = bit depth).
40. Vegetation's spectral signature? → Low in visible red (chlorophyll absorption), very high in NIR (red edge).
41. Water's spectral signature? → Strong absorption in NIR/SWIR; very dark in NIR; dips near 1.4 µm.
42. True-colour vs false-colour composite band assignment? → True: R→R, G→G, B→B. False (common): NIR→R, Red→G, Green→B; vegetation appears bright red.
43. Two key pre-processing corrections for multi-date change detection? → Geometric correction/georeferencing (common coordinate system) and radiometric normalization (comparable reflectance).
44. Dominant source of noise (low SNR) in satellite RS? → Atmospheric conditions — clouds, scattering.
45. SR vs AP — what's the same, what differs? → Technically similar; differ in capturing and interpretation. AP uses an analog camera at 3,000–9,000 m, then film is scanned.
46. Rank satellite / aircraft / drone by spatial resolution and by atmospheric noise. → Resolution: drone > aircraft > satellite. Atmospheric noise: satellite > aircraft > drone (drone flies below clouds).
47. LiDAR expansion and wavelength? → Light Detection And Ranging; ~1064 nm (NIR); active; day or night.
48. First return vs last return? → First = canopy/building tops (→ DSM, canopy models); last = ground (→ bare-earth DEM/DTM).
49. Purpose of the LiDAR ground base station? → High-accuracy GPS reference to correct the platform's XYZ (removes satellite-clock/atmospheric error) → cm-level.
50. DEM vs DSM vs DTM? → DEM/DTM = bare earth; DSM = includes buildings & canopy.
51. Which radar bands help in monsoon and why? → Longer-wavelength radar penetrates clouds and rain; active, day/night.
52. HH/VV vs HV/VH sensitivity? → Co-pol (HH, VV) → surface roughness, man-made structures; cross-pol (HV, VH) → volume scattering, vegetation canopy.
53. Sonar depth formula? → depth = (speed of sound in water × two-way travel time) / 2; ~1500 m/s.
54. GPS: number of satellites, altitude, orbital period? → 24+ (21 + 3 spare), 20,200 km, 12-hour orbit.
55. GPS core equation and what RATE is? → RATE × TIME = DISTANCE; RATE = speed of light ≈ 300,000 km/s.
56. How many satellites for a position fix? → ≥ 3 (a 4th resolves the receiver clock bias).
57. A 1 ms timing error equals how much position error? → ~300 km.
58. What is multipath error? → GPS signal reflects off buildings/terrain before reaching the antenna → wrong travel time; worst in urban canyons and forests.
59. How does DGPS work? → Base station at a known location computes its error vs measured position, broadcasts corrections to rovers → cm-level accuracy.
60. Name three digitizing errors. → Undershoot, overshoot/dangle, sliver polygon (also invalid polygon, sheet mismatch).
61. Which QGIS tools fix them? → Snapping tool (magnet) with a tolerance; Topology Checker with "must not have gaps"/"must not overlap"; Vertex tool.
62. Manual (tablet) digitizing vs heads-up digitizing? → Tablet: trace on a digitizing board with a puck. Heads-up: trace on-screen over a scanned, georeferenced image.
63. IDW vs Kriging? → Both spatial interpolation from sample points; IDW = simple distance weighting; Kriging = statistical/geostatistical ("smart").
64. What is resampling / grid aggregation? → Changing raster resolution (or CRS); merging adjacent similar cells with a representative value (nearest-neighbour/bilinear/cubic).
65. Vector transfer formats (file / web / GPS)? → File: Shapefile, GeoPackage, GeoJSON, KML, GML. Web: WFS, APIs. GPS: GPX, CSV, GeoJSON.
66. VGI vs crowdsourcing vs citizen science? → VGI = individuals contribute geographic data (OSM); crowdsourcing = many people via apps (flood/road reports); citizen science = public in scientific data collection (eBird).

---

## 20. HIGH-YIELD "MEMORIZE THESE" LIST

- Spatial informatics = **data + analysis**, extraction of information for an application.
- Spatial data is **spatio-temporal**; location = where + when + how + why.
- **John Snow / cholera / Broad Street pump** (1854) — first spatial analysis. **Tomlinson** — father of GIS.
- **5 eras**: field/analog → sensing/DIP → digital maps web → geo services → GeoAI.
- **6 data sources** + key ideas; **VGI** = consumer is the source; **Pokémon GO** case study.
- **Layered architecture**: one feature type per layer; points/lines/polygons separate.
- **Geometry** underlies everything: point (0-D), line (1-D), polygon (2-D), multi-polygon.
- Map must have **title, legend, scale, north**.
- **R-C-L-P** abstraction: Conceptual = features + relationships; Logical = representation + tables; Physical = storage.
- **Measurement scales**: nominal, ordinal, interval (no true zero), ratio (true zero), cyclic (wind/aspect).
- **Vector structures**: spaghetti & vertex-dictionary = no topology; **DIME** (Census 1968, left/right polygon) & **Arc–Node** (dominant) = topology.
- **Topology** = adjacency + connectivity + containment; needed for network analysis & overlay.
- **Raster**: grid of equal cells, one value each, relationships implicit; header = ncols/nrows/cellsize/origin/NODATA.
- **Band interleaving**: BSQ / BIL / **BIP (best for NDVI)**.
- **Compression**: RLE & quadtree for repeated values; DEM barely compresses.
- Finer resolution → more detail + more storage. **"Raster is faster, vector is corrector."**
- **Rasterization easy, vectorization hard**; **dominant/winner-take-all rule** for mixed cells.
- **Choropleth** = shaded polygons by attribute; needs (which attribute) + (how to classify).
- **Classification methods**: equal interval, pretty breaks, quantile (rank), standard deviation (normal data), natural breaks.
- Data collection = **15–50% of project cost**; **primary vs secondary** capture; **data transfer**.
- **3 resolutions**: spatial, spectral, temporal (+ radiometric).
- **Spectral signatures**: vegetation high NIR (red edge); water absorbs NIR; soil flat.
- **True vs false colour composite** (false: NIR→R → vegetation bright red).
- **Pre-processing / error corrections**: geometric (georeferencing, GCPs) + radiometric + atmospheric.
- **Platforms**: satellite (global, cloud noise, low SNR) / aircraft (medium, distortion) / drone (cm-res, below clouds, cheap repeat).
- **LiDAR** = active NIR laser 1064 nm; first return = canopy/DSM, last return = ground/DEM; base station for cm accuracy; TIN.
- **Radar/SAR** penetrates clouds; co-pol (HH/VV) = roughness/structures, cross-pol (HV/VH) = vegetation volume.
- **Sonar**: depth = speed_of_sound × two-way-time / 2; ~1500 m/s.
- **GPS**: 24 sats / 20,200 km / 12 h; RATE×TIME=DISTANCE, RATE = c ≈ 300,000 km/s; ≥3 sats; 1 ms → 300 km; **DGPS** base+rover → cm.
- **Digitizing errors**: undershoot, overshoot/dangle, sliver, invalid polygon → fix with **snapping + topology checker + vertex tool**.
- **Interpolation**: IDW (simple), Kriging (statistical).
- **Vector transfer**: Shapefile/GeoPackage/GeoJSON/KML, **WFS**, GPX.
