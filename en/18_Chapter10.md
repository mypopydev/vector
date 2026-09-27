<!--p217-->
# (10) CURVING SPACES AND INVARIANT DISTANCES

**On the Way to Tensors**

When Einstein began wrestling with the problem of how to extend the special theory of relativity to a general one, where the relative motion didn’t have to be constant, he needed a whole new mathematical toolkit. And who better to call on than his old friend from the Swiss “Poly,” Marcel Grossmann. Grossmann had never cut Minkowski’s maths classes! He was also a first-rate mathematician and a loyal friend. In fact, it was through Grossmann’s family that the impoverished Einstein had landed that life-saving job at the patent office. Grossmann himself had been given a place at the Poly— as a PhD student and an assistant to his supervisor—as soon as he graduated, and seven years later he’d become professor of mathematics there.

<!--p218-->
Einstein had tried for years to find someone to take him on as a doctoral student, but all he’d got for his trouble were rejections—partly because of his sassy reputation among the “old philistines” of mainstream academia. Still, he persevered, and in the summer of 1905, he’d finally had some luck with a landmark paper on measuring molecules: it earned him a doctorate from the University of Zurich. He dedicated it to Grossmann, in appreciation of his generosity in their student days—from lending him notes from lectures he’d skipped to helping him find a job. Unlike his professors, Grossmann had seen from the outset that Einstein was destined for greatness.[^ch10n1]

![Marcel Grossmann, 1909. ETH-Bibliothek Zürich, Bildarchiv/Photographer unknown/Portr_01239. Public domain.](images/p246.jpg){width="50%"}

In 1911, Grossmann began seeking ways to bring his now-famous friend back to their old school—which had recently been renamed the Swiss Federal Institute of Technology (still known as ETH for its German acronym). Marie Curie and Henri Poincaré were among those who wrote glowing and perceptive testimonials for Einstein, and in 1912 he was appointed to the newly established chair of theoretical physics at the ETH. Perhaps he savored such a glorious return. He certainly relished the chance to work once again with his old classmate, the way they used to study and explore ideas together as students, smoking their pipes and drinking coffee at the nearby Café Metropole.

<!--p219-->
For the next two years, the two friends collaborated closely on the herculean task of building mathematical foundations for the general theory of relativity. Einstein had already realised that in generalising the special theory, he was working on nothing less than a whole new theory of gravity. After all, an example where the relative motion isn’t constant is when one observer is falling because of gravity—in a free-falling elevator, say—and the other is fixed to the ground: the falling observer is accelerating relative to the ground-based one, so their relative speed isn’t constant. In 1912, however, when Einstein and Grossmann began their collaboration, there were still two major mathematical problems to solve before Einstein could find his general theory.

First, how to transfer the laws of physics from the special theory to the general one; and second, how to find the appropriate “distance” or interval measure in curved space-time (we’ll see *why* it’s curved in chap. 12), analogous to the flat Minkowski metric we saw in the previous chapter. As Einstein later recalled, “We found that the mathematical methods for solving problem 1 lay ready in our hands in the absolute differential calculus of Ricci and Levi-Civita”—that is, in tensor calculus. “As for problem 2,” he continued, the answer lay in Bernhard Riemann’s work on curved surfaces.[^ch10n2]

“Ready-made” these tools may have been, but first Einstein had to master them. As he told Arnold Sommerfeld, “In all my life I have never before labored [so] hard.” He went on to say that with Grossmann’s help, he had “become imbued with a great respect for mathematics, the subtle parts of which, in my innocence, I had till now regarded as pure luxury.” Minkowski would have been thrilled.[^ch10n3]

As we’ve seen, Sommerfeld had already dabbled with tensors as a way of writing Maxwell’s equations in flat 4-D space-time—and Maxwell himself had used two-index tensorial quantities to describe stresses in ordinary 3-D space. What Gregorio Ricci and Tullio Levi-Civita did was to develop a calculus that could handle curved spaces, too—and it was Grossmann and Einstein who first applied tensor calculus to curved *space-time*. But they all built on Riemann’s work—and he’d built on the ideas of his legendary teacher, Gauss.

<!--p220-->
## THE MATHS OF CURVED SURFACES: CARL FRIEDRICH GAUSS

Grossmann had done his PhD on non-Euclidean geometry, which had been pioneered by Gauss, Janos Bolyai, and Nicolai Lobachevsky in the 1820s. With the geometry of curved surfaces, Euclid’s axiom about parallel lines never meeting no longer holds, and you can see this most readily with lines of longitude on the globe: they’re parallel at the equator but they meet at the poles. So, can you ever speak definitively about “parallel” lines on a curved surface? This is a crucial question for vector analysis because the whole concept of addition of vectors is based on the parallelogram rule, where you slide vectors to the correct position by keeping them parallel (as in fig. 3.1).

The answer to this question came much later, as we’ll see when we meet Levi-Civita. But he was indebted to Ricci, who, in turn, was indebted to Gauss’s work on a related problem. In everyday life, we measure the distance between two points with a straight ruler laid along the straight line between the points, and Pythagoras’s theorem gives the distance measure or “metric.” But if there are no straight lines on a curved surface, what is the distance formula? The solution, Gauss decided, was to look at points that are very close together.

