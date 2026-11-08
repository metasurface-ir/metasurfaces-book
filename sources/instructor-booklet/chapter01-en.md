## 1.1 Introduction: why do we need metasurfaces at all?

Let's begin with a very simple question: if we want to change the path of an electromagnetic wave, what options do we have? The first thing that comes to mind is probably a lens, mirror, or antenna. Well, we have used these very tools in optical, communication, and radar systems for years: a lens focuses light, and a mirror sends it back.

These tools are excellent, and metasurfaces are not about to retire them! So where is the problem? Like old tube televisions, these conventional components are often heavy, thick, and bulky. Each is also made for a particular job. In today's world, where phones, radars, and sensors become smaller and more complex every day, we cannot keep putting a large, bulky component in the wave's path to control it.

Now imagine a layer as thin as a sheet of paper that does exactly what a thick lens would do when a wave hits it! It might tilt the wave, focus it at a point, rotate its polarization, or even perform several tasks at once.

That is precisely the magic of a **metasurface**: controlling a wave with an ultrathin engineered surface.

Many tiny elements, smaller than the wavelength, are arranged on this thin surface. Instead of relying on a large thickness to control the wave, we use these tiny structures to tell it how to behave.

This chapter will not bury us in heavy mathematics and simulations. For now, we simply want to feel the physics and see how these magical layers work.

## 1.2 From natural materials to engineered structures: playing with geometry!

When we hear the word “material,” its intrinsic properties come to mind. We know, for example, that glass transmits light and copper conducts electricity. Ordinarily, a material's composition and chemistry determine its behavior.

But electromagnetics has a big secret: shape and geometry can matter just as much as the material itself!

Suppose we have a piece of copper sheet. Cut it into a straight strip, and it interacts with a wave in one way. Bend that same strip into a ring or a U shape, and the arriving wave encounters a completely different response. Why?

To picture it, imagine a playground swing. Push it with exactly the right rhythm—the appropriate frequency—and its oscillation grows. We call this **resonance**.

The tiny elements on a metasurface behave in much the same way. When a wave at the right frequency reaches them, electric charges inside these structures begin to oscillate strongly and resonate. Here is the golden point: by changing the dimensions of these elements, such as the strip length or gap size, we can determine the frequency and phase at which this resonance occurs.

Our whole viewpoint now changes. We no longer wring our hands and ask, “Which material in nature has the property I need?”

Instead, we roll up our sleeves and ask, “What geometry should I build to make the wave show the behavior I want?”

## 1.3 Metamaterials: playing with nature's rules

Have you ever wondered why most materials around us behave similarly toward light and electromagnetic waves? The answer lies in two key parameters: electric permittivity, $\epsilon$, and magnetic permeability, $\mu$.

When an electromagnetic wave encounters a material, it sees that material through these two parameters. In general, both are complex quantities:

$$
\epsilon=\epsilon'-j\epsilon'',\qquad \mu=\mu'-j\mu''.
$$

The real parts, $\epsilon'$ and $\mu'$, act like the material's “memory”: they determine how much energy is stored in it. The imaginary parts, $\epsilon''$ and $\mu''$, act like an “engine of loss”: they indicate how much wave energy becomes heat and is dissipated when the wave encounters the material.

Now let's enter the world of **metamaterials**. Plot two coordinate axes for the real parts, and we obtain four regions, each with its own behavior and personality:

1. **Natural or DPS materials (Double-Positive):** this is our familiar world, with $\epsilon'>0$ and $\mu'>0$, where glass, water, and most natural dielectrics live.
2. **ENG materials (Epsilon-Negative):** these have $\epsilon'<0$ and $\mu'>0$. Metals at optical frequencies and plasmas are examples of this behavior.
3. **MNG materials (Mu-Negative):** these have negative magnetic permeability, with $\epsilon'>0$ and $\mu'<0$. They operate through magnetic resonances and behave very differently.
4. **DNG materials (Double-Negative):** these are the stars of the metamaterial world: both parameters are negative at once, $\epsilon'<0$ and $\mu'<0$.

The DNG story began in 1967, when Viktor Veselago put a bold prediction on paper: “If a material could be found with both negative permittivity and negative permeability, the physics of refraction would be transformed!” He showed that the direction of energy propagation, the Poynting vector $\mathbf S$, and the wavefront direction, the wave vector $\mathbf k$, point in opposite directions in these materials. This means that a wave incident on such a material refracts on the same side of the normal—negative refraction—rather than behaving as in the classical Snell-law picture we learned!

