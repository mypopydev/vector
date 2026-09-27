<!--p188-->
# (9) FROM SPACE TO SPACE-TIME

**A New Twist for Vectors**

Since 1863 Arthur Cayley had held the Sadleirian professorship of mathematics at Cambridge—in fact, he was the first to hold this prestigious chair, which had been endowed by Lady Mary Sadleir. Not much is known about her, except that she was devoted to good causes—the maths chair at Cambridge was far from her only beneficence. It is fitting, given such a benefactor, that Cayley was an early supporter of women’s higher education. Although they couldn’t take formal degrees at Cambridge, women were allowed to study lectures similar to those offered the men, and in 1869 and 1871 the first women’s residential colleges were established—Girton and Newnham. One of these young Girton women was Grace Chisholm, who found Cayley very welcoming, yet stiflingly old-fashioned in his approach to mathematics. She recalled the “flapping sleeves” of his academic gown “as he stood with his back to the listeners chalking and talking at the same time at the blackboard.”[^ch09n1] But this was a one-off comment: she’d needed special permission from the headmistress of Girton, as well as from Cayley, even to attend his class; with few exceptions, women studied with tutors in their own colleges, rarely attending lectures with the men.

<!--p189-->
Chisholm qualified for the equivalent of a first-class degree in 1893. A motion to formalise degrees for women was defeated, several times, over the next few decades—including in 1897, when some male undergrads were so chuffed at retaining their privilege they went on a wild celebratory rampage through town, causing the equivalent of more than a hundred thousand dollars’ worth of damage. Cayley must have been disgusted, for he’d been chairman of Newnham’s council through the 1880s, and he had also taught at Girton. Virginia Woolf would give her famous “Room of One’s Own” lectures at these colleges in 1928.[^ch09n2]

In the years just before that wild student rampage, the vector wars had been playing out, and as we saw, the physicists’ argument in favour of modern vector analysis was gaining ground. In the background, though, Cayley and Peter Tait had been quietly debating the issue from a mathematical point of view. Back in 1888 Cayley had exclaimed to Tait, “we are irreconcilable and shall remain so,” but in the summer of 1894—when Cayley was seventy-three and Tait ten years younger—these two elder statesmen of British mathematics went public with their mathematicians’ view of the vector debate. And at Tait’s suggestion, they did it together, each reading a paper before the Royal Society of Edinburgh.[^ch09n3]

## THE BEAUTIFUL CONCEPT OF INVARIANCE

Cayley began his presentation diplomatically, quoting Tait’s view of the advantage of quaternions: “They give the solution of the most general statement of the problem they are applied to, quite independent of any limitations as to the choice of particular coordinate axes.” What Tait meant was that if you change your frame of reference—by rotating the axes, say— your points in space will have different coordinates, and your vectors (and quaternions) will have different components. But as you can see in figure 9.1, the *length* of a vector doesn’t change when the frame is rotated through an angle of θ—it’s just the same vector—and so the *scalar and vector products* of any two vectors will remain the same, too.

<!--p191-->
This remarkable property, where certain things stay the same even when the components are measured from different axes, is called “invariance.” The relationship between the two sets of coordinates is called a “coordinate transformation.” There are two basic types of coordinate transformation: one is simply a “change of variables,” such as transforming from Cartesian to polar coordinates as in figure 2.3, where your axes stay the same; the other is a transformation between *frames*—that is, where the axes themselves are changed. (More technically, a frame is a ruler, a clock, and a coordinate system, which allow the observer to coordinatize events in time and space.) It’s this second type of coordinate transformation that is important in many practical problems.

![FIGURE 9.1. The vector ***a*** has components (*a*~1~, *a*~2~) in the usual *x*-*y* frame, and (*a*~1′~, *a*~2′~) in the rotated *x′*-*y′* frame. It is the same vector, with two different coordinate representations. The length of the vector is the same in both frames, as you can see from the geometry of the figure. Mathematically speaking, it is invariant under rotations. The same will be true for a second vector ***b***. So the scalar and vector products are invariant under rotations, too, as you can see by using the geometric definitions of these products: ***a*** ∙ ***b*** = *ab* cos Φ, where *a* and *b* are the lengths of the two vectors, and Φ is the angle between them; because the vectors don’t change, the angle between them isn’t affected by the coordinate change. Similarly, ***a*** × ***b*** has a magnitude (length) of *ab* sin Φ, and a direction perpendicular to the plane of the two vectors, and this plane—the plane of the page in the diagram here—doesn’t change when you rotate the axes in this way. When the axes are changed like this, the “coordinate transformation equations” are: *x′* = *x* cos θ + *y* sin θ, *y′* = −*x* sin θ + *y* cos θ. We saw an example of this for the robot arm in figure 4.2 (where we rotated the arm rather than the axes). But the key point is not the details but the fact that when you change your coordinate frame, the two sets of coordinates are related by specific equations. This is key to the idea of tensors.](images/fig9_1.jpg){width="50%"}

Because whole-vector expressions such as scalar products are invariant under certain coordinate transformations, “coordinate-free”—or “coordinate-independent”—is a more mathematical way of saying “whole” when speaking of representing vectors. The 1905 special theory of relativity will show in spades just why (and how) invariance matters in physics, but in 1894, when Tait and Cayley were debating the issue, they were focusing on maths rather than physics.

In fact, the idea of invariance is both mathematically fascinating and more broadly applicable than in physics alone. To take a modern digital application first, neural networks handle complex data by passing information from one node or “neuron” to another, just as the neurons in our brains do. At each node, a model (analogous to linear regression) assigns weights to the input data, weighting each piece of data according to its importance in the desired output. We saw something similar in chapter 4, with search engine ranking algorithms. In neural networks, though, each layer of nodes adds more complexity to the model, so when working out the maths for mapping one layer of neurons onto the next, programmers must make sure that key features of the information are invariant under these “maps” or coordinate transformations.

