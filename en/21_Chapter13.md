<!--p304-->
# (13) WHAT HAPPENED NEXT

As we saw with Einstein’s thought experiment about falling people and accelerating elevators, a surprising amount of intuition goes into finding a law about how nature works. Logic alone is simply not enough. Yet even when a theory’s equations work spectacularly well, it is often necessary for others to come along and tighten up the mathematical foundations, or to shine a light more closely on the theory’s assumptions. Which is why David Hilbert and Felix Klein needed Emmy Noether.

Noether arrived in Göttingen in 1915. She’d earned her doctorate in 1907 at Erlangen, where Klein had taught earlier, and she was an expert on invariant theory—so Klein and Hilbert had invited her to Göttingen, hoping she could help sort out their questions about general relativity and energy. And help them she did, for in 1917 Klein told Hilbert, “You know that Miss Noether advises me continually regarding my work, and it is only thanks to her that I have understood these questions.”[^ch13n1]

<!--p305-->
Despite Einstein’s legendary intuition, he’d struggled when he tried to interpret the relationship between mathematical covariance—the idea that if you write a tensor equation, it will keep the same form when you transform to another set of coordinates—and the physical principles of relativity and equivalence that had guided him to his theory. His struggle helped later mathematicians sharpen the distinction between transformations of coordinates, frames of reference, and points or events, and between relativity as a theory of invariance and symmetry groups as opposed to one of covariance—but if you’re confused by such subtleties, don’t worry: these distinctions are still being debated today.[^ch13n2] All that matters, really, is that Einstein’s tensor equations give a marvelously accurate description of gravity, from which so many extraordinary consequences have been correctly predicted. So, what I want to focus on here are the issues that Noether helped resolve, during the debates that took place immediately after Einstein published his theory at the end of 1915, and his longer 1916 overview, *The Foundation of the General Theory of Relativity*.

By the way, this 1916 paper is a master class in Ricci’s tensor calculus. Because this language was still new to most physicists and mathematicians, Einstein took great care in setting out, economically but clearly, the tensor rules we saw in chapter 11.

In November 1915 Einstein had finally ended up with the conservation of energy-momentum equation *T* ^μν^~;ν~ = 0, as we saw in the previous chapter. He’d come at it via a circuitous route that was different from Hilbert’s, and in May 1916 he asked if Hilbert thought there might be some deep principle underlying their two separate approaches. Hilbert replied that he thought there probably was, and that he’d already asked “Miss Noether” to investigate the issue. Hilbert and Klein, and colleagues such as Einstein, had the highest respect for Noether, yet her presence was so singular they couldn’t help calling her “Miss” rather than “Dr.” Perhaps they thought it was more polite than just using her surname, as they often did among themselves.

<!--p306-->
The questions Klein and Hilbert were trying to resolve concerned the physical and mathematical meaning of the energy-momentum conservation law in general relativity. The traditional route to conservation equations in ordinary mechanics had been the calculus of variations. This involves minimising the “action”—that is, the integral of a “Lagrangian” *L*, which is a function of position and velocity. Leonhard Euler and Joseph-Louis Lagrange had pioneered this method, and then our vector pioneer William Rowan Hamilton introduced a useful alternative, in which *L* is expressed in terms of momentum rather than velocity (so it is a new function, now called the Hamiltonian, denoted by *H*). Sometimes it is easier to work in terms of momentum rather than velocity, but either way, when *L* and *H* are expressed in terms of kinetic and potential energy, the equation of motion arising when the integral is minimised has a solution that gives the usual conservation of energy equation. The details of this method aren’t important here: for an individual particle the equation of motion found in this way is equivalent to Newton’s second law of motion, and we’ll see shortly how this leads to conservation equations.

Meantime, to find their conservation of energy-momentum equations, Hilbert had used an elegant Lagrangian approach while Einstein had used a mix of tensors and a Hamiltonian. They were breaking new ground, because first they had to figure out how to define *gravitational* energy—and how to choose the right *L* or *H* to express this new kind of energy. When that was done, there was still a nagging question: How did the resulting equation, *T* ^μν^~;ν~ = 0, gel with the traditional idea of energy-momentum conservation?