Gauss knew all about measuring distances firsthand. Ever since he was a teenager he’d been interested in geodesy—the mathematical analysis of the shape of Earth and the area of its surface—and in triangulation, the method used for surveying. Since then, he’d worked on various government and military surveying projects—war was still seemingly neverending. In fact, it was because of the Napoleonic Wars, which had raged during the years 1803–15, that Sophie Germain had finally revealed her true identity to Gauss. As we saw in chapter 3, she’d sought mathematical advice by writing to him under the pseudonym Monsieur Le Blanc. But when French forces took a Prussian town not far from Gauss’s home, she was so afraid for him that she persuaded a family friend—who was also a military general—to check on his safety. Gauss was most surprised by a courteous visit from an enemy soldier—and even more perplexed when the soldier said he’d been sent on behalf of Mademoiselle Germain!

<!--p221-->
From 1821 to 1825, Gauss, now in his forties, led a series of surveying expeditions mapping the entire kingdom of Hanover. These expeditions required not just mathematical know-how and expertise with instruments but also traveling through difficult terrain and living rough. Then, at night, Gauss would have to process by hand the data he and his team had collected—and to help himself he used the method of least squares that he’d already invented. This is a method for fitting a line to data points, or for finding the most accurate estimate from a bunch of repeated measurements— and among its many modern applications are the linear regression models I mentioned in connection with machine learning. Gauss was almost as reluctant to publish as that enigmatic Elizabethan Thomas Harriot had been two centuries earlier, for both men were perfectionists—and so the least squares method, and countless other of Gauss’s discoveries, were reinvented later by others.[^ch10n4]

Anyway, after all this hands-on experience Gauss was ready to present his seminal 1828 paper, *Disquisitiones Generales circa Superfices Curvas* (*General Investigations of Curved Surfaces*). In fact, it is Gauss who created the concept of the metric, the distance measure we met in the previous chapter, where I wrote the flat 3-D Euclidean metric as

::: {.displayeq}

$$\sqrt{x^{2}+y^{2}+z^{2}}.$$

:::

I assumed that *x, y, z* were the components of the position vector giving the distance along the straight line from the origin to the point (*x, y, z*), but the distance between two arbitrary points (*x*~1~, *y*~1~, *z*~1~) and (*x*~2~, *y*~2~, *z*~2~) is given by

::: {.displayeq}

$$\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}}$$.

:::

<!--p222-->
Gauss’s idea was that if two points on a *curved* surface are close enough together, so that *x*~2~ − *x*~1~ is very small, and similarly for the other coordinate differences, the little piece of surface between them is approximately flat. You can see this intuitively by imagining two nearby dots on an orange or a ball—and on a larger scale it’s why we can speak of a patch of “flat” land on the curved Earth. If your two points are *infinitesimally* close together, the surface between them will be flat to all intents and purposes, and the line between them will be straight. In modern terms, the surface is “locally” flat. It’s the same idea as when a small section of a curved line is approximated by a tangent line. You can use this straight tangent line to approximate the distance to a nearby point on the curve, as in figure 10.1—except that with the curved *surface*, you have a tangent *plane* rather than a tangent line.

![FIGURE 10.1. When two points on a curved line, or a curved surface, are very close together, the distance between them, *AB*, is approximately the straight-line distance *AB′*. In computer graphics, for example, curved lines can be built from tiny tangential segments.](images/fig10_1.jpg){width="50%"}

What this means is that you can use the Euclidean distance measure on a curved surface, except that instead of *x*~2~ − *x*~1~, *y*~2~ − *y*~1~, *z*~2~ − *z*~1~, you need the kind of infinitesimal distances used in differential calculus: *dx, dy, dz*. In other words, instead of

::: {.displayeq}

$$\sqrt{x^{2}+y^{2}+z^{2}}\text{or}\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}},$$

:::

Gauss showed that the general distance measure or metric is

::: {.displayeq}

$$ds=\sqrt{\left(dx\right)^{2}+\left(dy\right)^{2}+\left(dz\right)^{2}}$$,

:::

where the length of a line on the surface is denoted by *s*. Often this expression is squared, and, taking liberties with notation, the brackets are left out to make it easier to write—so the Euclidean metric for the surface is generally written as

::: {.displayeq}

*ds*^**2**^ = *dx*^**2**^ + *dy*^**2**^ + *dz*^**2**^.

:::

<!--p223-->
(Writing eighty years after Gauss, Minkowski knew to use this kind of differential notation for his 4-D space-time metric:[^ch10n5]

::: {.displayeq}

*ds*^**2**^ = *dx*^**2**^ + *dy*^**2**^ + *dz*^**2**^ − *c*^**2**^ *dt*^**2**^.)

:::

If all this isn’t familiar to you, you might be thinking that it’s all very well to talk about distance measures as the length of tiny straight lines, but what do you do when you want to measure longer curved distances? On the face of it, you’d have to lay down your infinitesimal rulers end-to-end along the curved line across the surface. Fortunately, the Leibnizian differential notation makes it beautifully clear how to answer this question much more simply: just integrate *ds* to find the distance *s*. I did this in figure 2.3b, using the 2-D version of this metric. If you *are* familiar with this, I hope you agree that it’s interesting to look back and see where the maths we learn today comes from—in this case, the mighty Gauss. He didn’t use the term “metric,” though; instead, he called this distance measure the “linear element” of the surface—and it’s still often called the “line element.”

The curved surface of a ball, say, is only two-dimensional, so you might also be wondering why the metric looks the same for flat 3-D space and a small patch on a 2-D curved surface. When we look at the ball’s surface, we are looking at it from the outside, so we see the points on the surface as points in 3-D space. But as you can see in figure 10.2, and analogously in figure 10.1, the infinitesimal distance between two of those points, measured *on the surface*, is virtually the same as the straight-line distance measured in space.