Years later, scientists learned to make these materials in practice. They used thin metal wires to create negative permittivity and split metal rings, or SRRs, to create negative permeability, bringing these remarkable properties into the real world.

Other exciting ideas appeared along the way:

- **ENZ materials (Epsilon-Near-Zero):** materials with near-zero permittivity, where the effective wavelength becomes very large and the phase remains nearly uniform throughout space.
- **MNZ materials (Mu-Near-Zero):** materials with near-zero permeability, where the wave impedance takes on particularly unusual values.
- **DZR materials:** materials with both permeability and permittivity very close to zero.
- **Chiral structures:** materials without mirror symmetry that can rotate the wave's plane of polarization.

## 1.4 From volume to surface: why was becoming “two-dimensional” a big leap?

After the initial excitement about three-dimensional metamaterials, engineers encountered a practical reality: “These structures are very challenging and expensive to make!” Imagine arranging many tiny resonators, such as SRRs, inside a three-dimensional volume with micrometer precision. Besides the fabrication difficulty, there was another serious physical obstacle: high ohmic loss.

When a wave travels through a thick volume full of metallic resonators, part of its power becomes heat in each layer. By the end of the path, the output signal was greatly weakened. A fundamental question arose: “Do we really have to manipulate the wave inside a thick volume? Could we perform the same control on a very thin layer?”

That idea was the birth of **metasurfaces**.

With metasurfaces, we no longer need to fill a volume with complicated materials. Instead, we fabricate a very thin layer, like a printed circuit board or a nanopatterned layer, made of an array of engineered unit cells. These tiny planar elements locally change electromagnetic boundary conditions and surface impedance, providing complete control of the reflected or transmitted wave's phase, amplitude, and polarization.

In this way, metasurfaces pushed the boundaries of electromagnetics and provided a platform for realizing ideal theoretical boundary conditions, such as a perfect magnetic conductor or PMC, in the real world with negligible weight, easier fabrication, and much higher efficiency.

But the most important change was how we viewed the physics. With metamaterials, we wanted to make a “new material.” With metasurfaces, we want to hack the “boundary between two media”!

What does that mean? When a wave hits a wall—a boundary—classical physics tells us that some is reflected and some transmitted. Now imagine that this is no ordinary boundary! Its surface is covered in smart elements that tell the incoming wave, “You change your phase, you change direction, and you rotate your polarization!”

From this viewpoint, we have a smart intermediary that engineers the electromagnetic boundary conditions just as we wish.

## 1.5 What exactly is a metasurface? A plain mirror versus a smart boundary

Now that we know where metasurfaces came from, let's give them a neat, precise definition:

**A metasurface is a thin engineered layer formed by arranging many elements smaller than the wavelength, whose job is to control a wave during reflection, transmission, or absorption.**

“A metasurface can be regarded as a thin engineered layer whose arrangement of constituent elements controls wave behavior, including reflection, transmission, and absorption. Common academic definitions often emphasize that these elements should be smaller than the wavelength and arranged regularly and periodically. However, there is a subtle point: small scale and periodicity are not absolute requirements of its nature; they are mainly tools that make our work easier.

The reason this viewpoint dominates academic teaching is that it simplifies the problem. Floquet's theorem, which we will meet in later chapters, lets us reduce the analysis of an infinitely periodic structure to one unit cell and minimize the mathematical complexity. In the real world, beyond the classroom framework, a surface can still be a fully fledged metasurface without a periodic structure. Its essential nature lies in the ability to engineer electromagnetic responses, rather than in a requirement that the structure repeat.”

You might ask, “A plain metal sheet reflects waves too. How is a metasurface different?”

The difference is freedom of action and programmability. A flat metal sheet behaves like a mirror: its response is uniform and intrinsic, and it returns everything at a specified angle. On a metasurface, we can arrange the elements so that the right side changes the wave's phase a little and the left side changes it more! These deliberate changes tilt the reflected wave, focus it at a point, or turn it into a complicated beam. A metasurface can even perform differentiation and integration.

### Is a metasurface a component or a system?

Both, really! Physically, you see a thin board—a component—but functionally, you are dealing with a “system.”

Imagine a symphony orchestra. The metasurface is the orchestra. Dozens of musicians, the small elements, sit on stage. Each plays an instrument and produces a particular sound, but what you hear as the listener—the outgoing wavefront—is the coordinated, precise combination of all those sounds. If even one musician changes rhythm—a phase change—the overall musical output changes.

Depending on what we arranged this orchestra to do, metasurfaces fall into two main categories:

1. **Reflective metasurfaces:** the wave hits the surface and returns after being modified, as in smart radar surfaces or reflectors.
2. **Transmissive metasurfaces:** the wave passes through the surface and changes shape along the way, as in very thin flat lenses or metalenses.

## 1.6 Unit cells: the musicians in this symphony orchestra!

Earlier, we used words such as “small elements” and “musicians.” In scientific language, this smallest building block of a metasurface is called a **unit cell** or **meta-atom**. It might be a metal ring, a simple strip, an aperture in metal, or even a dielectric post.

### Electromagnetic pixels

Just as the image on your monitor is made by placing thousands of tiny pixels side by side, the wavefront leaving a metasurface is formed by these unit cells. But there is a crucial difference: monitor pixels do not concern themselves with their neighbors, whereas metasurface cells talk to one another through electromagnetic fields and affect each other—a phenomenon called coupling.

To tell each unit cell exactly which musical note to play—which electromagnetic response to give—metasurface designers adjust several parameters:

- **Geometry and dimensions:** should it be a ring or a square? How long and wide should it be?
- **Materials:** should we use copper or gold? Should the substrate be Teflon or a Rogers laminate?
- **Element spacing:** how close should the cells be?

### Arranging the cells

Once the designer has made the desired cells, they need to be placed across the surface. There are usually two arrangements:

1. **Uniform arrangement:** all cells are identical. Think of painting an entire wall one solid color. This arrangement is mainly used for radar-wave absorbers or filters.
2. **Gradient arrangement:** the cells' size or shape gradually changes from one side to the other. These step-by-step changes bend, rotate, or focus the outgoing wave. The real magic of metasurface wave control lies in these gradient arrangements.

## 1.7 How does a metasurface give a wave instructions? The control toolbox

When an electromagnetic wave meets a metasurface, its unit cells can change four main wave properties. Let's see which buttons appear on this “magical control panel”:

### 1. The amplitude button

The cells can absorb some wave energy to reduce its amplitude. This is a wonderful property for radar absorbers—materials that swallow waves and prevent reflection—or spatial filters.

### 2. The phase button

This may be our most frequently used button! By changing the cell's shape or size, we can create a “time delay” in transmission or reflection, equivalent to a phase change. If these phases change step by step across the surface, the wavefront tilts, focuses, or takes on the shape we want.

### 3. The polarization button

Polarization means the direction of the electric field's oscillation. Some cells, particularly asymmetric shapes such as a cross with unequal arms, can receive a vertically oscillating wave and return a horizontal or even rotating, circularly polarized wave. This means complete control over the oscillation direction!

### 4. The direction button: generalized Snell's law

Remember learning in high-school physics that “the angle of incidence equals the angle of reflection”? Well, a metasurface gets around that classical rule!

By creating a continuous phase slope—a phase gradient—across the surface, it can reflect a normally incident wave obliquely at a steep angle. This upgraded rule is called **generalized Snell's law**, the basis of beam steering.

## 1.8 Inside a unit cell: electric and magnetic responses

Now let's use an imaginary microscope to look inside one of these tiny metal cells. What exactly happens when an electromagnetic wave, consisting of electric and magnetic fields, hits it?

### 1. Electric response

The wave's electric field pushes the free charges—electrons—inside the cell's metal and gathers them at its two ends. This charge accumulation creates an electric dipole that acts like a tiny antenna and radiates a new wave.

### 2. Magnetic response: the magic of artificial magnetism!

Here engineering really shines. In nature, materials with a strong magnetic response at high frequencies, such as microwave or optical frequencies, are scarce. Engineers found a trick: shape the unit cell as a ring with a small gap, and the wave's field makes a circulating current flow around it. That rotating current produces a magnetic field. We have created **artificial magnetism** without using any magnetic material!

### 3. Huygens metasurfaces: the complete development

What happens if we design a cell to produce electric and magnetic responses of equal strength at the same time? In this remarkable situation, the surface impedance becomes exactly equal to the impedance of air—free space.

What is the result? The wave reaches the surface and does not even notice a change of environment, so no wave is reflected! One hundred percent of its energy passes through, while its phase changes along the way. These magical surfaces, named in honor of Huygens' principle, are the best candidates for making exceptionally efficient metalenses—transmissive flat lenses.

### 4. Complex coupling: bianisotropy

Sometimes the geometry is so special, as in three-dimensional or chiral structures, that an electric field alone can induce a magnetic response in the cell, or vice versa! This phenomenon, called bianisotropy, gives designers access to more advanced forms of control.

## 1.9 From flat lenses to holograms: where are metasurfaces useful?