## EMMY NOETHER AND THE CONSERVATION OF ENERGY-MOMENTUM

Through 1916 and 1917, Einstein, Hilbert, Klein, and Noether exchanged ideas on this brand-new problem of gravitational energy. Each added to the debate, and several others joined in—notably Klein and Hilbert’s former student Hermann Weyl. But it was Noether who tied it all together, in the famous “Noether theorems” proved in her 1918 paper “Invariante Variationsprobleme.”[^ch13n3] These two theorems relate conservation laws to “symmetries.” And symmetries, as we’ve seen, relate to “invariance”—the idea that certain things are unchanged when you change your frame of reference. We also saw this kind of invariance in figures 9.1 and 9.3, and of course it is the defining feature of tensor equations. Since invariance has to do with things remaining the same, it also has to do with conservation—for if a physical quantity doesn’t change, it is “conserved.”

<!--p307-->
In ordinary mechanics—the study of the way objects move under forces—this connection had been known since Lagrange. For example, we’ve seen that gravitational force ***F*** can be expressed in terms of a potential *V*: ***F*** = ∇*V*. But since Newton’s second law says that the force acting on an object equals the rate of change of the object’s momentum vector, ***p***, we have,

::: {.displayeq}

$$F\frac{dp}{dt}=\nabla V\equiv\frac{\partial V}{\partial x}i+\frac{\partial V}{\partial y}j+\frac{\partial V}{\partial z}k.$$

:::

In terms of components, this equation gives $\frac{\partial p_{x}}{dt}=\frac{\partial V}{\partial x}$, and similarly for the *y* and *z* components. Now for the invariance, and let’s consider the group of coordinate transformations that are translations by various amounts in the *x*-direction. If the potential is invariant under these transformations, then it doesn’t change—it has the same value at the point (*x, y, z*) as it does at (*x* + *a, y, z*):

::: {.displayeq}

*V*(*x* + *a, y, z*) = *V*(*x, y, z*), for every value of *a*.

:::

Since it doesn’t matter which value of *x* is used, *V* must be independent of *x*. Which means $\frac{\partial V}{\partial x}$, and this, in turn, means that

::: {.displayeq}

$$\frac{\partial p_{x}}{dt}=\frac{\partial V}{\partial x}\Rightarrow p_{x}=C$$, where C is the constant of integration.

:::

And *this* means that the *x*-component of the momentum is constant—it is conserved.

The same equations of motion, and the same “conservation” laws, are found using the Lagrangian or Hamiltonian methods, as I mentioned. This would be like using a sledgehammer to crack a walnut for this simple case, but these methods are often easier for complicated situations with many particles.

<!--p308-->
At the simplest level of her theorems, Noether showed that this is a general result: when a function is independent of a particular variable, it indicates that something is conserved. In general relativity, for example, we saw in figure 12.1 that free-falling objects move along geodesics analogous to the straight lines of Euclidean geometry, so the equation of motion is an equation about geodesics—and we saw in chapter 12 that geodesics depend on the metric that describes the curved space-time. We also saw that Einstein chose the components of the metric to play the role of the potential, analogous to *V*. So, like the Newtonian example we just saw, if there is a frame in which the metric tensor *g*~μν~ is independent of a particular space-time coordinate, then that component of momentum is conserved along the particle’s path. In space-time, though, “momentum” is a 4-D vector: its spatial components are the ordinary spatial momentum components, but the time component is defined to be the energy.[^ch13n4]

I’ve been talking about the energy and momentum of an individual moving object here, not the energy-momentum tensor used to describe the energy and momentum carried by a gravitational field—but labeling the time component of the particle’s momentum as “energy” is analogous to what we saw for the time components *T*~41~, *T*~42~, *T*~43~, *T*~44~ in chapter 12. So, there are two conservation issues to address: conservation of a moving object’s energy and momentum in a gravitational field—as we’ve just seen, this is related to the symmetry (or invariance or coordinate-independence) of the potentials, *V* and *g*~μν~—and conservation of the energy-momentum of the gravitational field itself, which we’ve seen is *T* ^μν^~;ν~ = 0. Noether was the first to show mathematically that we’re actually talking about different types of conservation law.