So, to highlight the *intrinsic*, 2-D nature of the surface—the way that a super-intelligent ant or 2-D alien would see it—Gauss followed Leonhard Euler’s lead by parameterising surfaces in terms of two “curvilinear” coordinates, which he called *p* and *q*. On the surface of Earth, for example, the *p*-axis could be the line of latitude around the equator, and the *q*-axis the meridian of longitude through Greenwich. An intelligent ant-alien crawling over this surface would take measurements from these two axes—it wouldn’t be aware there was a third dimension.

Gauss showed that when you do this, the metric on the 2-D surface becomes

![FIGURE 10.2. The curved distance between two points that are separated by an infinitesimal distance is almost the same as the straight-line distance between them, measured in 3-D space as if the surface weren’t there.](images/fig10_2.jpg){width="50%"}

::: {.displayeq}

*dx*^**2**^ + *dy*^**2**^ + *dz*^**2**^ = *Edp*^**2**^ + 2*Fdpdq* + *Gdq*^**2**^,

:::

<!--p224-->
where the *E, F, G* are functions of *p* and *q*. (You can see how he did it, in the next endnote.) In a virtuoso feat he also showed that the coefficients *E, F, G* in this expression, along with their derivatives, contain all that our 2-D creature would need to know to figure out the intrinsic geometry of the surface.

For example, the ant-alien would be able to tell if it were crawling over a flat space, where the angles in a triangle add up to 180°, a positively curved space such as a sphere, where they add up to more than 180°, or a negatively curved surface such as that of a saddle, where they add to less than 180° (as in fig. 10.3).

That’s because Gauss defined the “intrinsic curvature” in terms of the *area* of the curved triangle and the *difference* between 180° and the triangle’s angle sum. He didn’t know it, but for the case of a sphere Thomas Harriot had already discovered this formula, during his own work on mapmaking and navigating the surface of the earth:

::: {.displayeq}

$$\frac{\alpha+\beta+\gamma-\pi}{\text{Area} \text{of} \text{triangle}}=\frac{1}{r^{2}},$$

:::

<!--p225-->
where the triangle’s angles are designated by α, β, γ radians, π radians equal 180°, *r* is the radius of the sphere, and $\frac{1}{r^{2}}$ is its “Gaussian” or intrinsic curvature. Because Harriot didn’t publish his result, Albert Girard rediscovered and published it several decades later—but Gauss’s version was more sophisticated, and not just restricted to spheres. What’s more, Gauss showed that both the area and the angles in this formula could be found from the metric alone. This is quite astonishing at first sight. In fact, Gauss was so excited he called this discovery his *theorema egregium*, his “remarkable theorem.”

So let me unpack this remarkable result a little more. We’ve already seen that the metric tells you the length of a line—such as the magnitude of a vector, as we saw in chapter 9, or the circumference of a circle as in figure 2.3. And long ago Archimedes had worked out the surface area of a sphere (4π*r*^**2**^), and had even shown how to find the area of cylindrical segments of the sphere. But Gauss showed that the area of *any* curved surface could, in fact, be found from the metric coefficients, *E, F, G*, via the surface integral of the expression $\sqrt{EG-F^{2}}$. Without calculus and the concept of a metric, when Harriot derived the curved area of a triangle on a sphere—he was the first known person to do this, and he needed it to prove the intrinsic curvature formula above—he had to use many pages of ingenious geometrical arguments.

<!--p226-->
Mind you, it took Gauss many pages, too, to establish these fundamental relationships between curvature and the metric, but whereas Harriot had solved only the spherical triangle problem, Gauss showed the way for areas of any shape on any surface. As for the angles needed in Gauss’s and Harriot’s curvature formula, amazingly it turns out that *E, F, G* are *scalar products* of the unit vectors tangent to the coordinate lines *p* and *q* shown in figure 10.4—and the geometric formula for scalar products gives the cosine of the angle between these vectors. Of course, in 1828 Gauss didn’t know about vectors and scalar products—at least not in the formal sense— but he had the equivalent coordinate form, nonetheless. I’ve explained how he did it in the endnote.[^ch10n6]

![FIGURE 10.3. The angles α, β, γ in a triangle on a flat piece of paper add up to 180° or π radians, but on a sphere, they add to more than π, and on a saddle they add to less.](images/fig10_3.jpg){width="80%"}

![FIGURE 10.4 A spherical triangle bounded by three great circle coordinate lines. The angle between two such lines is the angle between their tangent vectors, as illustrated by the arrows. On a sphere all three angles are right angles.](images/fig10_4.jpg){width="50%"}

It’s telling that the impetus for both Gauss and Harriot to make their breakthroughs on curvature was practical—mapmaking and navigation. So, all this isn’t just for ants and aliens. We, too, can use the metric to determine the curvature of the surface we live on—we don’t have to travel into space to see Earth from the outside. It really is remarkable, as if one tiny equation, *ds*^**2**^ = *Edp*^**2**^ + 2*Fdpdq* + *Gdq*^**2**^, encodes an all-seeing god’s-eye view of the whole surface. And as we’ll see when we meet Gregorio Ricci, the coefficients of the differentials in a metric—such as the *E, F, G* here— turn out to be the components of a *tensor*, the next step on from a vector. In Einstein’s hands, it will be a key to the whole cosmos.