When we can control wave phase, amplitude, and polarization pixel by pixel with subwavelength precision, we gain an almost magical ability to engineer waves! This all-purpose toolbox has helped metasurfaces revolutionize countless fields:

1. **Metalenses:** say goodbye to the curvature and thickness of conventional glass lenses! A flat, two-dimensional phase map can focus light or radio waves at a point. This means cameras, sensors, and microscopes that are remarkably light and thin.
2. **Smart antennas and beam steering:** in modern communication systems such as 5G and 6G, beams need to be directed toward different users without heavy mechanical motors. Metasurfaces can shape and narrow beams and redirect them in a fraction of a second.
3. **Polarization control:** a metasurface can act like a magical filter, receiving a linearly oscillating wave and returning a spiral-like, circularly polarized wave. This is vital in satellite communications.
4. **Radar absorbers and concealment:** if we match the surface so that the wave enters completely without reflection, then dissipate its energy inside the structure, we obtain a “perfect absorber,” a basis of stealth technologies.
5. **Holography and wavefront shaping:** by precisely setting the phase and amplitude of every cell, we can create complicated patterns or even three-dimensional holographic images in space.
6. **Biological and chemical sensing:** if a particular molecule settles on the unit cells, their resonance shifts slightly. That subtle change can be used to make highly sensitive medical and environmental sensors.

## 1.10 Challenges and limitations: why isn't everything a metasurface yet?

You may be asking, “If metasurfaces are so wonderful, why haven't they replaced all our existing equipment?” The answer lies in the difference between theory on paper and the unforgiving realities of engineering. Metasurface design is a continuous tradeoff among the following limitations:

1. **The bandwidth Achilles' heel:** metasurfaces usually operate through resonance. A resonance works wonderfully at a particular frequency, but a small change in the incident frequency can greatly degrade performance. Overcoming this limitation requires much more complicated designs.
2. **Energy loss:** unit cells are often made from metals and dielectrics. Especially at high frequencies, such as terahertz and optical frequencies, metals swallow some wave energy and turn it into heat. That reduces the efficiency of the whole system.
3. **Troublesome neighbors—mutual coupling:** we usually simulate a cell individually, assuming identical neighbors. In a real metasurface, a cell interacts electromagnetically with different cells beside it. This mutual coupling can shift its final response away from the design prediction.
4. **Fabrication and manufacturing challenges:** at high frequencies, cell dimensions reach micro- and nanoscales. Even a few nanometers of lithographic error or a thickness change can substantially shift the resonance.
5. **Sensitivity to incidence angle:** a surface designed for normal incidence may become completely confused when a wave arrives at a steep angle and fail to give the intended response!

## 1.11 Summary and our roadmap through the book

In this chapter, we saw how engineers moved beyond the limitations of natural materials to the idea of metamaterials, then created metasurfaces to escape the challenges of three-dimensional fabrication. We learned how a cell's geometry generates electric and magnetic responses that let us control wave phase, amplitude, and polarization.

In general, we encounter three levels of analysis when studying and designing a metasurface:

1. **Unit-cell or microscopic level:** investigating resonance physics and current distributions.
2. **Effective or macroscopic level:** viewing the metasurface as a boundary with a specified impedance.
3. **System level:** evaluating the whole assembly, such as the radiation pattern of the final antenna.

### Our roadmap for the coming chapters

To take you from an interested student to a capable metasurface designer, we have arranged the source book into nine engineered steps—chapters:

- **Chapter 2, Electromagnetic Modeling and Fundamental Relations:** the mathematics and physics governing boundaries.
- **Chapter 3, Initial Metasurface Design and Implementation:** how to build your first unit cell in software.
- **Chapter 4, Periodic Structures, Floquet Theory, and Diffraction Orders:** understanding periodic-array physics, an essential prerequisite for precise design.
- **Chapter 5, Metasurface Synthesis:** calculating the required phase and amplitude maps from the desired output wave.
- **Chapter 6, Numerical Modeling and Simulation Methods:** advanced techniques in CST and HFSS.
- **Chapter 7, Active, Tunable, and Intelligent Metasurfaces:** entering the world of coding metasurfaces and time-dependent control.
- **Chapter 8, Modern Metasurface Applications in Communication Engineering:** studying systems such as RIS for 6G.
- **Chapter 9, Materials, Fabrication Technologies, and Measurement Methods:** taking a software design into the laboratory and testing it successfully.

Our journey into the fascinating world of metasurfaces has only just begun. In the next chapter, we put on our mathematics-and-physics work clothes to uncover the equations behind this magic!