I’ve sketched the essence of how Noether did it in the endnote.[^ch13n5] The upshot is that in classical mechanics *and* special relativity, the resulting conservation laws are clearly physical—they arise from physical conditions such as those described by Newton’s laws. They also involve divergences, as we saw for electromagnetism in chapter 12.[^ch13n6] The equation *T* ^μν^~;ν~ = 0 seems to involve a divergence, but as Noether proved, it is not a physical divergence but a mathematical analogy.

<!--p309-->
This is not to say that *T*^**μν**^ is unphysical in general relativity. True, there are problems in defining local energy density, and unless there are certain symmetries in the space-time, there’s no global conservation law. Still, an observer can define energy density at a point, and the total gravitational energy of a system can be defined, and so can the energy flux carried away by gravitational waves.[^ch13n7] So *T*^**μν**^ plays a vital role in the study of cosmology and gravitational radiation, for example. And, whatever you want to call it, the equation *T* ^μν^~;ν~ = 0 is needed to find the relationship between energymatter sources and the curvature of space-time.[^ch13n8]

![Emmy Noether, circa 1900. Photographer unknown. Wikimedia Commons, public domain.](images/p337.jpg){width="50%"}

## IT’S A LOT SIMPLER WITH TENSORS

We saw in chapter 12 that the gravitational field equations are:

::: {.displayeq}

$$R_{\mu v}-\frac{1}{2}g_{\mu v}R=KT_{\mu v}.$$

:::

<!--p310-->
And we met, in chapter 11, covariant derivatives, and the fact that you can raise and lower tensor indices without changing their essential content[^ch13n9]—so I’m going to write the gravitational field equations with upstairs indices, and then take the covariant derivative of both sides:

::: {.displayeq}

$$\left(R^{\mu v}-\frac{1}{2}g^{\mu v}R\right)_{;v}=kT^{\mu v}_{;v}.$$

:::

Now, both Einstein and Hilbert found that conservation of energymomentum means the right-hand side of the equation is zero. Which means the left-hand side must be zero too. What neither Einstein nor Hilbert knew, nor Klein nor Noether, was that the left-hand side is zero quite independently of the conservation equation. That’s because of what are known as “the contracted Bianchi identities”:

::: {.displayeq}

$$\left(R^{\mu v}-\frac{1}{2}g^{\mu v}R\right)_{;v}=0.$$

:::

(The plural is because this “equation” is really four equations, one for each component μ. The repeated index ν indicates a sum.) A mathematical “identity” is an equation that is always true—because it must be true, by definition. The full Bianchi identities follow directly from the definition of the Riemann tensor, as Ricci had known in the 1880s, although it was his nemesis Luigi Bianchi who first published the result, when he rediscovered the identities in 1902. (Bianchi won the Italian Royal Mathematics Prize that Ricci had entered in the 1890s, and Bianchi was a none-toosympathetic judge when Ricci entered again in 1901.) As we saw in chapter 12, the Ricci tensor is formed from the contracted Riemann tensor, so that’s how the “contracted” Bianchi identities give rise to this equation.[^ch13n10]

<!--p311-->
Noether had spelled out the relationship between conservation and symmetries, and had shown in detail why *T* ^μν^~;ν~ = 0 is just a mathematical analogy to traditional conservation laws—but Hilbert and Klein had assumed that this conservation equation forced $\left(R^{\mu v}-\frac{1}{2}g^{\mu v}R\right)_{;v}=0$ to be true. So, they regarded this latter equation as a consequence of the variational (Lagrangian and Hamiltonian) methods that had led Einstein and Hilbert to the conservation equation. In fact, as Tullio Levi-Civita noted in 1917, it’s much simpler to argue the other way, for the conservation equations follow directly from the field equations, via the tensorial Bianchi identities![^ch13n11]