## FROM MAPMAKING TO BLACK HOLES: INVARIANCE, TOPOLOGY, AND “STRAIGHT” LINES

<!--p227-->
Einstein will also draw on something else that Gauss highlighted: the concept of invariance. In fact, invariance is critical to the economy and power of tensor equations, as we saw for vectors in the previous chapter. In particular, it’s important to have an invariant distance measure, in the sense that the Euclidean distance, say, or the Minkowski interval between events in space-time, would remain the same if it were being measured from a different point of view—from a rotated frame, for example, or a Lorentztransformed one. We saw examples of this earlier, and they illustrate the fact that the Euclidean and Minkowski metrics we met above are invariant under rotations and Lorentz transformations, respectively.

In 1828 Lorentz transformations were more than half a century into the future, but Gauss did show that his 2-D curvilinear metric—or what he called the “linear element” or “measure of curvature”—was invariant (or as he put it, “unchanged”) when you bent the surface into a different shape. At least, this was true if you didn’t tear or cut the surface: rolling up a piece of paper to form a cylinder, for example, or moulding a soccer ball into a football. This latter kind of moulding is what happens with the molten and fluid Earth, which bulges at the equator because of its rotation yet doesn’t change its total volume.

<!--p228-->
The invariance of the metric under this kind of bending or squashing relates to the counterintuitive idea that the curved surface of a cylinder is intrinsically “flat.” (It is only curved when viewed from the outside, so this kind of curvature is “extrinsic.”) To see the invariance, imagine a flat sheet of paper with a straight line drawn on it; as far as our 2-D ant can tell, it is just the same line—with the same length, and therefore the same metric—as when the paper is rolled up into a cylinder. But a sphere is intrinsically curved, as you may have noticed after juicing a half-orange: you can’t flatten out the hemispherical shell without tearing it. It’s only flat locally, as in figures 10.1 and 10.2. So, we’re talking not only coordinate transformations here but also topology—which deals with properties of surfaces and shapes that can be moulded without tearing—although Gauss didn’t use this term. We saw the idea of topology briefly in chapter 5, with the work of Gauss’s students Möbius and Listing in the 1840s, which was two decades after Gauss’s paper. Nonetheless, what Gauss had shown about the topological invariance of the metric explains why the bulging Earth can be treated as a sphere when it comes to measuring distances and angles.

An even more remarkable connection between curvature and topology is expressed in what’s called the global Gauss-Bonnet theorem. The “local” version of the theorem is just Gauss’s definition of curvature in terms of the angles and area in a curved triangle on a patch of the surface— with Harriot’s formula as a special case for spherical triangles—and, when needed, Pierre Ossian Bonnet’s 1848 extension of Gauss’s theorem to open surfaces such as disks. When you apply this not simply to a patch but to the whole (“global”) surface, such as a whole sphere, topology comes into it. In 1972, Stephen Hawking used the global Gauss-Bonnet theorem and Einstein’s equations to prove that the boundary, or event horizon, of a stationary black hole is topologically equivalent to a sphere. It’s another example of the way little human “ants” can sit with their pens and paper and use the maths of curvature to discover vast and mysterious new territory. The year before, Hawking had proved mathematically that the area of this boundary could never decrease—a result that wasn’t confirmed experimentally until 2021. But it was Roger Penrose who, in 1965, had used topology to prove that if general relativity is correct, then black holes really should exist in nature—they were not just mathematical artifacts. And then, in 2019, thanks to the international collaboration behind the Event Horizon Telescope, we were all treated to that extraordinary first direct image of a black hole—or rather, its roughly (topologically!) circular shadow.[^ch10n7]

Penrose shared the 2020 physics Nobel Prize after this spectacular confirmation of the existence of black holes. The other two recipients, astronomers Rienhard Genzel and Andrea Ghez, discovered the “supermassive compact object”—assumed to be a black hole—at the centre of our galaxy. Ghez is only the fourth woman to have won a Nobel Prize for Physics. But let me come back to Gaussian curvature, for it isn’t only useful in geodesy, surveying, and cosmology: today it has a wide range of down-to-earth applications, including cutting-edge materials science.[^ch10n8]

• • •

<!--p229-->
Gauss had another brilliant insight that paved the way for the sophisticated maths behind the headlines today. Just as Hamilton realised that quaternions formed an algebraic system in their own right, with different rules from ordinary algebra, Gauss realised that a curved 2-D surface was a “space” in its own right, just like the 3-D space that we live in. Such a space, with its two curvilinear coordinate axes and its own distance measure, has its own intrinsic 2-D geometry, and we’ve already seen that the metric is the key to this geometry, for it is needed to calculate distances, angles, and curvature. But there’s even more to it than this. In ordinary (flat) space, we have Euclid’s geometry. It is the geometry of straight lines, and the angles they make with each other, and there are countless theorems about these lines and angles, which have served us well for more than two thousand years. So, the question for Gauss was this: How do you find geometrical rules in a space that has no straight lines? His answer is ingenious. The thing about a straight line is that it is the shortest distance between two points in ordinary Euclidean space—so the question becomes, what is the shortest distance between two points on a curved surface?