<!--p192-->
For instance, in 2022 the DeepMind AI group’s “AlphaFold” neural network succeeded in predicting the structures of virtually all the known proteins—two hundred million of them, which had been identified over the years through genetic sequencing of various species. Proteins are chains of amino acids that fold into three-dimensional shapes—and it’s the shape that governs their function. So, it’s the shape that scientists want to understand in order to create new types of drugs, or new enzymes for agriculture or pollution control, or to detect new variants of concern in the SARS-CoV-2 virus via its associated proteins, and so on—except that there are so many possible ways these chains of amino acids can fold that it had long been impossible to figure out the actual structures. The AlphaFold algorithm used the linear (1-D) sequence of each protein’s amino acids, along with training data about known structures of related proteins, to predict the 3-D coordinates of all the key atoms in the folded protein.[^ch09n4] As it progresses from one layer of nodes to the next, such an algorithm “learns” more about the protein’s possible shape from this input data, so programmers have to make sure that key attributes, such as the distance between the atoms, stay the same when the information is transferred to the coordinate frame of the next node.

As with other molecular modeling, and also with computer vision applications, the protein algorithm also had to learn to recognise the correct shape even if it is rotated—which meant that the mathematical representation of the 3-D shape had to be invariant under rotations. The concept of invariance is important in many neural network and other technological applications, from satellite imagery and biomedical microscopy imagery to keeping the James Webb Space Telescope in place.

Cayley, and the other pioneers of the maths of invariance, would be stunned at these sophisticated modern applications. On the other hand, they knew that all sorts of things can be invariant. For example, in chapter 4 we saw that if you rotated a book horizontally through 90° and then flipped it over vertically through 180°, it would have a different orientation when you performed these operations in reverse—whereas if you rotated a featureless box or ball in this way, it would look the same each time. That’s because the box and ball are symmetrical. Similarly, a snowflake generally has six points or corners, and it is beautifully symmetrical—so it looks just the same when you rotate it through multiples of 60°. (To be pedantic, in nature not all snowflakes are *perfectly* symmetrical— but you can see the point.) In other words, it is invariant under these rotations—and also under 180° rotations, or reflections, about its axes of symmetry.

So, invariance is related to symmetry—and in maths these two words are often used interchangeably.

<!--p194-->
As for Tait, he was interested in the invariance of vector and quaternion quantities, and he gave the example of ***a*** ∙ ***b*** = 0, an equation that stays true even if you measure the vectors’ components in different coordinate frames, such as those shown in figure 9.1. That’s because the scalar product itself is invariant under these coordinate transformations. You may remember from school that the equation ***a*** ∙ ***b*** = 0 can be interpreted as saying the vectors ***a*** and ***b*** are perpendicular to each other. Being perpendicular is a geometric property, and a vector is (part of ) a quaternion—so Tait argued that whole vectors and quaternions give clear and immediate geometrical interpretations.