By the way, I mentioned in chapter 12 that Einstein had first tried *R*^**μν**^ = *kT*^**μν**^ for his field equation. If you differentiate both sides of this equation, you get R^μν^ ~;ν~ = kT^μν^~;ν~, and Einstein rightly rejected this as unphysical.[^ch13n12] But the Bianchi identities show immediately that this is the wrong equation if conservation of energy-momentum is to hold, so that *T* ^μν^~;ν~ = 0. Had Einstein known these identities, he’d have saved himself from quite a few headaches!

• • •

Noether’s theorems are far more complicated than I’ve indicated here, of course. They were overlooked for many decades, because aside from their mathematical complexity, their significance lies in their generalising a host of already-known conservation results. These known results had been built up slowly and separately over the centuries, and it took physicists some time to appreciate the importance of Noether’s discovery that a single fundamental principle united mathematical symmetries and physical conservation laws. But the generality of this principle also means that her theorems are more widely applicable than general relativity: in recent times they have found applications from quantum mechanics to elasticity to fluid mechanics, for example, and in pure mathematics and numerical analysis. Back in 1918, though, even the link with general relativity was not fully understood.

In fact, it wasn’t until 1924 that Jan Schouten and Dirk Struik highlighted the connection between Noether’s Lagrangian identities and the beautiful tensor identities $\left(R^{\mu v}-\frac{1}{2}g^{\mu v}R\right)_{;v}=0$. Noether used the symmetries of the Lagrangian, while the Bianchi identities depend on the symmetries of the Riemann tensor (which remains invariant when various combinations of its indices are interchanged, just as *g*~μν~ and *T*~μν~ are invariant when you swap the order of their indices: *g*~μν~ = *g*~νμ~ and *T*~μν~ = *T*~νμ~).[^ch13n13]

<!--p312-->
Struik’s interest in relativity had arisen early, for while he was a student in Leiden, Einstein had given a guest lecture there—Struik’s professor was Einstein’s close friend Paul Ehrenfest, who’d worked with Klein at Göttingen. Half a century later Struik still remembered the excitement of Ehrenfest’s lectures, where science felt “alive”—an exciting, contemporary activity emerging “from conflict and debate” between famous living scientists and mathematicians, including, Struik recalled, Klein, Abraham, and Einstein.[^ch13n14]

If Struik’s phrase “conflict and debate” brings to mind Marxist dialectics, you’d be right: Struik later became a historian of science, and in 1936 he cofounded the Marxist journal *Science and Society*, which is still going today. He was motivated by the idea that science both shapes and is shaped by society, and that scientists have a social as well as a scientific responsibility for their work—an idea that has finally found its way into science classes and ethics committees.

## NOETHER’S STRUGGLE FOR ACCEPTANCE

In 1924–25, Struik and his new wife, Dr. Ruth Ramler, who was also a mathematician, spent a year at Göttingen. “You had to have a thick skin to survive,” he recalled, for “the Göttingen mathematicians were known for their sarcastic humor.” Einstein would have agreed: “The people of Göttingen sometimes strike me,” he’d declared, “not as if they want to help one formulate something clearly, but as if they want only to show us physicists how much brighter they are than we.” Struik noted that Noether, “who was shy and rather clumsy, was often the butt of some joke.” But it wasn’t just sexism, for Struik added that “the good-natured Erich Bessel-Hagen” was also treated to the same “humor.”[^ch13n15]

<!--p313-->
Sexism was, however, the reason Noether found it hard to forge an academic career. In 1915, with the support of Klein and Hilbert, she had applied for habilitation as a private tutor or *Privatdozent*. I mentioned earlier that when Einstein presented his special relativity paper in his own first step on the academic ladder, it was rejected as “incomprehensible.” But Noether was rejected because of misogyny. At Göttingen, mathematics was part of the philosophy faculty, so most of the members had no idea of Noether’s mathematical brilliance—they just saw that she was a woman, and that it was unthinkable that a woman be allowed to teach. “What will our soldiers think when they return to the University and find that they are expected to learn at the feet of a woman?” Hypatia could have told them a thing or two about that! As it was, Hilbert responded that he didn’t see that “the sex of the candidate” was an issue: the university is “not a bathhouse,” he retorted.[^ch13n16]