On the surface of a sphere, like Earth, mathematical astronomers, map-makers, and navigators had known for millennia about “great circles”— circles that have the same centre and radius as the sphere, such as lines of longitude, and the equator. But it was Johann Bernoulli and his brother who’d figured out that the shortest distance between two points on this surface is along the great circle that runs through them. Even today, airplane pilots follow great circle lines where possible, to make their journeys more efficient. In the 1720s, Bernoulli’s former student Euler invented what is known as “the calculus of variations” to find the equation of this shortest line; it’s a sophisticated extension of school calculus, where you set derivatives of a function equal to zero to find its maxima and minima. A century later, Gauss showed how to apply the calculus of variations to the metric, to find the shortest distance between any two points on a 2-D curved surface.

<!--p230-->
This “shortest distance” lies on a line called a “geodesic”—a name that reminds us of non-Euclidean geometry’s connection with ancient navigation and Earth’s great circles. Einstein will make stunning use of geodesics when he rewrites the laws of motion for curved spaces. But as he recalled later, first he and Grossmann needed to understand the work of Gauss’s remarkable student Bernhard Riemann, for he’s the one who took Gauss’s analysis into higher dimensions.

## BERNHARD RIEMANN TAKES UP GAUSS’S BATON

In the late 1840s and early 1850s, Riemann studied at the University of Göttingen where Gauss was a professor, but it wasn’t the vibrant centre of intellectual activity it would become later in the century. The professors were formal and remote, and their lectures were old-fashioned—even Gauss taught only elementary classes. So, Riemann transferred to the University of Berlin for a couple of years—the professors there were also excellent mathematicians, and they gave much more cutting-edge lectures. Still, he chose to do his PhD with Gauss back at Göttingen.

Three years later, Riemann set himself quite a challenge in a paper first translated into English by William Kingdon Clifford—Maxwell’s brilliant young colleague and George Eliot’s friend, who developed a synthesis of Hamilton’s and Grassmann’s vectorial ideas as we saw in chapter 7. As I mentioned in the prologue, if you generalise *x, y, z*, the familiar Cartesian coordinates, and write *x*~1~, *x*~2~, *x*~3~, then it’s easy to imagine as many dimensions as you like, with coordinate axes *x*~1~, *x*~2~, *x*~3~, … , *x~n~*. Vector components—of velocity, say—in such an *n*-D space would be denoted by, say, *v*~1~, *v*~2~, *v*~3~, … , *v~n~*. Riemann’s challenge was to adapt Gauss’s work on curved 2-D space and find the rules of geometry for curved *n*-dimensional space.

First, Riemann had to define a way of measuring distances on an *n*-dimensional curved surface. He called this surface, this curved space, a “manifold.” (It’s a topological concept, for Riemann followed Gauss in exploring *intrinsic* curvature.)

<!--p231-->
Before we see how he did it, I should mention that he wasn’t the only one investigating *n*-dimensional spaces in the 1850s. Arthur Cayley, for example, wasn’t just the inventor of matrix theory, and a spirited opponent of vector analysis; he was also a pioneer in both invariant theory *and n*-D geometry—specifically, the geometry of a curved surface when it is projected onto flat Euclidean space, like a shadow on the ground.

Speaking of Cayley, twenty years later, in 1874, he was to be honoured with a portrait; it still hangs in the Trinity College dining room, next to Maxwell’s portrait and across from Newton’s (Maxwell had returned to Cambridge in 1871, as the first director of the university’s first science lab, the Cavendish). The occasion inspired another of Maxwell’s famous poems, this time addressed to the Cayley portrait fund committee. For those who are “to space confined,” he began, what honour could you pay to one whose mind has penetrated beyond these bounds? Then, after poetically listing Cayley’s achievements, he hoped viewers would pause before the portrait’s two-dimensional form and reflect on the man whose “soul, too large for vulgar space, in *n*-dimensions flourished unrestricted.”[^ch10n9] It’s a lovely evocation of the sense of freedom mathematicians can feel when they imagine spaces untethered to our ordinary world.

Cayley was ultimately working in Euclidean geometry, though, whereas Riemann was looking at the intrinsic geometry of curved spaces, or manifolds. In modern terminology, a manifold looks “locally” like a flat *n*-D Euclidean space—so it is an extension of Gauss’s idea that curved surfaces look flat if you zoom in close enough, and that flat spaces can be handled with simple generalisations of school geometry, especially Pythagoras’s theorem. So, Riemann defined the distance measure—the metric, or what he called the “line element”—of a flat *n*-dimensional manifold by analogy with the Euclidean metric:

::: {.displayeq}

$$ds^{2}=dx_{1}^{2}+dx_{2}^{2}+\dots+dx_{n}^{2}.$$

:::

In fact, it is Riemann who first used the term “flat” for a surface whose line element is the sum of squares of differentials like this.

<!--p232-->
On a flat piece of paper, the Euclidean metric *ds*^**2**^ = *dx*^**2**^ + *dy*^**2**^ holds regardless of the size of the sheet—and in ordinary Euclidean space, *ds*^**2**^ = *dx*^**2**^ + *dy*^**2**^ + *dz*^**2**^ holds everywhere. On a curved manifold, however, Riemann followed Gauss, noting that you could only write the metric as a sum of differentials like this if you focussed your attention locally, in the flat “neighbourhood” around a *point*. Information about the intrinsic curvature of the *surface* is contained in the *coefficients* of the differentials in the surface’s *intrinsic* metric, as we saw earlier with Gauss’s 2-D metric,

::: {.displayeq}

*ds*^**2**^ = *Edp*^**2**^ + 2*Fdpdq* + *Gdq*^**2**^.