![FIGURE 9.2. The symmetry of snowflakes. Plate 18 from Wilson A. Bentley, “Studies among the Snow Crystals during the Winter of 1901–2, with Additional Data Collected during Previous Winters,” *Monthly Weather Review* 30, no. 13 (1903): 607–16, https://doi.org/10.1175/1520-0493-30.13.607.](images/fig9_2.jpg){width="80%"}

Cayley, on the other hand, was interested in using invariance to help solve equations in pure maths. A simple example of an algebraic invariant is the discriminant, which, in the quadratic case we learn at school, is *b*^**2**^ − 4*ac*. It’s the expression under the square root sign in the formula for the solution of the general quadratic equation, *ax*^**2**^ + *bx* + *c* = 0, and as you can see in the next endnote, it stays the same if you change the equation by changing the coordinates in certain ways—for example, by replacing *x* with *x′* = *x* + *h*. In other words, the discriminant is invariant under the coordinate transformation *x′* = *x* + *h*. (As I indicated earlier, a coordinate transformation is just a set of equations showing how to relate the coordinates in the original frame with those in the new one—in this case, when the axes are horizontally translated by a distance *h*.)[^ch09n5]

What this all means for the final round of the vector wars is that while both men were exploring the idea of invariance, Cayley was interested in coordinates and coordinate transformations, whereas Tait was interested in whole quaternions and vectors. You can see why they remained “irreconcilable” on the best way of representing vectorial information!

Tait didn’t know it, but the coordinate-free, invariant way of writing equations that he championed, such as ***a*** ∙ ***b*** = 0, is the key link between vector analysis and tensor analysis. Cayley, however, responded just like William Thomson, saying you still need coordinates to do the calculations. So, he proclaimed—in his 1894 address to the Royal Society of Edinburgh—that just as the full moon is more beautiful than a dimmer moonlit view, “so I regard the notion of a quaternion as far more beautiful than any of its applications.” To emphasise the point, he added that a quaternion formula was like a pocket map, incredibly useful once you unfold it—once you translate the formula into its coordinate-based components. When Chisholm had first met Cayley just a couple of years earlier, she felt that “The fire was gone that they say had once gleamed from the eyes of the great mathematician.” But there was still fire enough in Cayley’s engagement with the vector wars.[^ch09n6]

<!--p195-->
![Peter Guthrie Tait in his study, demonstrating the physics of electricity; used with generous permission from the James Clerk Maxwell Foundation, Edinburgh.](images/p223.jpg){width="60%"}

Not to be outdone via literary analogies, Tait responded that rather than an unfolded pocket map, coordinate-based geometry was like a steam hammer, requiring expert manipulation so it would be useful rather than destructive. Quaternions, on the other hand, were so general they were “like an elephant’s trunk, ready at *any* moment for *anything*,” large or small— picking up a breadcrumb or strangling a tiger, as he put it. We don’t usually associate hyperbole with mathematicians—but Tait, with his hearty laugh and twinkling eyes, was a bit of a prankster.[^ch09n7]

• • •

<!--p196-->
Sparring over the relative advantages of coordinate-free vector and quaternion equations versus coordinate-based component ones continued for the next decade. It was an English-speaking debate, partly because Grassmann’s vectorial system hadn’t really taken off at that time, while quaternions were still virtually unknown outside Britain—and the young vector analysis mavericks Gibbs and Heaviside were English-speakers, too. But historian Michael Crowe suggests another reason for these long-running debates over the best notation to use for vectorial quantities. British mathematicians were aware that Leibniz’s symbolism for calculus was much better suited to calculations than was Newton’s, and that by the early nineteenth century this notational advantage had helped continental mathematics to leap ahead of that in Britain. So, they did not want the same thing to happen with Hamilton’s quaternions and vectors.[^ch09n8]

Whatever the reason for it, I’m emphasising this seemingly arcane dispute because it also shows how difficult it was for even the best mathematicians to appreciate the value of vectors in their whole, coordinate-free form, as opposed to their component forms. Yet it is mathematicians who will turn vectors into tensors (or rather, who will identify and generalise the invariance and algebraic structure underlying vectors). So, although the physicists were ahead of the game in the creation of vector analysis, it is mathematicians who will pave the way for Einstein’s masterpiece of physics, the (tensor) theory of general relativity.

Meantime, the next step in the story of vectors begins with the younger Einstein and his maths professor Hermann Minkowski, at the Federal Polytechnic School in Zurich. In 1900 Einstein completed his degree at the “Poly,” as it was affectionately known—but he was the only one of his small class of graduates not to be offered a job there, just as Maxwell hadn’t been offered a fellowship at Cambridge when he graduated. Maxwell had been deemed too careless, while young Einstein was far too sure of himself for his professors’ liking. (He was also Jewish, so anti-Semitism may have played a role in his lack of employment: Einstein himself thought so.[^ch09n9]) And so, in desperate financial straits and with a pregnant fiancée to care for, he took that legendary job at the Swiss patent office. It was during those years that he developed his special theory of relativity, in his spare time.

<!--p197-->
Before I talk more about this theory, and how it led to the next step in the story of vectors, let me acknowledge the ongoing controversy over Einstein’s relationship with his first wife, who’d been his fellow student at the Poly.

## REMEMBERING MILEVA MARIĆ

Much has been written about this tragic saga, in which the idealistic young students Einstein and Marić fell in love, secretly had (and gave up) a baby out of wedlock, married against parental disapproval, and finally separated, torn apart by Einstein’s growing fame and workload—and the fact that Marić, having repeatedly failed her exams, lost her confidence and her academic dreams, and increasingly took on all the day-to-day responsibilities for their two other children. I won’t detail the sad drama further—except to say that it was bigger than the two of them. Einstein famously behaved very badly during the breakdown of the relationship, but the seeds of that breakdown, sown when they were still students, also have to do with the patriarchal culture in which they were both trapped. This includes what I believe is the sexism of the examiners who failed Marić twice: she was the only girl in her class, frightened and pregnant at the time of her final attempt at the exams, yet she had excelled in her earlier school studies.

As for the popular belief that Marić “did Einstein’s maths for him,” or coauthored his 1905 relativity paper, as far as I know there is no confirmed evidence for it—and she herself never claimed it. She was certainly one of the first to believe in Einstein, as he struggled against the “old philistines” who kept refusing him an academic job—and her extensive study at the Poly made her, at the very least, a worthy and important sounding board for him. But the surviving letters between them suggest she didn’t have Einstein’s driving, creative scientific curiosity. Still, I can’t help thinking that if they’d been at university today, with our more open society and with contraception readily available, she would have gotten her diploma and the doctorate she was planning, and gone on to make her mark in science—and things between them might have turned out very differently.[^ch09n10]

<!--p198-->
![Mileva Marić-Einstein and Albert Einstein in Prague, 1912. ETH-Bibliothek Zürich, Bildarchiv.Photographer: Jan F. Langhans/Portr_03106. Public domain.](images/p226.jpg){width="80%"}

## THE SPECIAL THEORY OF RELATIVITY

Maxwell’s critics had complained he had no model for the hypothetical ether, the medium they assumed must surely be necessary for the transmission of light waves, just as sound waves need air. Instead, he’d focussed on describing concrete, measurable electromagnetic effects—and it was an astute move, because in 1887, the famous Michelson-Morley experiment “failed” to detect the ether via a state-of-the-art interferometer. The concept for the experiment was actually Maxwell’s, but it was Albert Michelson who designed the Nobel Prize–winning equipment needed to put it into practice. Michelson was the first American to win a Nobel, in 1907, and his experiment helped set the stage for the special theory of relativity. So, there’s a nice symmetry in the fact that the 2017 Nobel Prize for physics went to the founders of the Laser Interferometer Gravitationalwave Observatory (LIGO), which detected gravitational waves in 2015, as predicted by the general theory of relativity.

<!--p199-->
The idea behind the 1887 experiment was that if the ether existed, when Earth moved through it there would be an “ether wind”—just as you feel a breeze on your face when riding a bike on a still day. And just as you move faster swimming downstream in a river than upstream or across it, Michelson and his collaborator Edward Morley expected the speed of light would be fastest in the downstream direction—that is, “with” the ether wind. Maxwell had proposed using the timing of eclipses of Jupiter’s moons when the giant planet was seen from Earth at two nearly opposite positions in its orbit. Earth would then be moving toward Jupiter at one position and away from it at the other, so that the speed of the light from the Jovian system would be measured both “with” and “against” the ether wind.[^ch09n11] But Michelson and Morley used interference patterns—the same kind of patterns Thomas Young had used to show the wave-like nature of light in the first place. Specifically, they sent a beam of light downstream and another beam across-stream—that is, parallel to the direction of Earth’s motion and perpendicular to it; any difference in light speed would cause a phase difference between the two beams, which would show up in the interference pattern. But the researchers found no such difference. Which meant that the ether wind had no discernible effect on the speed of light. (Experiments have been ongoing ever since, to see if tiny speed differences can be found with better equipment—and some physicists speak of the possibility of a “quantum ether.” But the old mechanical idea of ether is out.)

By 1895, both George FitzGerald and Hendrik Lorentz had independently and ingeniously “explained” Michelson and Morley’s result by suggesting that objects—including measuring rulers—*physically shrank* when they were traveling parallel to the direction of the ether wind. Such a physical “length contraction” would shrink the *measurement* of light’s downstream speed, masking the supposed fact that it was “actually” faster.

<!--p200-->
In 1904, Lorentz made a brilliant start at applying this conjecture to Maxwell’s equations of electromagnetism, devising a set of coordinate transformations between the frame of a stationary observer and that of an observer moving with constant speed relative to the stationary one, like the swimmer in the river moving relative to an observer on the riverbank. These transformations were designed to show that the rulers in the moving frame shrank in just the right way to account for the Michelson-Morley result— and Henri Poincaré dubbed them the “Lorentz transformations” when he developed Lorentz’s ideas more fully in 1905. (We’ll see these transformations in fig. 9.3 below.) Years later, during a visit to the University of Leiden, Einstein met Lorentz and immediately fell under his spell. They developed a friendship, for Einstein thought Lorentz was both an extraordinarily lucid thinker—he’d won a Nobel Prize in 1902 for his work extending Maxwell’s theory in light of the discovery of electrons—and a person of perfect character. “The greatest and noblest man of our times,” Einstein called him, “a marvel of intelligence and exquisite tact.”[^ch09n12]

Einstein and Poincaré never warmed to each other, although they admired each other’s work. Poincaré was a superb mathematician—and a groundbreaking scientific philosopher to boot. In 1905 he was a famous fifty-one-year-old professor of mathematical astronomy and celestial mechanics at the Sorbonne in Paris. His 1905 paper on the Lorentz transformations was, in fact, a detailed theory of relativity, in the “special” case where the relative motion between observers (and therefore between their coordinate frames!) is constant. At the same time, twenty-six-year-old patent officer Einstein independently completed his own “special” theory of relativity. Marić had been captivated when she read his final draft, telling her husband, “It’s a very beautiful piece of work!” More than a century later, physicists still describe it as being beautiful: compared with the brilliant but convoluted complexities of Poincaré’s and Lorentz’s papers, Einstein’s is simpler and more intuitive. It is also the only one that ditched the old notion of a stationary ethereal medium for transmitting light through “empty” space, so it’s the only one that is fully relativistic, as we’ll see over the next couple of pages.[^ch09n13]

<!--p201-->
Since Poincaré accepted the idea that the ether existed—and that the Lorentz transformations provided the necessary “length contraction” to support the ether hypothesis—he’d taken this as his starting point. Einstein, on the other hand, began his analysis of relative motion by invoking two simple principles. First, the relativity principle, which says that if a stationary observer deduces a particular law of physics, then another observer, moving relative to the first one with constant speed, should deduce the same law. Otherwise, there wouldn’t be much point to physics, if the laws changed every time you changed your speed. Poincaré understood this, too—at least in the Lorentzian sense that Earth’s motion through the ether had no effect on light, and therefore no effect on Maxwell’s equations. What this means, as Lorentz, Poincaré, and Einstein all showed, is that the Lorentz transformations are, in fact, just the right coordinate transformations so that Maxwell’s equations have the *same form*, regardless of how the components of the electromagnetic field vectors are measured—from a fixed coordinate frame, or one that is moving relative to it with constant speed.

<!--p202-->
A simpler example of what “keeping the same form” means is Newton’s second law. Under the simple, so-called Galilean coordinate transformation shown in figure 9.3, the stationary observer deduces the horizontal force component to be *F* = *mẍ*, and the relatively moving observer deduces *F′* = *mẍ′*. The equation has the same form in each frame, and both observers agree that force equals mass times acceleration. You can see the calculations for this in the box above. (The box also shows calculations with the Lorentz transformations, showing the maths of “length contraction” in special relativity. We don’t really need these calculations for our story—we just need the *ideas* and conclusions—so feel free to skim or skip them.)

![FIGURE 9.3. Two frames *S* and *S′* are moving relative to each other in such a way that *S′* is moving to the right with constant speed *v* relative to *S*. So, let’s take *S* to be you standing on the sidewalk and *S′* to be someone driving by. If the axes initially coincided—if you and the car were level with each other at time *t* = 0—then after a time *t* the *S′* frame (the car) will have moved *vt* units to the right. In this case the relative motion is horizontal, so for any point P the *y* and *y′* coordinates (and in 3-D the *z* and *z′* coordinates too) will be the same; during the time *t*, however, *S′* has moved closer to *P*, so a measurement made *at that moment* will give *P*’s horizontal coordinate as *x* when measured in the *S* frame and *x′* (= *x* − *vt*) when measured with respect to the moving *S′* frame. This is the Newtonian/Galilean perspective, where time ticks away at the same rate for both observers. Even so, you can see that measurements of distance must be different in the different, relatively moving frames, and therefore speeds must be measured differently, too. You can see the mathematical consequences of this, from both the Newtonian and Einsteinian perspectives, in the related (and entirely optional!) box.](images/fig9_3.jpg){width="80%"}

::: {.infobox}

**COORDINATE TRANSFORMATIONS AND INVARIANCE**

<!--p203-->
CALCULATIONS FOR FIGURE 9.3

The coordinate transformations for the horizontal Galilean translation in figure 9.3 are:

::: {.displayeq}

*x′* = *x* − *vt, y′* = *y, z′* = *z, t′* = *t*. (1)

:::

It works well when *v* is much less than the speed of light. In such “everyday” situations, using (1) you find that Newton’s laws keep their form, regardless of whether they are measured in *S* or *S′*: for instance, if you deduce *F* = *mẍ*, then the person in the moving car deduces *F′* = *mẍ′*. That’s because *x′* = *x* − *vt*, and when you differentiate this twice with respect to *t′* (= *t*), you get *ẍ* − *v̇* (using Newton’s dot notation for the time derivatives); but since the speed is constant, the second term is zero and you have *ẍ′* = *ẍ*. So Newton’s second law applied to this component of force has the *same form* in both frames: *F* = *mẍ* = *mẍ′* = *F′*. In fact, the force components have the *same value* in each frame, so they are *invariant* under Galilean transformations; and since there’s no relative motion in the *y* and *z* directions, both observers will measure the same force components in those directions, too.

Although you both deduce *the same values of F and ẍ*, you *disagree* on the horizontal speed component *u* of a moving object such as a ball being thrown, because in *S, u* = *ẋ*, and in *S′, u′* = *ẋ′* = *ẋ* − *v*. So, the force and acceleration are invariant under Galilean transformations, but the speed is not.

<!--p204-->
Maxwell’s equations do not keep their form under the coordinate transformations (1). Instead, the *Lorentz transformations* are the right ones for the laws of electromagnetism. (In this case, the individual components and indeed the electric and magnetic field vectors are not invariant: e.g., if a charge is at rest in one frame, a relatively moving observer will see a magnetic field, but an observer in the charge’s frame will not. But the Maxwell equations linking the vectors *do* have the same form in each frame.) These transformations show that not just spatial measurements but also time measurements are relative—so you can no longer assume that *t′* = *t*. The Lorentz transformations for the set-up in the diagram are:

::: {.displayeq}

$$x'=\beta\left(x-vt\right),y'=y,z',\boldsymbol{t'}=\beta\left(\boldsymbol{t}-\frac{vx}{c^{2}}\right),$$ (2)

