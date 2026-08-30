# DPCN Quiz Study Guide — 30 July to 24 August

**Course:** Dynamical Processes in Complex Networks (SC1.440), Instructor C. Hens.
**Web version (with diagrams):** https://claude.ai/code/artifact/4f235d00-2890-4a2c-861e-10c0b5aba8b1

The course has an arc. Lectures 1–3 are **graph structure** (how to describe a network).
Lectures 4–6 leave networks aside to learn **1-D dynamical systems** (fixed points, stability,
bifurcations). Lecture 7 fuses them: **a dynamical process running on a network**. Study in that order.

---

## Lecture 1 — 30 July · Networks as complex systems

A **network = graph** = a set of **nodes** (vertices) joined by **edges** (links). Everything in the
course is a way of *measuring* a graph or *running a process* on one.

**Why one toolbox works everywhere:** social (people/friendships, Milgram's "six degrees"),
biological (neurons ~10¹¹–10¹²; protein/gene interactions), infrastructure (airports–flights,
cities–roads, power stations–lines), information (web links, citations, character co-occurrence in
*Game of Thrones* / *Mahabharata*).

Recurring questions: who is the **influential** node? Where is the **bottleneck**? If you remove a
few nodes/edges does the network **fragment**? How does something **spread**?

### Adjacency matrix
For `N` nodes, `A` is `N×N` with `A[i][j] = 1` if an edge joins `i,j`, else `0`.
- Undirected ⇒ `A` symmetric; simple graph ⇒ zero diagonal.
- **Weighted** graph stores a real number (e.g. #flights) instead of 1.
- Real networks ⇒ **sparse** matrices (mostly zeros) ⇒ computation feasible.

### Degree and degree distribution
- **Degree** `kᵢ = Σⱼ A[i][j]` = number of edges touching `i` = `i`-th row sum of `A`.
- **Degree distribution** `P(k)` = fraction of nodes with degree `k`. Usually **not** a narrow bell
  curve — many real networks have a few huge **hubs** and a long tail (airport / celebrity picture).

### Static vs dynamic graphs
Lectures 1–3 treat the graph as **static** (wiring frozen while measuring). Real contact networks
are **temporal**; modern epidemic models rebuild the contact graph over time from phone mobility
data. The course assumes structure changes slowly vs the process on it.

---

## Lecture 2 — 6 August · Graph theory foundations

### Timeline to memorise
| Year | Who | What |
|---|---|---|
| 1735 | Euler | Seven Bridges of Königsberg — birth of graph theory |
| 1950s | Erdős & Rényi | Random graphs; when a "giant component" appears |
| 1967 | Milgram | "Six degrees of separation" |
| 1998 | Watts & Strogatz | Small-world networks |
| 1999 | Barabási & Albert | Scale-free networks (hubs), from the Internet |

### Seven Bridges of Königsberg
4 land masses, 7 bridges. Is there a walk crossing **every bridge exactly once**? Euler: land = node,
bridge = edge ⇒ a **multigraph**. Degrees `A=5, B=3, C=3, D=3` — **all four odd** ⇒ impossible
(proved without trying a route).

### Ways of moving through a graph
| Term | Rule | Repeats |
|---|---|---|
| Walk | any edge-connected node sequence | edges ✓, nodes ✓ |
| Trail | no repeated **edge** | edges ✗, nodes ✓ |
| Path | no repeated **node** | edges ✗, nodes ✗ |
| Cycle | a **path** that returns to start | only endpoints coincide |
| Circuit | a **trail** that returns to start | edges ✗, nodes ✓ |

### Eulerian vs Hamiltonian
- **Eulerian circuit** = closed trail using every **edge** once; **Eulerian trail** = same but open.
- **Hamiltonian** path/circuit = visits every **node** once.
- **Euler's criterion** (connected graph): Eulerian **circuit** ⟺ every vertex has **even** degree;
  Eulerian **trail** ⟺ **exactly two** vertices have odd degree (start/end at those two).
- **Trap:** Euler is a cheap `O(N)` degree check. Hamiltonian has **no** easy criterion (NP-hard).
  "Every edge once" (Euler) ≠ "every node once" (Hamilton).

### Handshaking lemma
`Σᵢ kᵢ = 2E`. Each edge adds 1 to two endpoints ⇒ total degree even ⇒ **number of odd-degree
vertices is always even**.

### Powers of A
`(Aᵏ)[i][j]` = number of **walks of length exactly k** from `i` to `j`.
- `(A²)[i][i] = kᵢ`; `trace(A²) = Σkᵢ = 2E`.
- `(A³)[i][i]/2` = triangles through `i`; `trace(A³)/6` = total triangles.

### Distance, shortest path, diameter
- **Path length** = number of edges (network distance, not physical).
- **Shortest path / geodesic** `d(i,j)` = fewest edges; `∞` if in different components.
- Directed graphs: `d(A→B) ≠ d(B→A)` in general.
- **Diameter** = largest shortest path. **Average path length** = mean of `d(i,j)` over all pairs.
- **BFS** computes all shortest paths from a source, layer by layer.
- **In-degree** `Σⱼ A[j][i]` (column sum); **out-degree** `Σⱼ A[i][j]` (row sum). Much-cited paper =
  high in / low out; textbook = low in / high out.

---

## Lecture 3 — 10 August · Centrality & clustering

No single "important node" — each measure answers a different question, and they can disagree.

### Local clustering coefficient
`eᵢ` = edges that exist **among `i`'s neighbours**; max possible = `kᵢ(kᵢ−1)/2`.
`Cᵢ = 2eᵢ / [kᵢ(kᵢ−1)]` (needs `kᵢ ≥ 2`).
`Cᵢ = 1` ⇒ neighbours form a clique; `Cᵢ = 0` ⇒ none connect. **Global/average** `C` = mean over
nodes. High `C` neighbourhood ⇒ info saturates the cluster fast but can be trapped; long-range
shortcut edges let it jump the whole graph (small-world).

### Four centralities
| Centrality | Formula (node `v`, `n` nodes) | "Central" = | Use when |
|---|---|---|---|
| Degree | `C_D(v) = k_v`; norm. `k_v/(n−1)` | many one-hop links | local influence matters |
| Closeness | `C_C(v) = (n−1) / Σ_{u≠v} d(v,u)` | short distance to everyone | fast broadcast/spread from `v` |
| Betweenness | `C_B(v) = Σ_{s≠t} σ_st(v)/σ_st` | lies on many shortest paths | bottleneck/gatekeeper; fragmentation |
| Eigenvector | `A x = λ_max x`, take `x ≥ 0` | connected to important nodes | influence where "who you know" counts |

`σ_st` = #shortest `s–t` paths; `σ_st(v)` = how many pass through `v`. Betweenness also has an
**edge** version (find links whose removal splits communities).

**Eigenvector centrality:** a node is important if important nodes point to it ⇒ solve `A x = λ x`,
take eigenvector of **largest** eigenvalue `λ_max`. Perron–Frobenius ⇒ all-positive entries for a
connected non-negative graph. This exact vector returns in Lecture 7 as the early-epidemic pattern.

**Traps:** highest-degree node is **not** automatically highest betweenness or eigenvector
centrality. Two nodes of equal degree can differ in eigenvector centrality. Modest degree + huge
betweenness = sole bridge between dense regions.

**Strength** (weighted graphs): `sᵢ = Σⱼ wᵢⱼ` (sum of incident weights); centralities generalise with
weighted paths.

**Applications shown:** climate networks (link locations with synchronised heat-wave events;
degree structure intensified over ~40 yr); epileptic seizure networks (time-varying weighted network
from EEG channel correlations, watch centrality shift as seizure propagates); text character
networks.

---

## Lecture 4 — 13 August · Intro to dynamical systems

Networks paused. Analyse `ẋ = f(x)` — one variable in time. Goal is never exact solution; it is
**where does it end up, and is that endpoint robust?**

### Linear first-order ODE
`du/dt = a − b·u` (constants, `b > 0`).
Exact solution with `u(0) = u₀`: `u(t) = a/b + (u₀ − a/b)·e^(−bt)`.
As `t → ∞`, `u → a/b`. Readings: charging capacitor, Newton cooling, population with immigration
`a` and death rate `b`.

### Fixed points (equilibria / steady states)
Set RHS to zero: `f(u*) = 0 ⇒ u* = a/b`. Long-time value instantly, no integration.

### Linear stability
Perturb `u = u* + ε`, keep first order: `ε̇ = f′(u*)·ε ⇒ ε(t) = ε(0)·e^(f′(u*)·t)`.
- `f′(u*) < 0` ⇒ decays ⇒ **STABLE** (here `f′ = −b < 0`, always stable).
- `f′(u*) > 0` ⇒ grows ⇒ **UNSTABLE**.
- `f′(u*) = 0` ⇒ inconclusive; look at higher order — this is where **bifurcations** live.

### Phase line
Plot `u̇` vs `u`. Zeros = fixed points. `u̇ > 0` ⇒ drift right; `u̇ < 0` ⇒ drift left. Arrows
converging ⇒ stable. **`+ → −` crossing (downward, negative slope) = stable; `− → +` = unstable.**

### Euler's method
`u_{n+1} = u_n + h·f(u_n)`. Local error `~h²`; global error `~h` (first order). For `u̇ = −b u`:
`u_{n+1} = (1 − bh)u_n`, decays only if `|1 − bh| < 1` ⇒ need `h < 2/b`. Too-big step ⇒ numerical
solution oscillates/blows up. RK4 / RK45 = accurate upgrades.

### Supporting ideas
- **Taylor series:** `sin x = x − x³/3! + x⁵/5! − …`; truncation error ↔ Euler discretisation error;
  same expansion is how you **linearise** `f` near a fixed point.
- **Finite-difference derivative:** forward `[f(x+h)−f(x)]/h`; central `[f(x+h)−f(x−h)]/2h` (cancels
  leading error).
- **Logistic** `u̇ = r u(1 − u/K)`: fixed points `u* = 0` (unstable, `f′(0)=r>0`) and `u* = K`
  (stable, `f′(K)=−r<0`); `K` = carrying capacity.

---

## Lecture 5 — 16 August · Bifurcations & the SIS model

**Bifurcation** = qualitative change in dynamics as a control parameter `r` crosses a critical value:
fixed points created, destroyed, collide, or swap stability. Only possible where `f(x*) = 0` **and**
`f′(x*) = 0` (non-hyperbolic point).

### Canonical 1-D bifurcations (normal forms)
| Name | Normal form | Fixed points | At `r = 0` |
|---|---|---|---|
| Saddle-node (fold) | `ẋ = r − x²` | `x* = ±√r` (r ≥ 0) | pair collides at 0, vanishes for `r<0`; `+√r` stable, `−√r` unstable |
| Transcritical | `ẋ = rx − x²` | `x* = 0, r` | branches cross and **exchange stability** |
| Supercritical pitchfork | `ẋ = rx − x³` | `x*=0`; `±√r` for `r>0` | `x*=0` stable→unstable; `±√r` **stable** (needs `x→−x` symmetry) |
| Subcritical pitchfork | `ẋ = rx + x³` | `x*=0`; `±√(−r)` for `r<0` | nonzero branches **unstable**, exist while origin still stable ⇒ abrupt jumps |

Course diagram convention: **solid = stable branch, dashed = unstable**. Read `ẋ vs x` (dynamics at
one `r`) together with `x* vs r` (organisation of equilibria).

### SIS epidemic model (Susceptible ⇄ Infected, no immunity)
`i` = fraction infected, `β` = infection rate, `γ` = recovery rate. Homogeneous mixing ⇒
`di/dt = β·i·(1−i) − γ·i = i·[(β−γ) − β·i]`.
- **Fixed points:** `i* = 0` (disease-free); `i* = 1 − γ/β` (endemic, exists iff `β > γ`).
- `f′(i) = (β−γ) − 2βi`. At `i*=0`: `f′ = β−γ` ⇒ disease-free stable iff `β < γ`. At endemic point:
  `f′ = −(β−γ) < 0` ⇒ stable.
- **Threshold / basic reproduction number:** `R₀ = β/γ`. `R₀ < 1` ⇒ dies out; `R₀ > 1` ⇒ endemic.
  This is a **transcritical bifurcation** at `R₀ = 1`. Control = push `R₀ < 1` (lower `β` distancing,
  raise `γ` treatment).
- **SIR** adds Removed: `ṡ=−βsi`, `i̇=βsi−γi`, `ṙ=γi`. **SIR-X** adds quarantine (Maier &
  Brockmann, COVID, *Science* 2020).
- **Trap:** `β` infects, `γ` recovers — trust the equations, not the lecture wording.

---

## Lecture 6 — 20 August · Numerics & the Spruce Budworm

### Workflow
1. Fix `r`. Plot `y = f(x; r)` vs `x`.
2. Axis crossings = fixed points (ignore trivial `x*=0` if told to).
3. Classify by crossing direction: `+ → −` (downward) stable; `− → +` (upward) unstable; tangent to
   axis = candidate saddle-node.
4. Pin exact values with a root-finder; re-plot for several `r` ⇒ build `x* vs r` diagram.

### Root-finders
| Method | Iteration | Needs | Convergence |
|---|---|---|---|
| Bisection | bracket `[a,b]` with `f(a)f(b)<0`; take midpoint; keep bracketing half | sign-change bracket, continuity | linear (slow), bulletproof |
| Newton–Raphson | `x_{n+1} = x_n − f(x_n)/f′(x_n)` | derivative + good guess | quadratic; can diverge |
| Secant | `x_{n+1} = x_n − f(x_n)(x_n−x_{n−1})/(f(x_n)−f(x_{n−1}))` | two start points, no derivative | superlinear ~1.618 |

**Trap:** bisection bracket must be **tight** (converges to whichever root it traps). Newton needs
`f′ ≠ 0` near the guess and can jump to another root.

### Spruce Budworm — bistability & hysteresis
`ẋ = r·x·(1 − x/K) − x²/(1 + x²)` (`K = 10`, `r > 0`). Term 1 = logistic growth; term 2 = saturating
bird predation. `x* = 0` always an equilibrium, **unstable** (`f′(0) = r > 0`). Nonzero-equilibrium
condition is a **cubic** ⇒ up to **three** positive equilibria.

At `r ≈ 0.5` the sign pattern of `ẋ` is `+ − + −` ⇒ **stable · unstable · stable**:
- low "refuge" state `x* ≈ 0.68` (stable)
- threshold `x* ≈ 2` (unstable) — start below ⇒ fall to refuge; start above ⇒ run to outbreak
- high "outbreak" state `x* ≈ 7.32` (stable)

**Bistability** for roughly `0.384 < r < 0.560` (three equilibria). Two folds = two saddle-nodes
(`r_SN,1 ≈ 0.384`, `r_SN,2 ≈ 0.560`).
**Hysteresis:** slowly raise `r` ⇒ population clings to low branch until it ends at the upper fold,
then jumps up; slowly lower `r` ⇒ clings to high branch until the lower fold. Up-path ≠ down-path —
the system "remembers". Same shape as ecological regime shifts, power-grid collapse, climate tipping.

Reference numbers (`K = 10`): `r=0.25` → one stable `x*≈0.26`; `r=0.5` → `0.68` (s), `2.0` (u),
`7.32` (s); `r=0.56` → only high `x*≈7.73` survives.

---

## Lecture 7 — 24 August · Dynamics *on* networks

Every node `i` carries state `xᵢ(t)`; edges couple the ODEs. Two flagship linear examples:
**diffusion** (Laplacian) and **early epidemic spread** (adjacency matrix).

### Graph Laplacian
`D = diag(k₁,…,k_n)` (degree matrix); `L = D − A`.
Undirected graph ⇒ `L` symmetric, positive semi-definite (`λᵣ ≥ 0`), `L·1 = 0` so smallest
eigenvalue `λ₁ = 0` with `v₁ ∝ (1,…,1)`. Number of zero eigenvalues = number of connected
components.

### Diffusion / consensus
`ẋᵢ = c·Σⱼ A[i][j]·(xⱼ − xᵢ)` ⇒ matrix form `ẋ = −c·L·x`.
Solve by eigen-decomposition: `x(t) = Σᵣ aᵣ(t) vᵣ`, each `ȧᵣ = −c·λᵣ·aᵣ ⇒ aᵣ(t) = aᵣ(0)e^(−cλᵣt)`.
So `x(t) = Σᵣ aᵣ(0)·e^(−c·λᵣ·t)·vᵣ`.
- Every `λᵣ > 0` mode decays; only `λ₁ = 0` survives ⇒ `x(t) → a₁(0)·v₁` = constant vector =
  **average of the initial condition** (consensus; connected graph homogenises).
- Speed set by smallest non-zero eigenvalue `λ₂` (**spectral gap** / algebraic connectivity /
  Fiedler value). Big `λ₂` ⇒ fast mixing; bottlenecked graph `λ₂ ≈ 0` ⇒ slow; shortcut edges
  raise `λ₂`.

### SI epidemic on a network (infected never recover)
`ẋᵢ = β·(1 − xᵢ)·Σⱼ A[i][j]·xⱼ`.
Early outbreak: all `xᵢ ≈ 0` ⇒ `(1 − xᵢ) ≈ 1` ⇒ **linearise**: `ẋ ≈ β·A·x`, so
`x(t) = Σᵣ bᵣ(0)·e^(β·κᵣ·t)·vᵣ` where `κᵣ, vᵣ` are eigenpairs of **A** (not `L`), exponent
**positive** (growth).
- Largest `κ₁` (spectral radius) dominates: `x(t) ~ e^(β·κ₁·t)·v₁`. Early growth rate = **`β·κ₁`**.
- Perron–Frobenius ⇒ `κ₁ > 0` and `v₁` all-positive ⇒ `v₁` is the **early infection pattern**
  (larger component = infected sooner). This `v₁` = eigenvector centrality from Lecture 3.

### Structure sets epidemic speed
Star (`n` nodes): `κ₁ = √(n−1)` (grows without bound). Open chain: `κ₁ ≤ 2` (→ 2 as `n → ∞`). Same
node and edge count ⇒ epidemic runs away faster on the **star**.

**Trap:** diffusion uses **L**, **decays** (`e^{−cλt}`), driven by **small** eigenvalue `λ₂`. Early
SI uses **A**, **grows** (`e^{+βκt}`), driven by **largest** eigenvalue `κ₁`. `κ₁` equals max degree
only for regular graphs — star has max degree `n−1` but `κ₁ = √(n−1)`.

---

## One-page formula sheet

**Structure**
```
kᵢ = Σⱼ A[i][j]                          degree = row sum of A
kᵢ(in) = Σⱼ A[j][i] ,  kᵢ(out) = Σⱼ A[i][j]
Σᵢ kᵢ = 2E    ⇒  #(odd-degree nodes) is even
(Aᵏ)[i][j] = # walks of length k, i→j
(A²)[i][i] = kᵢ ;  trace(A³)/6 = # triangles
ρ = 2E / [N(N−1)]   link density ;  ⟨k⟩ = 2E/N
```
**Eulerian (connected):** circuit ⟺ all degrees even; trail ⟺ exactly two odd; Hamiltonian ⟺ no
easy test.

**Node measures**
```
Cᵢ = 2eᵢ / [kᵢ(kᵢ−1)]                    eᵢ = edges among i's neighbours
C_D(v) = k_v/(n−1)
C_C(v) = (n−1) / Σ_{u≠v} d(v,u)
C_B(v) = Σ_{s≠t} σ_st(v)/σ_st
A x = λ_max x  →  take x ≥ 0 (Perron–Frobenius)   eigenvector centrality
sᵢ = Σⱼ wᵢⱼ                              strength (weighted)
```
**1-D dynamics**
```
u̇ = a − b u   ⇒  u(t) = a/b + (u₀ − a/b) e^{−bt}
f(x*) = 0                                fixed point
f′(x*) < 0 stable ; > 0 unstable ; = 0 inconclusive
ε(t) = ε(0) e^{ f′(x*) t }
phase line:  +→− crossing = stable ;  −→+ = unstable
u_{n+1} = u_n + h f(u_n)   Euler (global error ~h; stable if h < 2/b)
f′(x) ≈ [f(x+h) − f(x−h)] / (2h)   central difference
x_{n+1} = x_n − f(x_n)/f′(x_n)   Newton
```
**Bifurcations**
```
saddle-node    ẋ = r − x²      x* = ±√r (r ≥ 0); pair collides & dies at r=0
transcritical  ẋ = rx − x²     x* = 0, r ; exchange stability at r=0
supercrit fork ẋ = rx − x³     x*=0 loses stability ; ±√r stable for r>0
subcrit fork   ẋ = rx + x³     ±√(−r) unstable for r<0 ; abrupt jumps
fold: f = 0 AND f′ = 0 simultaneously
```
**Epidemics**
```
SIS   i̇ = β i (1−i) − γ i
      i* = 0  ;  i* = 1 − γ/β  (needs β > γ)
      R₀ = β/γ .  R₀<1 die out ; R₀>1 endemic  (transcritical at R₀=1)
SIR   ṡ=−βsi ,  i̇=βsi−γi ,  ṙ=γi
```
**Dynamics on networks**
```
L = D − A ,  symmetric PSD ,  λ₁=0 with v₁∝(1,…,1)
ẋ = −c L x  ⇒  x(t) = Σᵣ aᵣ(0) e^{−c λᵣ t} vᵣ   → consensus at mean(x(0)); speed λ₂
ẋ ≈ β A x  ⇒  early SI growth rate β·κ₁ (κ₁ = largest eig of A)
v₁ (all positive) = early infection pattern = eigenvector centrality
```

---

## Worked examples

1. **Degree sequence `(4,3,3,2,2,1,1)`.** `Σk = 16 ⇒ E = 8`. Odd-degree vertices `{3,3,1,1}` — four,
   an even count. Eulerian trail? No — needs exactly two odd vertices.
2. **Eulerian check.** `K₄` (square + both diagonals): all degrees 3 ⇒ four odd ⇒ no trail/circuit.
   Remove one diagonal ⇒ degrees `(3,2,3,2)` ⇒ exactly two odd ⇒ Eulerian **trail** exists (ends at
   the degree-3 corners), no circuit.
3. **`ẋ = x − x³`.** Fixed points `x* = 0, ±1`. `f′ = 1 − 3x²`: at `0`, `f′ = 1 > 0` unstable; at
   `±1`, `f′ = −2 < 0` stable. (Supercritical pitchfork at `r = 1`.)
4. **SIS threshold.** `β=0.3, γ=0.5 ⇒ R₀=0.6 < 1` ⇒ disease-free stable, endemic root negative
   (unphysical), outbreak fades. `β=0.8 ⇒ R₀=1.6`, endemic `i* = 1 − 0.625 = 0.375` stable.
5. **Euler step.** `u̇ = 2 − u`, `u₀ = 0`, `h = 0.5`: `u₁ = 1`, `u₂ = 1.5`, `u₃ = 1.75`. True
   `u(t) = 2(1 − e^{−t}) → 2`. Stable (`b = 1 > 0`); Euler stable (`h = 0.5 < 2/b = 2`).
6. **Diffusion on `K₃`.** `D = 2I ⇒ L = 2I − A`, eigenvalues `{0, 3, 3}`. `x(0) = (2,0,1)`; the
   `λ=3` modes decay `e^{−3ct}`; `x(t) → (1,1,1)` since mean `= 1`.

---

## Practice questions (answers below each)

**Q1.** What does `(A³)[i][i]` carry, and how do you get total triangles?
> Number of closed length-3 walks `i→…→i` = `2 ×` triangles through `i`. Total = `trace(A³)/6`.

**Q2.** State Euler's criterion for an Eulerian trail; apply to Königsberg.
> 0 or exactly 2 odd-degree vertices (0 ⇒ closed circuit; 2 ⇒ open). Königsberg has four odd
> (`5,3,3,3`) ⇒ no trail.

**Q3.** High degree, low betweenness — picture and meaning?
> A node deep in one dense cluster: many neighbours, but few shortest paths between other pairs
> route through it (internal alternatives; not on a bridge). Good local influence; removing it does
> not fragment the graph.

**Q4.** Why can equal-degree nodes have different eigenvector centrality?
> Degree weights each neighbour by 1; eigenvector centrality weights a neighbour by its own
> centrality (`x_v ∝ Σ A[v][j] x_j`). Neighbours that are themselves hubs ⇒ higher score.

**Q5.** `ẋ = r − x²`: fixed points, stability, bifurcation at `r = 0`?
> `x* = ±√r` (r ≥ 0). `f′ = −2x`: `+√r` stable, `−√r` unstable. At `r = 0` they collide (`f = f′ =
> 0`), vanish for `r < 0` — **saddle-node (fold)**.

**Q6.** Derive SIS endemic equilibrium and threshold.
> `i̇ = i[(β−γ) − βi] = 0 ⇒ i* = 0` or `i* = 1 − γ/β` (positive iff `β > γ`, i.e. `R₀ > 1`).
> `f′(0) = β − γ`: disease-free stable for `R₀ < 1`, loses stability at `R₀ = 1` (transcritical).

**Q7.** Why does explicit Euler blow up on `u̇ = −b u` with too-large `h`?
> `u_n = (1 − bh)^n u_0`; decays only if `|1 − bh| < 1` ⇒ `0 < h < 2/b`. Larger `h` ⇒ factor
> magnitude > 1 ⇒ growth/oscillation though the true solution decays.

**Q8.** Budworm at `r ≈ 0.5`: what is the middle equilibrium and why does it matter?
> The **unstable** equilibrium (`x* ≈ 2`) between the low refuge and high outbreak states — the
> **threshold / basin boundary**. Below it ⇒ collapse to refuge; above ⇒ explode to outbreak. Its
> fold collision produces hysteresis.

**Q9.** Hysteresis in one or two sentences?
> Sweeping a parameter up then down, the system follows different branches each way because each
> stable branch survives until destroyed at a fold — so the state depends on history, not just the
> current parameter.

**Q10.** Graph diffusion in matrix form; what does the state converge to?
> `ẋ = −cLx`, `L = D − A`. Eigenbasis: `x(t) = Σ aᵣ(0) e^{−cλᵣt} vᵣ`. All `λᵣ > 0` decay; `λ₁ = 0`
> mode (`v₁ ∝ 1`) survives ⇒ uniform vector = **average of initial values** (consensus). Rate ≈
> `cλ₂`.

**Q11.** Why does the largest eigenvalue of `A` (not `L`) govern early SI, and what is its eigenvector?
> Linearised SI is `ẋ ≈ βAx`; `Σ bᵣ e^{βκᵣt} vᵣ` is dominated by the biggest `κᵣ` ⇒ growth
> `e^{βκ₁t}`. Perron–Frobenius ⇒ `v₁ > 0` componentwise = order in which nodes light up =
> eigenvector centrality.

**Q12.** Star vs open chain, same `n` and edges — which spreads faster early, and why?
> The **star**: `κ₁ = √(n−1)` (unbounded in `n`) vs chain `κ₁ ≤ 2`. Early growth rate `βκ₁` ⇒
> star's `e^{βκ₁t}` outruns the chain's.

**Q13.** Phase-line stability rule without derivatives?
> Plot `ẋ` vs `x`. `+ → −` crossing (downward) ⇒ arrows inward ⇒ stable. `− → +` ⇒ unstable.
> Tangent to axis ⇒ candidate saddle-node.

**Q14.** Distinguish walk, trail, path.
> Walk: anything repeats. Trail: no repeated edge. Path: no repeated node. Closed path = cycle;
> closed trail = circuit.

---

## 10 things to nail before you walk in

1. **Adjacency matrix ⇄ graph.** Degree = row sum. `Aᵏ` counts length-`k` walks; `diag(A²)` = degree,
   `trace(A³)/6` = triangles.
2. **Handshaking:** `Σk = 2E`; odd-degree vertices come in even numbers.
3. **Euler's criterion:** circuit ⟺ all degrees even; trail ⟺ exactly two odd. Hamiltonian has no
   shortcut. Königsberg fails (four odd).
4. **Four centralities** and the question each answers: degree (local reach), closeness (fast
   broadcast), betweenness (bottleneck), eigenvector (important friends). They can disagree.
5. **Clustering coefficient** `Cᵢ = 2eᵢ / [kᵢ(kᵢ−1)]` — "do my neighbours know each other".
6. **Fixed point** = root of `f`. **Stability** = sign of `f′(x*)`: negative stable, positive
   unstable, zero ⇒ bifurcation territory. Same as arrow direction on the phase line.
7. **Three normal forms:** saddle-node `r − x²` (pair appears/dies), transcritical `rx − x²`
   (stability swap), pitchfork `rx ∓ x³` (symmetric split).
8. **SIS:** `i* = 1 − γ/β`, threshold `R₀ = β/γ = 1` (transcritical). `β` infects, `γ` recovers.
9. **Bistability & hysteresis** (Budworm): stable–unstable–stable, middle point is the threshold,
   up-sweep ≠ down-sweep because branches die at folds.
10. **On networks:** diffusion `ẋ = −cLx` → consensus at the mean, speed `λ₂`. Early SI `ẋ ≈ βAx` →
    growth rate `βκ₁`, pattern `v₁ > 0`. `L` = decay / small eigenvalue; `A` = growth / largest
    eigenvalue.

---

*Built from the 30 Jul–24 Aug transcripts, summary/key-point sheets, and the Module 2 + 1-D
bifurcation slide decks. Cross-check any exam-critical formula against your own class notes.*