:::

In general, though, the coefficients in a metric depend not just on the curvature but also on the choice of coordinates: the same metric will look different when expressed in different coordinates, just as the equation of a circle looks different in Cartesian coordinates than it does in polar ones: *x*^**2**^ + *y*^**2**^ = *a*^**2**^ and *r* = *a*, respectively, for a circle with radius *a* and centred at the origin. So, the simple fact of having coefficients in the metric is *not* enough to tell you if the surface is curved. What Riemann hinted at, however, was that there *is* a way to decipher the manifold’s curvature from these metric coefficients. We’ll see what he meant later, for he didn’t go into detail in this paper, which was designed for a general audience.

He presented it when he was applying to become a *Privatdozent* at Göttingen, in 1854. *Privatdozents* were lecturers who were paid by their students, not by the university—so it was pretty tough if you didn’t get many students. But it was the first step on the academic ladder—and part of the grueling application process included a “habilitation” thesis and lecture. Einstein’s first academic job, in 1908, was as a *Privatdozent* at Bern University; he’d failed the year before with an application offering his 1905 special relativity paper as a habilitation thesis: it was rejected as “incomprehensible”! Which shows just how radical his theory was at the time. Riemann’s lecture, too, was beyond most of his listeners’ comprehension, although seventy-seven-year-old Gauss, who was in the audience, certainly appreciated its significance. Gauss was a good person to have on your side, and he thought Riemann was a true mathematician “of a gloriously fertile originality.” High praise indeed, for Gauss wasn’t one to hand out compliments, as Grassmann and many others had found. Perhaps Gauss’s difficult temperament had something to do with the death in childbirth of his beloved first wife, for it seems he never recovered from his grief.[^ch10n10]

<!--p233-->
Three years later, Riemann became an assistant professor, and eventually a professor, at Göttingen. He made many brilliant contributions to mathematics, including his PhD thesis, which laid the foundations for complex analysis, taking the idea of complex numbers into deeper territory. He also pioneered the topological idea of classifying a surface according to its “genus” (as it is now called)—essentially the number of “holes” in it, like a teacup with one hole as opposed to a sphere with none. But what concerns our story now is a paper he wrote in 1861, for it is at the heart of both the algebraic theory of curvature and the concept of tensors.

## RIEMANN’S LANDMARK ESSAY: HOMING IN ON TENSORS

Riemann had written this essay for a competition sponsored by the Parisian Academy of Sciences, on the topic of heat conduction for a specific type of heat distribution. As we saw with Grassmann’s and Germain’s prizewinning papers, such competitions were an important way to stimulate research on cutting-edge topics. And since it was *so* cutting-edge, here things become a little more complex, not least because of Riemann’s Greek notation, so feel free to skim this section for the key take-away points. In particular, note that his Greek symbols have more than one index or subscript—a hallmark of tensors—and that metrics are examples of “quadratic differential forms”; also, the notation Σ means a sum.

Riemann began with the heat equation that Joseph Fourier had derived in 1822. As I mentioned in chapter 6, this equation shows how temperature changes over time as heat diffuses through a body. You can imagine, say, holding a metal fire poker where the other end is heated by the fire, and gradually you feel the heat flowing up and through the handle—so the temperature is changing in all three dimensions of space. For the competition, however, the Academy had specified that as the heat flowed, the temperature should change only in two dimensions—say, when the interior of the poker is insulated so the heat only flows along and across its surface. Riemann’s innovative approach to this problem was to transform the coordinates in the heat equation from the usual Cartesian coordinates *x* ≡ *x*~1~, *y* ≡ *x*~2~, *z* ≡ *x*~3~ to new coordinates *s*~1~, *s*~2~, *s*~3~, which he defined to be functions of only two dimensions—say *x* and *y* but not *z*. This is what Gauss had done when he wrote his 2-D curved metric in terms of *p* and *q*.

<!--p234-->
I’ve been talking a lot about coordinate transformations here and in chapter 9, and how quantities such as scalar and vector products, and the distance/interval measures given by the Euclidean and Minkowski metrics, remain invariant when expressed in terms of the new coordinates. Similarly, Riemann ended up with the equation

::: {.displayeq}

Σα~ι,ι′~ *dx*~ι~*dx*~ι′~ = Σβ~ι,ι′~ *ds*~ι~*ds*~ι′~.

:::

You can see that the form of the expression on the left-hand side of the equation is the same as that on the right, and so the expression is invariant under Riemann’s coordinate transformation from *x*~1~, *x*~2~, *x*~3~ to *s*~1~, *s*~2~, *s*~3~.

Riemann’s two-index symbol α~ι,ι′~ is related to the “conductivity coefficients,” which appear in the heat equation—and his β~ι,ι′~ is related to the conductivity coefficients in the heat equation written in terms of the new coordinates *s*~1~, *s*~2~, *s*~3~. (He wrote the conductivity coefficients themselves as *a*~ι,ι′~ and *b*~ι,ι′~, respectively.) But the technical details[^ch10n11] are not important: it’s the way Riemann represented his coefficients that matters here, and the fact that he intuited—forty years before tensors were formally defined—that they were what we now call the “components” of a tensor.