In May 1918, after Einstein had studied a paper of Noether’s on invariants, he wrote to Hilbert saying how impressed he was with the generality of her approach, adding, “It would have done the Old Guard at Göttingen no harm to be sent back to school under Miss Noether. She really seems to know her trade!” Later that year he studied her conservation theorems hot off the press, and he was so impressed he wrote to Klein, “I once again feel that refusing her the right to teach is a great injustice.” He offered to approach the relevant ministry himself if Klein was too busy. Fortunately, the war finally ended, and a new, more democratic government was established in Germany—and in June 1919, Noether was finally allowed to become a *Privatdozent*.[^ch13n17]

Her habilitation thesis had been her 1918 conservation theorems, but in her lifetime, she was much more famous for her later work on abstract algebra—she was so cutting-edge she’s been dubbed “the mother of modern algebra.”[^ch13n18] But she was also the first woman to play a role in relativity theory, and she’s been an inspiration to many mathematically inclined young women who have come after her. I remember my first international conference on general relativity, where there were about four hundred men and ten women—including University of Paris professor Yvonne Choquet-Bruhat, who was a living legend for proving, from the 1950s on, some landmark theorems in general relativity. We are still a minority, but things are improving all the time, and women are increasingly visible. For example, in 2022, the Australian National University’s Professor Susan Scott won the European Academy of Sciences’ Blaise Pascal Medal for her work on gravitation, including her role in the 2015 detection of gravitational waves. And on a related topic, Katie Bouman was a Harvard postdoctoral fellow when she famously played a key role in devising the algorithms that led to the first direct image of a black hole in 2019.

<!--p314-->
Black holes and gravitational waves are predictions of general relativity, although Einstein himself was ambivalent about the possibility of their physical existence. But that doesn’t matter: it’s all there in those extraordinary little tensor equations,

::: {.displayeq}

$$R_{\mu v}-\frac{1}{2}g_{\mu v}R=KT_{\mu v}.$$

:::

At least, it’s there for those who know how to solve these equations, and today this often requires the use of numerical algorithms and computer power. Tensors such as the Ricci and metric tensors are there at the heart of it, although not necessarily in the numerical methods themselves. But for those of us working on exact solutions, those tensor indices and their symmetry properties help lighten the load of our computational tasks.

## THE MEANING OF “PARALLEL”

There’s another interesting tensor problem that was solved in the wake of general relativity. In the parallelogram rule for vector addition, which we saw back in figure 3.1, vector ***A*** is added to ***B*** by translating or “transporting” it to align with the end of ***B***, all the while keeping ***A*** parallel to itself. Alternatively, you can move ***B***, keeping *it* parallel to itself. On a curved surface such as that of a globe, you cannot move vectors around like this: as I’ve mentioned, meridians of longitude that are parallel at the equator are no longer so at the poles. Evidently, then, the usual idea of parallelism makes sense only locally, when a curved line is approximately straight.

![FIGURE 13.1. Parallel transporting a vector that starts out being vertical at point *A* is unproblematic in flat space—but on a curved surface, the notion must be carefully defined. I’ve explained this a little more in the related box.](images/fig13_1.jpg){width="60%"}

<!--p315-->
It was Levi-Civita who figured out, in 1917, how to “parallel transport” vectors along curved surfaces—and he did it with tensors. His “parallel transport” equation (in the box) helps show how much the curvature causes two initially parallel geodesics to deviate with respect to each other—like the converging meridians on a globe. In a hugely curved space-time such as that around a black hole, the geodesics converge so quickly and drastically that you would be crushed if you came too close. (The inverse square law shows that you’d also be torn apart, because the gravity changes so dramatically over the distance between your head and your feet!)

::: {.infobox}

**PARALLEL TRANSPORT AS A WAY OF CHARACTERISING CURVATURE**