:::

where *c* is the speed of light (measurement units are often chosen so that *c* = 1), and

::: {.displayeq}

$$\beta=1/\sqrt{1-v^{2}/c^{2}}.$$ (3)

:::

These equations represent a so-called boost (of *S′* relative to *S*) in the *x*-direction, but the full Lorentz transformations can describe boosts in any direction, and rotations, too. And note that if *c* is infinite as implied in action-at-a-distance, then equations (2) are just equations (1).

If you were to measure the *length* of a moving car, at a given time you would have to measure simultaneously both its endpoints *x~a~* and *x~b~*, say, and compute *x~b~* − *x~a~*; using the Lorentz transformations (2) to compare your result with the actual (“rest”) length of the car in its own frame, *x~b~′* − *x~a~′*, you get

::: {.displayeq}

*x~b~′* − *x~a~′* = β(*x~b~* − *x~a~*)

:::

(because *t~b~* − *t~a~* = 0 for a simultaneous measurement). Since β > 1 (because the denominator is less than 1 for nonzero *v*), you see that the actual car length is greater than the one you measured. In other words, your measurement suggests the car had “shrunk.” Unlike Lorentz’s idea, there is no *physical*, molecular shrinking of the car itself, but a shrinking in *measurements* used in calculations. But these measurements do have real, testable consequences in the stationary observer’s physics.