The Σ in Riemann’s equation stands for sum. (It’s the upper-case Greek letter sigma, analogous to the Latin S, used as shorthand for “sum.”) The indices ι, ι′ in the sum Σα~ι,ι′~*dx*~ι~*dx*~ι′~ each refer to the three dimensions of space, represented by the three coordinates *x*~1~, *x*~2~, *x*~3~. All the possible combinations of ι, ι′ in this case are (1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3). So Σα~ι,ι′~*dx*~ι~*dx*~ι′~ is a shorthand way of writing

::: {.displayeq}

α~1,1~*dx*~1~*dx*~1~ + α~1,2~*dx*~1~*dx*~2~ + α~1,3~*dx*~1~*dx*~3~ + α~2,1~*dx*~2~*dx*~1~ + … + α~3,3~*dx*~3~*dx*~3~.

:::

(And similarly for Σβ~ι,ι′~.) This looks rather like the metrics we’ve been discussing, although this kind of “differential form” had also been studied purely for its algebraic properties—and Riemann was talking about heat conduction, not metrics. Differential forms are expressions with differentials such as *dx*~1~, *dx*~2~, … ; Riemann’s expression is a “quadratic differential form,” because it is made from products of *two* “differentials”—*dx*~1~*dx*~1~, *dx*~1~*dx*~2~, and so on—analogous to the squares in quadratic equations.

<!--p235-->
To see the similarity of Riemann’s differential form with a metric, in the Euclidean metric $dx_{1}^{2}+dx_{2}^{2}+dx_{3}^{2}$ the coefficients analogous to Riemann’s α~ι,ι′~ would be:

::: {.displayeq}

α~11~ = α~22~ = α~33~ = 1,

:::

with all the other α~*ij*~’s equal to zero. (Today the indices in a tensor component aren’t separated by commas as Riemann did, because commas now refer to partial derivatives. And I’ve used the subscript *ij* because Riemann’s use of ι and ι′ is confusing: as we’ve seen in figure 9.3, dashes often denote transformed coordinates. But I’ll keep to Riemann’s notation for the rest of this chapter.) Riemann was well aware of this similarity with metrics. But although he said that he was using similar methods to those Gauss had used for his work on curved surfaces, his focus was on the algebra that came out of his analysis of the heat equation.

The first hint that this algebraic analysis involved quantities that we now call tensors is in the *two-index notation* he used to represent the conductivity coefficients (*a*~ι,ι′~ and *b*~ι,ι′~) in the heat equation, and the associated coefficients α~ι,ι′~ and β~ι,ι′~ that we saw in the quadratic form above. At the end of chapter 9, I showed how Maxwell, too, had intuited the idea of a tensor, when he wrote the components of stress with two indices, *P~hk~*. I also showed—with the help of figures 9.4 and 9.5—why he needed two indices, rather than the one you need for the components of a vector (as in fig. 9.1, for example). Riemann didn’t discuss why he used two indices when he represented his conductivity coefficients as *a*~ι,ι′~. But to visualise them, you can take a small volume of the body conducting the heat, just as in figure 9.4—so the coefficients *a*~ι,ι′~ behave like the *P~hk~*, except that they are measuring conductivity rather than stress. For example, when ι ≡ *y* and ι′ ≡ *x*, the conduction of heat is going in the *y*-*x* direction like the arrow *P~yx~*.

<!--p236-->
Riemann did specify that he was considering only the case where the conduction was the same in both directions—for example, when the conduction is the same from *y* to *x* as from *x* to *y*, so that *a~y~*~,*x*~ = *a~x~*~,*y*~, or more generally, *a*~ι,ι′~ = *a*~ι′,ι~. This is another example of invariance: interchanging the indices on *a*~ι,ι′~ doesn’t change the value of the coefficient. Another name for this invariance is “symmetry,” because interchanging the indices ι, ι′ to get ι′, ι is like reflecting them, just like reflecting your image in a mirror, or reflecting a snowflake about an axis of symmetry.

But there’s more to Riemann’s “tensors” than just two indices.

## THERE’S MORE TO TENSORS THAN NOTATION!

In fact, two indices alone are not necessarily the marker of a tensor. For instance, two decades after Riemann’s paper, Maxwell, too, represented conductivity with two indices—in his case, *K~pq~*, where he explained that the conduction was flowing from a point *p* to *q*; but he also denoted a current flowing in the same direction as *C~pq~*.[^ch10n12] It is true that a current has a direction and a magnitude, but in a circuit it adds like an ordinary number or scalar, so it is neither a vector nor a tensor.

The question of notation *is* important, and the index notation is brilliant for doing computations with tensors. But it is only a way of *representing* a mathematical quantity, not of *defining* it. What matters is the properties that mathematical quantities have to have if they are to be called vectors and tensors—including not just their rules of addition and multiplication but also the ability to express invariant expressions, such as the scalar product ***a*** ∙ ***b*** and Riemann’s Σα~ι,ι′~*dx*~ι~*dx*~ι′~ = Σβ~ι,ι′~*ds*~ι~*ds*~ι′~. Later we’ll see in more detail what it takes to define a tensor. But it does turn out that Riemann’s α~ι,ι′~ and β~ι,ι′~ are tensor components—and so are the conductivity coefficients, although Riemann’s working doesn’t show it.[^ch10n13] After all, tensors haven’t yet been invented! Still, Riemann’s paper—like Maxwell’s, Cauchy’s, and Thomson’s papers on stress—shows the kinds of problems that made it necessary to invent them.