To see how Levi-Civita’s idea of parallel transport relates to curvature, it’s easiest to start with the idea in flat space. Imagine a flat piece of paper with a triangle drawn on it (as in fig. 13.1). Hold a pencil—standing in for a vector—vertically at the point *A*, and then, keeping it parallel to itself, move it along the flat page to the point *C*. Now do the same thing, but travel to *C* in the opposite direction, so you’re transporting the vertical pencil along the line from *A* to *B* and then up to *C*. No surprises there—the pencil remains vertical all the time. The same thing happens if you take an intrinsic, ant’s-eye view, keeping your vector in the 2-D plane of the page: begin with, say, a vector tangent to the side *AC*. It will remain parallel to itself when you transport it from *A* to *C* in either direction.

Now imagine holding the pencil vertically at a point *A* on the “equator” of a ball or orange. In this vertical position the pencil is tangent to the ball at *A* and pointing upward. Move it up toward the pole at *C*, keeping it tangent to the sphere but holding it straight (make sure you don’t twist it). Now go the other way, parallel transporting the pencil along the curve from *A* to *B* and then up to *C*. This time the pencil—or vector—ends up at an angle of 90 degrees from the same vector transported directly from *A* to *C*. This is noncommutativity in action!

<!--p316-->
Hamilton would be amazed that his “shocking” notion that mathematical operations are not always commutative has found so many applications—this time, as a measure of curvature. It is the kind of intrinsic curvature our 2-D ant-alien could discover, simply by crawling along the surface with a pencil and noting how it changed direction at *C*.

**CALCULUS, TOO**

When you differentiate vectors in ordinary vector analysis, intuitively speaking you compare the vector at two nearby points and divide by the distance between them—and you implicitly assume the vector remains parallel when you calculate its value at one point and then the other. So, vectors must be able to be moved or “transported” along a curve in some sort of parallel way, if we are to understand how to define derivatives in curved spaces (that is, what Ricci called “covariant” derivatives). It’s not surprising, then, that Levi-Civita’s idea of parallel transport connects covariant derivatives and curvature.

It turns out that the definition of the parallel transport of a vector ***V*** along a curve with tangent vector ***U*** is *U*^μ^*V*^ν^~;μ~ = 0. (The semicolon denotes the covariant derivative.)

:::

As so often happens in science and mathematics, someone else had independently discovered the same ideas as Levi-Civita, at around the same time—although he hadn’t yet published them. This someone was Jan Schouten. His colleague Dirk Struik recalled the day Schouten had come bursting into his office waving Levi-Civita’s paper. “He also has my geodesically moving systems,” Schouten told Struik, “only he calls them parallel.” Struik recalled that Levi-Civita’s approach was much simpler than Schouten’s; still, he mused, “Few people realize that Schouten barely missed getting credit for the most important discovery in tensor calculus since its invention by Ricci.”[^ch13n19]

<!--p317-->
Struik worked with Levi-Civita in 1923 and described him as vivacious, gentle, and charming. The influential Scottish algebraic geometer William Hodge wrote that Levi-Civita was “one of the personally best known and best liked mathematicians of his time.”[^ch13n20] And like Struik, Levi-Civita had married a maths graduate, Liberia Trevisani—his former student. She had hoped to teach mathematics, but ended up traveling the world with her husband, who was in great demand on the lecture circuit. Tragically, all that would change in the 1930s, when the Fascists and Nazis began their persecution, and Levi-Civita, Einstein, Noether, and so many other Jewish academics were stripped of their academic positions, if not of their lives.