Similarly, the relativity of the time measurement is why Earth-based observers deduce that time slows down for fast-moving airplane or spaceship travelers—or GPS satellites—just as distances shrink. (Both special and general relativity are needed to account for time in GPS measurements, as we’ll see.)

As Einstein realised, however, you can also interpret figure 9.3 as saying that *S* is moving relative to *S′*—so it is moving to the left, and its speed is −*v*. So, the Lorentz transformations from this point of view are:

::: {.displayeq}

$$x=\beta\left(x'+vt'\right),y=y',z=z',\boldsymbol{t}=\beta\left(\boldsymbol{t'}+\frac{vx'}{c^{2}}\right).$$ (4)

:::

And this time, it is measured lengths in *S*’s frame that contract.

**GROUPS**

Groups are important tools for studying symmetries, such as invariance. In this case, the “elements” of the group are coordinate transformations, and they form a group if they all obey a simple set of rules, which I’ll illustrate for the Lorentz transformations (although we won’t need these details in this story).

The fact that the Lorentz transformations (2) have an “inverse,” (4), and also an “identity” element (that is, an element that is unchanged by the transformation—in this case, the transformation when *v* = 0), is key to knowing that they form a mathematical “group.” Closure (the idea that all possible transformations in the group are of the same type) and associativity (of the group “product”—in this case, the composition of two transformations) are the other key features.

:::

Similarly, if you deduce $\nabla\times E=-\frac{\partial B}{\partial t},$ one of Maxwell’s equations that we saw earlier, then using the Lorentz transformations you’d see that a moving observer deduces an equation with exactly the same form. So, you’d both agree that the changing magnetic field on the right-hand side of the equation gives rise to the curl of the electromagnetic field on the left. The same goes for the other whole-vector Maxwell equations.

<!--p205-->
In other words, if an equation representing a law of physics has the same form even when its components are measured in different frames, then all observers will deduce the same physics (and the same maths, as we saw with the invariant equation ***a*** ∙ ***b*** = 0). That’s the principle of relativity in action.

It’s also another example of invariance—in this case, the invariance of the *form* of the equations. (Such form-invariant equations are also called “covariant.”)[^ch09n14]

Einstein’s *second* principle was that the speed of light in empty space is independent of the motion of the source (which is what physicists seemed to have found experimentally). Together these two principles imply that the vacuum speed of light, *c*, is a universal constant.

From these two principles alone, Einstein had *derived* the Lorentz transformations from scratch, in a completely general way. By contrast, Poincaré had *assumed* Lorentz’s “length contraction” was a real physical effect, and then rederived the Lorentz transformations by showing that they left the form of Maxwell’s equations invariant. (Woldemar Voigt found something similar back in 1887, so these ideas were “in the air.” We’ll hear more about Voigt in chap. 11.) But Einstein had no need of hypotheses about the ether and no need to suppose any objective *physical* shrinking of rulers took place—rather, you get different measurements from different, relatively moving frames of reference. I showed a simple example of this in the box of calculations for figure 9.3, but the key fact, as Einstein made clear, is that the effect is reciprocal: *each* observer can consider themselves at rest and the other one to be moving. In other words, each observer would measure the other’s ruler contracting, because they’re each moving relative to the other. Lorentz and Poincaré, by contrast, believed that only one observer was “really” moving (relative to the all-pervading ether)— the one whose ruler “really” shrinks. That’s why Einstein’s was the only fully relativistic theory.

## FOUR-DIMENSIONAL SPACE-TIME NEEDS FOUR-DIMENSIONAL VECTOR ANALYSIS

<!--p206-->
The Lorentz transformations include time as well as the three spatial directions (as you can see in equation (2) in the box above with fig. 9.3). So, when the term “relativity” is mentioned today, one of the first things many people think of is the four-dimensional nature of space-time. Yet the idea of a “fourth dimension” had been tantalising the public since the 1880s. True, Hamilton had created a mathematical four-dimensional space when he defined quaternions in 1843—but as we saw with the vector wars, not even mathematicians could agree on its worth. So, while Tait, Cayley, Heaviside, and the others debated the academic merit of components versus whole vectors versus quaternions in the 1880s and 1890s, the possibility of a literal four-dimensional space was being tackled in popular books—such as mathematician Charles Howard Hinton’s *Scientific Romances* and *A New Era of Thought*.