<!--p237-->
There’s more, though, for tensors can have more than two indices, and in his search for the transformation that kept Σβ~ι,ι′~*ds*~ι~*ds*~ι′~ invariant—that is, the same as Σα~ι,ι′~*dx*~ι~*dx*~ι′~—Riemann came up with threeand four-index quantities, too. Then he did something really special. First, he tossed off, as an aside, the fact that “the expression $\sqrt{\sum\beta_{\iota,\iota},ds_{\iota}ds_{\iota}},$ can be regarded as a line element in a more general space of *n* dimensions extending beyond the bounds of our intuition.” Then he said that if you imagine a surface in this space, then his three- and four-index quantities are key to measuring the curvature of the surface. They are built from combinations of the coefficients β~ι,ι′~ and their derivatives—so this is what Riemann meant in his habilitation lecture, when he suggested there *was* a way to tease out the curvature information from the metric coefficients, regardless of the coordinate system.[^ch10n14]

Riemann didn’t give a name to these three- and four-index quantities. They are essentially the components of what are now—thanks to Ricci and Levi-Civita—called the Christoffel symbols and the Riemann tensor, respectively. The name “Christoffel *symbols*” indicates that these three-index quantities *aren’t* components of a tensor—at least, not of a single tensor. The details don’t matter here, for the point once again is simply that if something has indices, it isn’t necessarily a tensor; as I indicated, it needs to have other properties—notably invariance under linear coordinate transformations.

Christoffel symbols are built from derivatives of the coefficients in a quadratic differential form such as the metric, and the Riemann tensor is built from the Christoffel symbols and their derivatives. So, in a space with a metric, the key idea is that if the Riemann tensor equals zero, then the space is flat. What’s more, if the space is flat, then the Riemann tensor is zero. Which means the Riemann tensor is *the* thing that tells you if your space is curved or flat. So it’s often just called the “curvature tensor.”

Since the Riemann tensor is built from the coefficients in the metric, which are functions of the coordinates, it has a value at each point in space. So technically it is a tensor field rather than a tensor, just as the electric and magnetic vectors ***E*** and ***B*** are vector fields. In practice, though, researchers tend to refer simply to the *tensors* and *vectors* that define gravitational and electromagnetic *fields*. (Some, however, demand more mathematically precise language, but such rigorous definitions came long after Maxwell’s mathematical development of Faraday’s idea of physical fields, and Riemann’s pioneering work on curvature.)

<!--p238-->
The Riemann tensor is sometimes called the Riemann-Christoffel tensor, and the symbols comprising it are called the Christoffel symbols because, surprisingly, Riemann wasn’t the only one to come up with these quantities. So did Elwin Christoffel, a maths professor at Einstein’s old school, the Zurich Polytechnic—although Christoffel published his work in 1869, three decades before Einstein was a student there. Christoffel probably didn’t know about Riemann’s 1861 essay, but he *was* inspired by Riemann’s 1854 habilitation lecture, which led him to explore conditions for the invariance of quadratic differential forms. Unlike Riemann, though, Christoffel didn’t connect his three- and four-index symbols with curvature, for his focus was pure algebra.[^ch10n15]

Riemann didn’t develop his curvature idea much further—that would be up to Ricci, Einstein, and Grossmann. For like his English translator Clifford—and like Maxwell, Minkowski, and so many others—Riemann died too young to fully develop his potential. In 1862, he’d contracted tuberculosis. Over the next few years, he and his new wife and baby daughter spent time in Italy, desperately hoping he’d recuperate in the warmer climate. But in 1866, he lost his battle with this dreadful disease, just like his mother and three sisters. He wasn’t yet forty.

• • •

Riemann’s habilitation lecture wasn’t published until 1867. Clifford’s English version, *On the Hypotheses Which Lie at the Bases of Geometry*, appeared in 1873, in *Nature*. Riemann’s essay on heat was published only in his collected works of 1876—it hadn’t won the essay competition! The judges were looking for something more specific—they hadn’t appreciated Riemann’s extraordinarily general approach to their heat problem, let alone the fact that it contained the seeds of both tensor analysis and the theory of curvature. So, his paper had languished for years, unappreciated and unknown, and Riemann never knew how important it would become. He never knew that his name would live on in the Riemann tensor, the bedrock of general relativity.

<!--p239-->
In 1912, however, Einstein and Grossmann seized upon Riemann’s work in order to build the geometry of curved space-time. We saw earlier that Einstein had identified two problems he and Grossmann needed to solve: how to transfer the laws of physics from the special theory to the general one; and how to find the appropriate metric in curved space-time. Riemann gave them the answer to the second problem: the line element will look like Riemann’s $\sqrt{\sum\beta_{\iota,\iota},ds_{\iota}ds_{\iota}},$ and the coefficients β~ι,ι′~ will be functions of the coordinates. They won’t be constants, like the 1s in the Euclidean metric, or the 1, 1, 1, −*c*^**2**^ in Minkowski’s metric,

::: {.displayeq}

*ds*^**2**^ = *dx*^**2**^ + *dy*^**2**^ + *dz*^**2**^ − *c*^**2**^ *dt*^**2**^,

:::

for then their derivatives would be zero and therefore so would the Riemann tensor, so the space-time would be flat.[^ch10n16]

To solve the first problem, however, Einstein and Grossmann will need a rigorous theory incorporating all the tensorial ideas I’ve been discussing—ideas intuited over many decades by many mathematicians, from Cauchy and Christoffel to Maxwell, Riemann, and more. So, it’s time to meet Gregorio Ricci!

<!--stats: p=72 fig=5 eq=14 note=0-->