The likes of Arnold Sommerfeld and David Hilbert were appalled at the direction their country had taken between the wars. Soon after the first war, Arthur Eddington, a leader of the 1919 eclipse expedition, had seen hope in the symbolism of a British team confirming a German theory—Einstein’s light-bending prediction. But hostility between the former enemy nations still simmered, and when Italian mathematicians organised the first postwar mathematics congress in 1928, they took pains to invite their German colleagues. Many German mathematicians refused to go, but when Hilbert triumphantly led a delegation of his countrymen into the opening session, they received a standing ovation. Hilbert addressed the gathering in terms that would certainly have pleased Eddington. There are no limits in mathematics, he said, including national ones. “It is a complete misunderstanding of our science to construct differences according to people and races. For mathematics, the whole world is a single country.”[^ch13n21] It’s a noble sentiment—and it is true in the sense that international collaboration has always been important in the advancement of mathematics, which is now an international language. But war changes everything. In 2022, for example, in the wake of Vladimir Putin’s disastrous invasion of Ukraine, there was a similar debate among mathematicians, after a journal refused to publish papers from Russian institutions, and the International Mathematics Union stripped St. Petersburg of its right to host the 2022 International Congress of Mathematicians. Some felt as Hilbert did, that there should be no discrimination, and others felt that sanctions sent a message about institutional *and* individual responsibility for war (such as Hilbert and Einstein had shown when they refused to sign the kaiser’s waiver of responsibility during World War I).[^ch13n22]

• • •

<!--p318-->
Levi-Civita’s invariant tensor definition of parallelism was important for the maths of tensors—especially for understanding the idea of covariant differentiation. But in 1929 Einstein began corresponding with the French mathematician Élie Cartan on the possibility of spaces with a broader definition of parallelism. Cartan is the one who did the most to put all the ideas of his predecessors—including the long-neglected Hermann Grassmann, whom Cartan had studied well—into the modern “differential form” version of Ricci’s tensor calculus. It was Cartan who, for example, clarified the idea of one-forms as duals of vectors, which I mentioned briefly in chapter 11.

The content of the letters between Cartan and Einstein has to do with Cartan’s idea of “absolute” parallelism, a notion that allowed torsion or twisting of “parallel” vectors. As I mentioned with the pencil illustration in figure 13.1, this isn’t allowed in Levi-Civita’s definition of parallel transport—and therefore it isn’t used in general relativity (because nontwisting parallel transport relates to the covariant derivatives in Einstein’s equations). Einstein had hoped adding torsion might be a way to unify electromagnetism and gravity—but like Hilbert and Gustav Mie, he didn’t succeed. Nonetheless, space-times with torsion, such as those in the Einstein-Cartan theory, are still being explored today—as a possible way of avoiding the Big Bang singularity, for example, or to account for the intrinsic spin of matter.

Although the details of the Einstein-Cartan correspondence are beyond my scope here, a cursory glance shows that tensors were the mathematical language they were speaking. It also shows the respectful way the two men interacted. Einstein, who was fifty in 1929, wrote such things as, “I am very fortunate that I have acquired you as a coworker. For you have exactly that which I lack: an enviable facility in mathematics.... I am both touched and delighted that you have taken so many pains over the problem.” And sixty-year-old Cartan wrote, “I’m very proud my letters may be of some interest to you.... I consider it to be a privilege,” he added, “that you are willing to spare me some of your time, which is so precious for science.”[^ch13n23]

<!--p319-->
Einstein’s letter of June 13, 1931, is especially poignant. He informs Cartan that his old friend Marcel Grossmann has published a paper “rudely” criticising the idea of absolute parallelism, but he wants Cartan to know that Grossmann is seriously ill with advanced multiple sclerosis. “I tell you all this to urge you not to answer him publicly,” Einstein said loyally, adding that Grossmann was too ill to be accountable for the unpleasant tone and misguided content of his critique. When Grossmann died five years later, after his long and debilitating illness, Einstein wrote movingly to his widow, telling her what a treasured friend Marcel had been.[^ch13n24]

Grossmann may never have realised what a crucial role he had played in putting tensors on the map. But since 1975 his legacy in general relativity has been honoured in the Marcel Grossmann Meetings, which, every three or four years, bring together researchers from all over the world to discuss the latest developments. And in honouring Grossmann, these meetings also honour—implicitly, at least—the mathematical brilliance of Ricci and Levi-Civita, and the genius of Einstein.

<!--stats: p=48 fig=2 eq=7 note=0-->