Hinton—who was George Boole’s son-in-law—was also a spiritualist, and spiritualists loved the idea of a mysterious other dimension. These ideas had so penetrated popular culture that when Grace Chisholm stood for the oral exam related to her doctoral dissertation (which included *n*-dimensional spaces), one of her examiners mentioned the spirit idea, and asked what *she* meant by “higher dimensions.” She replied that for her, it was simply a way of speaking about certain abstract relations in mathematics. She got her doctorate with highest honours, although obviously she’d fielded much harder questions than this![^ch09n15]

<!--p207-->
As for Hinton, he hadn’t lost his mind completely to the spirits, for he also focussed on trying to visualise four-dimensional geometric objects, such as “hypercubes.” You can think of a cube as a “hypersquare,” a sequence of two-dimensional squares that forms a 3-D shape—that is, a cube—so a hypercube would be an arrangement of cubes in 4-D space. In 1954, Salvador Dali famously drew on this idea in his crucifixion painting “Corpus Hypercubus,” in which the cross is made of cubes—but seventy years earlier, Hinton had inspired the schoolmaster Edwin Abbott to write his legendary 1884 *Flatland: A Romance of Many Dimensions*. Hinton also inspired his wife’s sister Alicia Boole Stott, Boole’s youngest daughter. Stott discovered several mind-bending results in four-dimensional geometry, including a collection of physical models she made of various sections of an imagined 4-D structure made of six *hundred* tetrahedrons, which together can be thought of as the three-dimensional surface of the four-dimensional analogue of an icosahedron. The mind boggles at such visual geometric imagination.[^ch09n16]

Then, in 1895—the same year that Lorentz found the Lorentz transformations to explain the Michelson-Morley experiment—H. G. Wells published his famous novel *The Time Machine*, in which he claimed that *time* was the fourth dimension. Brilliantly imaginative as Wells was, however, words alone were not enough to make this idea stick—to make it real. It took Lorentz, Poincaré, and Einstein to uncover the mathematical properties of such a four-dimensional construct—and it took Einstein to make it “real” by suggesting testable predictions to check his theory. (One of those predictions led him, completely unexpectedly, to deduce that *E* = *mc*^**2**^.) So, when people hear the words “fourth dimension” today, they tend to think of Einstein, not Wells—and Einstein did it with the language of maths.

As far as *vector* language is concerned, Poincaré worked entirely in components, but Lorentz also used whole-vector notation and vector calculus. In his special relativity paper Einstein, like Poincaré, wrote all his equations in terms of components, and although his coordinates (*t, x, y, z*) represented both time and space, he did not yet speak of space-time.

<!--p208-->
In principle Einstein could have used quaternions, which have four components, to represent quantities in his four-dimensional coordinate system.[^ch09n17] He’d likely never heard of quaternions, though—his maths professor, Minkowski, had said no one outside Britain used them—and perhaps he didn’t even know much vector algebra, although Minkowski did teach that. As a student Einstein had figured that he needed a single focus if he was to succeed in unraveling nature’s secrets, and this focus was firmly on physics. Besides, he felt there were so many topics to choose from in maths that he was overwhelmed. So, although he admired Minkowski, he’d cut quite a few of his classes so he could study on his own the physics he wasn’t being taught in lectures—including Maxwell’s theory. Minkowski, on the other hand, thought Einstein was simply “a lazy dog who never bothered about mathematics at all.” By contrast, when Minkowski himself had been a seventeen-year-old student, he’d won a prestigious award for his mathematical work—and had secretly given the prize money to an impoverished classmate.[^ch09n18]

Minkowski certainly ate his words in 1905: “Oh that Einstein, always missing lectures—I really would not have believed him capable of it!” But for all its conceptual elegance, compared with Poincaré’s paper young Einstein’s *was* a little rough around the edges, mathematically speaking. In fact, Minkowski, now professor of pure mathematics at Germany’s prestigious Göttingen University, told his students, “Einstein’s presentation of his deep theory is mathematically awkward—I can say that because he got his mathematical education in Zurich from me.”[^ch09n19]

For instance, Poincaré was fluent in the mathematical language of invariance and group theory, and used it to show something surprising: the four-dimensional expression

::: {.displayeq}

*x*^**2**^ + *y*^**2**^ + *z*^**2**^ − (*ct*)^**2**^

:::

doesn’t change if you transform the coordinates via Lorentz transformations. In other words, it is *invariant* under this “group” of transformations. (Actually, Poincaré used *c* = 1 here, and today it is common to choose units so that *c* = 1 in the Lorentz transformations and other equations of relativity.) Einstein found the same result, although he didn’t express it in such a sophisticated way. Formal “group theory” was pioneered by Évariste Galois—the impetuous prorevolutionary agitator and foolhardy lover who famously died in a duel in 1832, when he was just twenty years old. Cayley was one of the many others who made important early contributions to group theory, whose key features I listed at the end of the boxed caption to figure 9.3. But it was Minkowski who really made sense of this unusual expression.

It was unusual because, as Poincaré had pointed out, physicists were used to quadratic expressions where all the terms were added. For example, the length of a position vector is found from its components via Pythagoras’s theorem (as you can see by extending fig. 0.2 to 3-D and representing the components simply in terms of the coordinates):

::: {.displayeq}

$$a=x\boldsymbol{i}+y\boldsymbol{j}+z\boldsymbol{k}\Rightarrow\left|a\right|=\sqrt{x^{2}+y^{2}+z^{2}}.$$

:::

<!--p209-->
![Hermann Minkowski, ca. 1896 (when Einstein was his student). ETH-Bibliothek Zürich, Bildarchiv/Photographer unknown/Portr_02711. Public domain.](images/p237.jpg){width="60%"}

This is the formula for measuring lengths and distances in flat, 3-D Euclidean space, and it is invariant under coordinate transformations such as the rotations in figure 9.1. Minkowski realised that the analogous concept in special relativity is the expression:

::: {.displayeq}

$$\sqrt{x^{2}+y^{2}+z^{2}-\left(ct\right)^{2}},$$

:::

which Poincaré and Einstein had shown is invariant under Lorentz transformations. This expression looks rather like the Euclidean distance formula, but it is not the measure of distance in ordinary space. Rather, it is the “distance” in what Minkowski called “space-time.” In other words, it is the interval between “events” in space-time, rather than the distance between points in space. You can see what it means physically in the endnote, but here I’m focusing on its mathematical analogies with the Euclidean distance formula.[^ch09n20]

<!--p210-->
The space-time used in special relativity is now called “Minkowski space-time”; it is a four-dimensional extension of flat Euclidean space, so it is also called “flat” space-time, as opposed to the curved space-times of general relativity. A distance or interval measure is called a “metric,” and a measure with the form $\sqrt{x^{2}+y^{2}+z^{2}-\left(ct\right)^{2}}$ is called the Minkowski metric in his honour. (We’ll see a more precise definition later.) The concept of “world lines” is due to Minkowski, too. In Euclidean geometry, objects are located at a *point* in space; but even if the object is stationary in space, it is moving in time, so its location in space-time is represented by a *line* through the point—a line that is parallel to the time axis, and which gets longer as each second ticks by.

Minkowski first put forward his new concept of space-time in a lecture he gave in November 1907. A year later, he developed this more fully in his famous talk, “Space and Time,” which opened with the memorable proclamation, “Henceforth space by itself, and time by itself, are doomed to fade away into mere shadows, and only a kind of union of the two will preserve an independent reality.” He gave Einstein the credit for recognising the true, two-way principle of relativity, politely dismissing Lorentz’s “fantastical” hypothesis of a literal, physical contraction of moving objects. The confident tone of this address—on paper, at least—belies the fact that the gentle Minkowski used to turn deep red and stammer in front of an audience.[^ch09n21]

The key thing for our story, though, is that Minkowski then made a start at developing *four-dimensional vector analysis*. At one point he even tried quaternions, because you can divide with quaternions but not vectors, as we saw earlier. In the end, he found the ordinary, Heaviside-Gibbs–style vector analysis more flexible.

In ordinary vector analysis, which takes place in the flat Euclidean space used in diagrams such as figure 9.1, the length of a vector can also be written in terms of its scalar product with itself:

::: {.displayeq}

$$a=x\boldsymbol{i}+y\boldsymbol{j}+z\boldsymbol{k}\Rightarrow\left|a\right|=\sqrt{\boldsymbol{a}\cdot\boldsymbol{a}}=\sqrt{x^{2}+y^{2}+z^{2}}.$$

:::

In (flat) space-time, Minkowski defined the scalar product by analogy, using the interval metric: if a 4-D vector ***a*** has components (*x, y, z, t*), then the scalar product is

::: {.displayeq}

***a*** ∙ ***a*** = *x*^**2**^ + *y*^**2**^ + *z*^**2**^ − (*ct*)^**2**^.

:::

<!--p211-->
More generally, and using modern notation (and choosing units so that *c* = 1), while the scalar (or dot) product of two 3-D vectors is

::: {.displayeq}

***a*** ∙ ***b*** = *a*~1~*b*~1~ + *a*~2~*b*~2~ + *a*~3~*b*~3~,

:::

the 4-D dot product in Minkowski space-time is

• • •

(Today, it’s also common to denote the time component with a suffix 0 instead of 4.) Later mathematicians will generalise this to any kind of space—curved or flat, 3-D, 4-D, or *n*-D—defining the scalar product via the metric, in a beautiful example of the power of mathematical analogies.

In another paper, Minkowski came close not just to 4-D vector analysis; he dipped his toe into tensor analysis, too. Tragically, he never got the chance to develop his work fully, or to know that today his name lives on in the “Minkowski metric.” Not long after he gave space-time to the world, he died suddenly, after surgery for appendicitis. He was only forty-four. When his old college friend and Göttingen colleague, David Hilbert, stood in front of his students to tell them the sad news, he wept.[^ch09n22]

• • •

At first, Einstein wasn’t impressed with what his former professor had done to his theory—at that stage he preferred coordinates and components to whole, coordinate-free vectors. So, it was Minkowski’s friend Arnold Sommerfeld who took up his ingenious space-time invention and began to explore 4-D analogues of scalar and vector products, and of the vector calculus operations of divergence, curl, and grad. Sommerfeld, who was then a professor of theoretical physics at the University of Munich, opened his 1910 paper, “On the Theory of Relativity I: Four-Dimensional Vector Algebra,” with a tribute to Minkowski, “the friend who suddenly passed away.”

<!--p212-->
Sommerfeld had been a member of Germany’s “Vector Commission,” which was established in 1903. In the wake of Britain’s vector wars, the commission’s goal was to settle on a standard vector notation—although its founder, Göttingen maths professor Felix Klein, thought that all it achieved was a proliferation of notations! Klein was a fan of Heaviside (and Maxwell), but he had also been impressed with Grassmann’s *Ausdehnungslehre*. He’d heard about it soon after Grassmann’s son Justus enrolled as a maths student at Göttingen in 1869—Justus had proudly brought along copies of his father’s book, earmarked for two professors who had expressed interest in Grassmann’s work. One of these professors was Alfred Clebsch, whose enthusiasm for Grassmann also inspired his colleague Klein. Two decades later, Klein—along with Gibbs—was instrumental in the publication of Grassmann’s collected works.[^ch09n23] At the same time, Sommerfeld had become first Klein’s assistant at Göttingen and then his collaborator. He moved to Munich in 1906 and had taken with him the interest in vectors— and invariants—that Klein had nurtured.

In his two 1910 papers on relativity, Sommerfeld introduced the term “four-vector” for 4-D vectors in space-time. He emphasised the significance of the invariance of the space-time interval, for it expresses the constancy of the speed of light (as you can see in the endnote[^ch09n24]). Poincaré, Lorentz, and Einstein knew this, too, of course. But Sommerfeld also pointed out the importance of invariant symbolism in adapting Maxwell’s equations to space-time, noting “the complicated calculations” that Lorentz and Einstein had used in order to show that the ordinary component form of Maxwell’s equations stayed the same under these transformations. Instead, Sommerfeld aimed to build on Minkowski’s work, showing how to write these equations in invariant four-dimensional form.

He didn’t find a 4-D analogue of the 3-D “Heaviside” vector form of the equations shown in chapter 8; rather, he showed that what we now call “tensors” are needed to express the form-invariance of the 4-D Maxwell equations.

## YOU CAN SAY EVEN MORE WITH TENSORS!

<!--p213-->
Tensors were a new concept then, whose intriguing origin we’ll explore soon—but to get the flavor, this is how Sommerfeld explained them. With vectors you are exploring the geometry of *lines* (or arrows); for example, in three dimensions, perpendicular lines are characterised by the vector equation ***a*** ∙ ***b*** = 0, and parallel lines by ***a*** × ***b*** = 0 (as you can see from the geometric definitions of the dot and cross products given in the caption to fig. 9.1). But sometimes you also need to describe *planes*, and they have an additional feature: *orientation* in space. This is defined by the direction of the plane’s “normal,” which is represented by a unit vector perpendicular (or normal) to the plane. But to get a clearer idea of what planes have to do with tensors, we can go back to a surprising source: Maxwell’s 1873 *Treatise*.

Imagine a box submerged in water—an idealised version of the hull of a ship, perhaps. It keeps its shape under the pressure of the water because of the balance of forces acting on each of its faces. All sorts of rigid bodies, from bridges and airplanes to tiny crystals, balance these “stress” forces. (“Stress” is the force per unit area.) There are also many situations where the forces may not balance—in deformable or elastic materials, of course, but engineers also need to account for potential additional stress impacts, such as heavy traffic on a bridge or heavy seas battering a ship. Then there are situations where you want to move or rotate the body, so again you want a net *imbalance* of forces. Maxwell’s friend Thomson was one of the pioneers in the mathematical study of these situations, which he analysed back in 1856 in a paper on elasticity. Even earlier, Augustin Cauchy had published his foundational 1828 paper on stress in bodies in equilibrium.[^ch09n25] Maxwell, however, wanted to analyse the forces on a magnetised object immersed in an electromagnetic field. By analogy with the immersed box, he considered the forces acting on each face of a little cube of the magnetised body. (In other words, he considered a “volume element” that can be integrated through the whole body.) Thomson and Cauchy had used a similar approach. But Maxwell did something special, not only by extending these analyses to electromagnetism but also by representing stress with a symbol with *two indices*.

<!--p214-->
In maths an “index” refers in this context to a label, not a power. For example, the components of vectors are generally written with one index, as in ***a*** = (*a*~1~, *a*~2~, *a*~3~); the indices refer to the three axes from which the components are measured. Maxwell recognised that stress was an example of “physical quantities of another kind which are related to directions in space, but which are not vectors.” He said that’s because in 3-D space a vector has three components, but a stress needs nine of them (as you can see in fig. 9.4). So, he wrote the components of stress as *P~hk~*, explaining that the first label, *h*, indicates the surface on which the stress is acting—it is the one whose normal is parallel to the *h*-axis—and the second label shows the direction of the force producing the stress. There are three choices for *h*— one for each dimension in space, that is, one for each coordinate axis—and three choices for *k*. That’s nine possible combinations, one for each of the nine components.[^ch09n26]

![FIGURE 9.4. The fundamental stress components acting on the faces of a cube. Maxwell noted that if *P~hk~* = *P~kh~*, the stresses won’t produce a rotation (he was interested in the rotation produced by magnetism—as expressed in his curl equation). Indeed, the diagram suggests that if, say, *P~yx~* > *P~xy~*, the right-hand face will be pulled forward, and the cube will begin to rotate.](images/fig9_4.jpg){width="80%"}

<!--p215-->
What Maxwell had done here was to give a concise definition of the components of a single quantity he referred to simply as “stress,” but which is now called the “stress tensor”—just as the components (*a*~1~, *a*~2~, *a*~3~) form a single vector, ***a***. The fascinating thing about this is that tensors hadn’t yet been invented—at least, not as mathematical objects on a par with vectors. Yet Cauchy and Thomson had come close to the idea, too, although they didn’t have Maxwell’s concise and general notation.

![FIGURE 9.5. You need two vectors to make a stress tensor. First, the vector ***n*** giving the direction of the surface on which the stress is acting—I’ve labeled it with an *x* to indicate that here the relevant component of the normal is parallel to the *x*-axis. Second, the vector giving the strength and direction of the force: the label *y* indicates that the relevant component for the force acting on this face is in the direction parallel to the *y*-axis.](images/fig9_5.jpg){width="50%"}

From a modern point of view, the key idea here is that you need two vectors to form a stress tensor: one to represent the direction of the surface on which the stress is acting, and one to represent the force itself. You can see this in figure 9.5, which is another way of expressing Maxwell’s definition of his components *P~hk~*. When the mathematicians enter the field, they’ll turn the essence of this concept into a much more precise and more general definition of a tensor. But already you can see that with nine components, a tensor such as stress can store much more information than a 3-D vector can.

By 1910 when Sommerfeld was writing, tensors hadn’t yet found their way into the mainstream, but he understood that they are far more versatile than just ways of representing stresses. And they don’t necessarily have anything to do with planes, for they can be adapted to any number of dimensions and applications. Sommerfeld referred in passing to Grassmann, but his focus was on his friend Minkowski, and on rewriting Maxwell’s equations in the language of space-time. To do this, he followed Minkowski in rewriting the components of ***E*** and ***B*** as two-index quantities—giving essentially the modern tensor form of Maxwell’s equations.[^ch09n27]

<!--p216-->
We’ll see these beautiful equations later. First, though, we need to delve further into the evolution of tensors. In particular, we’ll find out how they encode and extend the idea of invariance—and why Einstein needed them for his masterpiece. But we’ll also go back in time a little, to find out what non-Euclidean geometry has to do with our story. For the road to tensors is a long one—and, as we’ve seen with vectors, too, it was built with creative insights from many surprising directions.

<!--stats: p=80 fig=8 eq=11 note=0-->
