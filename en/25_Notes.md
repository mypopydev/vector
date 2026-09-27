<!--p343-->
# NOTES

## PROLOGUE

[^ch00n1]: Letter from William Rowan Hamilton to P. G. Tait, published in the preface to the third edition of P. G. Tait, *An Elementary Treatise on Quaternions* (Cambridge: Cambridge University Press, 1890).

[^ch00n2]: Maxwell didn’t use the term “vector field,” but that’s what he’d created (as he made clear a few years later, in his 1873 *Treatise on Electricity and Magnetism*); I’ll explore what this means—and how it influenced later physicists—in subsequent chapters.

[^ch00n3]: *Ancient tabular mathematics*: see, e.g., Eleanor Robson, “Mathematical Cuneiform Tablets in the Ashmolean Museum, Oxford,” *SCIAMVS* 5 (2004): 2–65; Duncan J. Melville, “Computation in Early Mesopotamia,” in *Computations and Computing Devices in Mathematics Education before the Advent of Electronic Calculators*, ed. A. Volkov and V. Freiman (Switzerland: Springer Nature, 2018), 25–47. Melville highlights the difficulties in interpreting such ancient documents and their intended uses; and Robert Middeke-Conlin points out that the debate over the utility of some of the Mesopotamian mathematical tablets is ongoing, in “The Mathematics of Canal Construction in the Kingdoms of Larsa and Babylon,” *Water History* 12 (2020): 105–28. Daniel Mansfield’s 2021 study, however, adds significant clarity to some of these interpretations; see his “Plimpton 322: A Study of Rectangles,” *Foundations of Science* 26 (2021): 977–1005.

<!--p344-->
[^ch00n4]: I’m indebted for the information on Mesopotamian land use and surveying, and on Plimpton’s role, to Mansfield, “Plimpton 322.” Mansfield discovered the Pythagorean nature of Si427, and he also gives new insights on Plimpton 322 as well as details about Mesopotamian multiplication tables. On his claims for Mesopotamian trigonometry, however, see, e.g., Evelyn Lamb, “Don’t Fall for Babylonian Trigonometry Hype,” *Scientific American* (blog), August 29, 2017.

[^ch00n5]: *Australian indigenous astronomy*: Duane Hamacher, “Stories from the Sky: Astronomy in Indigenous Knowledge,” *The Conversation*, December 1, 2014; Ray P. Norris, Cilla Norris, Duane W. Hamacher, and Reg Abrahams, “Wurdi Youang: An Australian Aboriginal Stone Arrangement with Possible Solar Indications,” *Rock Art Research* 30, no. 1 (2013): 55–65.

[^ch00n6]: Some of Ptolemy’s brilliant but now mostly lost sources are Eudoxus of Cnidus, perhaps the first to begin the process of geometric modeling in astronomy, and who pioneered the protocalculus method of exhaustion that we’ll meet in chap. 2; Eratosthenes of Cyrene, who apparently used a basic kind of latitude and longitude, and who deduced the size of the Earth extraordinarily accurately, given he used a shadow stick and simple measuring rods; Hipparchus of Nicaea, who seems to have been the first to systematically use a 360° circle to make precise geometrical representations of planetary motion, and whose maths and astronomy were so good that he discovered the precession of the equinoxes; and Apollonius of Perga, who used a kind of post-hoc coordinate system in his mathematical analysis of conics, and whose epicycle and eccentric models of planetary motion Ptolemy built directly upon.

[^ch00n7]: For example, if you were traveling, say, *northeast* at 35 mph, your vector would point in the direction at 45° to the axes, but its components would be such that when you add them using Pythagoras’s theorem, the magnitude is still 35. So, it would be the vector $\left(\frac{35}{\sqrt{2}},\frac{35}{\sqrt{2}}\right)$.

    The vector $\left(\frac{35}{\sqrt{2}},\frac{35}{\sqrt{2}}\right)$ is found from fig. 0.2, and the fact that when working out the components you need $\sin 45^{\circ}=\cos 45^{\circ}=\frac{1}{\sqrt{2}}$; if you’re rusty on trigonometry, you can take a look ahead at fig. 3.4 to see why we need sin 45° and cos 45° for the vertical and horizontal components. Then, using Pythagoras’s theorem, you have $\left(\frac{35}{\sqrt{2}}\right)^{2}+\left(\frac{35}{\sqrt{2}}\right)^{2}=35^{2}$, so the vector is $\left(\frac{35}{\sqrt{2}},\frac{35}{\sqrt{2}}\right)$ and the magnitude is 35.

<!--p345-->
[^ch00n8]: The components of four-velocity are defined by analogy with ordinary velocity, as the derivatives of the (space-time) coordinates with respect to (proper) time. The proper time is the directly measurable “clock time,” that is, from a clock at rest with respect to the observer.

[^ch00n9]: *The Mad Hatter parody conjecture* refers to a consequence of one of Hamilton’s new types of multiplication (noncommutativity, which we’ll see in chaps. 1 and 4); it was suggested by Victorian literature expert Melanie Bayley, “Alice’s Adventures in Algebra: Wonderland Solved,” *New Scientist*, December 16, 2009. Michael Brooks followed up the story with Bayley in his *The Art of More* (Melbourne: Scribe, 2021), 194–96.

    Brooks and Bayley paint Dodgson as a conservative, mediocre mathematician (see also, e.g., Michael Deakin, “Lewis Carroll—Mathematician?,” *Function* 18, no. 1 [February 1994]: 10–18)—one who couldn’t have understood Hamilton’s work. This may well be true. Dodgson/Carroll’s mathematical fame today, however, rests not on work published in his lifetime but on posthumously discovered later manuscripts on methods of voting and on symbolic logic (in which he used absurd propositions and symbolic algebra to teach the rules of logic); cf. Francine Abeles, “Logic and Lewis Carroll,” *Nature* 527 (November 19, 2015): 302–4; Amirouche Moktefi, “Why Make Things Simple When You Can Make Them Complicated? An Appreciation of Lewis Carroll’s Symbolic Logic,” *Logica Universalis* 15 (2021): 359–79—and, for a taste of Carroll’s logical puzzles, see, e.g., the University of Hawaii website http://math.hawaii.edu/~hile/math100/logice.htm.

    Note, however, that in Carroll’s *Symbolic Logic* (New York: Dover, 1958; originally published 1897, three decades after *Alice*), he sets up a *commutative* algebra of symbolic logic (e.g., 35, 70): Carroll’s equation is about logic, not algebra, but it is interesting that he chose to emphasise “commutativity”— perhaps he did have a problem with Hamilton’s noncommutative multiplication. Or perhaps he simply wanted to distinguish his symbolic logical propositions from vector products.

## CHAPTER 1

[^ch01n1]: In the preface to his *Lectures on Quaternions*, Hamilton said he was led to quaternions because he wanted to “connect *calculation* with *geometry*,” and to move these calculations “from the plane to space.” Later he shows how to do 3-D rotations; see *Lectures on Quaternions* (Dublin: Hodges and Smith, London: Whittaker, and Cambridge: Macmillan, 1853), 269 (art. 282).

<!--p346-->
[^ch01n2]: Melanie Bayley (“Alice’s Adventures in Algebra”) pointed out this and other examples that suggest, to her, that Carroll was parodying Hamilton. But it’s possible that Carroll might simply have been distinguishing the rules of logic from those of Hamilton’s algebra.

[^ch01n3]: *Hamilton’s electrical analogy* is from a letter to his son Archibald (quoted in Michael J. Crowe, *A History of Vector Analysis* [Notre Dame, IN: University of Notre Dame Press, 1967], 29–30). He gave a similar description to P. G. Tait in an 1858 letter: https://www.tcd.ie/library/manuscripts/blog/tag/moon-landing/. The commemorative art installation is by Emma Ray; see the website of the Royal Irish Academy, which cocommissioned the work, and especially the YouTube video of the preparation and installation, at https://www.google.com/search?client=safari&rls=en&q=Commemorative+art+installation+Hamilton+Broombridge+Luas&ie=UTF-8&oe=UTF-8#fpstate=ive&vld=cid:a9bfbdde,vid:1nQct3p3184.

[^ch01n4]: While visiting the Old Library at Trinity College, Dublin, Armstrong paused beside a marble bust of Hamilton and explained to his guide how quaternions help spacecraft navigation: Estelle Gittins, July 19, 2019, https://www.tcd.ie/library/manuscripts/blog/tag/moon-landing/.

[^ch01n5]: I have adapted a diagram—possibly attributed to Pythagoras—given in T. L. Heath, *Translation of Euclid’s Elements* (Cambridge: Cambridge University Press, 1925) reproduced in John Stillwell, *Mathematics and Its History* (New York: Springer-Verlag, 1989), 7. For Euclid’s more sophisticated proof, see Carl Boyer, *A History of Mathematics*, rev. Uta Merzbach (New York: John Wiley and Sons, 1991), 108.

[^ch01n6]: There are different versions, but see, e.g., Library of Congress, https://www.loc.gov/item/2021666184/.

[^ch01n7]: Modern mathematicians tend to prefer defining *i* as the (principal) solution to *x***2** + 1 = 0, rather than specifying it as $\sqrt{-1}$; in other words, *i* is usually defined in terms of its square, *i***2** = −1, rather than as a square root. That’s because the latter can lead to conundrums such as this:

::: {.displayeq}

$$-1=i\times i=\sqrt{-1}\times\sqrt{-1}\sqrt{\left(-1\right)\left(-1\right)}=\sqrt{1}=\pm 1,$$

:::

    and if you take the positive root, you have −1 = 1, which is clearly wrong!

[^ch01n8]: *Descartes on imaginary numbers*: Brian E. Blank, “Book Review: An Imaginary Tale by Paul Nahin,” *Notices of the AMS* (November 1999): 1233.

<!--p347-->
[^ch01n9]: Al-Khwārizmī quoted in Boyer, *History of Mathematics*, 229; his geometrical way of completing the square, 231. Translation of *Al-jabr* … , and geometric example: Raymond Flood and Robin Wilson, *The Great Mathematicians* (London: Arcturus, 2011), 46–47.

[^ch01n10]: For more about Harriot’s extraordinary life and work, see my *Thomas Harriot: A Life in Science* (New York: Oxford University Press, 2019), and the references therein. Note that his posthumous book, *Praxis*, was put together by his friends, but evidently they were not such good mathematicians as he: his papers offer more sophisticated work than that which they published, including the use of imaginary numbers.

[^ch01n11]: For a fascinating history of the evolution of algebraic symbolism, see Joseph Mazur, *Enlightening Symbols: A Short History of Mathematical Notation and Its Hidden Powers* (Princeton, NJ: Princeton University Press, 2014).

[^ch01n12]: In addition to his special relativity and *E* = *mc***2** papers, in 1905 Einstein also published two important papers on Brownian motion and the size of molecules as well as a pioneering paper on the quantum theory of light. For an introductory overview, see my *Young Einstein and the Story of E = mc^2^* (Sydney: Ligature, 2014).

[^ch01n13]: This problem is from tablet CBS 43, as translated in Eleanor Robson, “Mathematical Cuneiform Tablets in Philadelphia, Part I: Problems and Calculations,” *SCIAMVS* 1 (2000): 11–48; for my illustrative purpose, I have changed the right-hand side of the problem to 21—the tablet (shown on 39) has 41, but as Robson says (42), the symbols are not entirely clear on the tablet, and as deciphered do not yield the kind of simple integer or two-place (in the sexagesimal system) solution used at the time. My diagram of the Old Babylonian geometrical method of completing the square is adapted from p. 42.

[^ch01n14]: *Canals, etc*.: Robert Middeke-Conlin, “The Mathematics of Canal Construction in the Kingdoms of Larsa and Babyon,” *Water History* 12 (2020): 105–28.

[^ch01n15]: Note that earlier mathematicians—including the legendary early twelfthcentury Persian poet Omar Khayyam, who was also a mathematician—had found a purely geometrical way of solving some cubic equations with positive roots via the intersection of two curves: Boyer, *History of Mathematics*, 241; Flood and Wilson, *The Great Mathematicians*, 49. On al-Ṭūsī, see J. J. O’Connor and E. F. Robertson’s MacTutor entry for him, at https://mathsh istory.st-andrews.ac.uk/Biographies/Al-Tusi_Sharaf/.

<!--p348-->
[^ch01n16]: *Cardano’s underlying algorithm* (based on Tartaglia’s) for solving an equation of the form *x*^**3**^ = *cx* + *d* is this: choose new variables *u, v* and set *x* = *u* + *v, uv* = c/3. Put these into the original equation, and you’ll get *u*^**3**^ + *v*^**3**^ = *d*; eliminate *v* and this becomes a quadratic equation in *u*^**3**^, which can be solved using the quadratic formula. Put this solution for *u*^**3**^ into *u*^**3**^ + *v*^**3**^ = *d* and solve for *v*^**3**^. Take the cube roots of *u*^**3**^ and *v*^**3**^ to find *u, v*, and hence *x* = *u* + *v*. It’s ingenious, and all created without the modern symbolism that makes it easier to keep track of your thought processes. The example I gave, *x*^**3**^ = 6*x* + 40, and Cardano’s algorithm for solving it—together with his geometric completion of the cube—is in chap. 12 of his *Ars Magna*, reprinted in R. Laubenbacher and D. Pengelley, “Algebra: The Search for an Elusive Formula,” in *Mathematical Expeditions*, Undergraduate Texts in Mathematics (New York: Springer, 1999), 230; https://doi.org/10.1007/978-1-4612-0523-4_5.

[^ch01n17]: For instance, Schrödinger’s equation describes the dynamics of fundamental particles such as photons, electrons, and other subatomic particles—and it contains *i*. Electromagnetic waves, too, are easier to handle mathematically using the complex form, so *i* is behind all sorts of modern technology.

[^ch01n18]: *Wallis on Harriot*: quoted in Jacqueline Stedall, “Rob’d of Glories: The Posthumous Misfortunes of Thomas Harriot and His Algebra,” *Archive for History of Exact Sciences* 54, no. 6 ( June 2000): 490. *Harriot first to algebraically (symbolically) solve cubics*: The great mathematician Lagrange first made this observation; see Seltman, “Harriot’s Algebra: Reputation and Reality,” in *Thomas Harriot*, vol. 1, *An Elizabethan Man of Science*, ed. Robert Fox (Aldershot: Ashgate, 2000), 185.

[^ch01n19]: Similarly, a quadratic equation has two solutions, a quartic has four solutions, and so on. The German mathematician Peter Roth suggested this link between degree and number of solutions at around the same time (in his 1608 *Arithmetica Philosphica*), but he did not write his equations symbolically or explore complex roots. A rigorous proof of the “fundamental theorem of algebra” suggested by Harriot’s “factor” construction came two hundred years later—Harriot himself didn’t claim as much. An example of his use of factors and symbols to get complex solutions is found in, e.g., British Library Manuscript 6783, fols. 157, 156.

<!--p349-->
[^ch01n20]: Following Euler (or figs. 3.4 and 3.6 and related discussion in chap. 3), you can write a complex number *a* + *ib* as *r*(cos θ + *i* sin θ) = *re^i^*^**θ**^, where $r=\sqrt{\left(a^{2}+b^{2}\right)}$ and θ is found from the inverse cosine and sine accordingly. From De Moivre’s theorem (or simply from the index laws), the cube root of this number is $\sqrt[3]{\left(re^{i\theta}\right)}=r^{1/3}e\frac{i\left(\theta+2k\pi\right)}{3}$, where *k* = 0, 1, 2 gives the three different roots. Applying this to $\sqrt[3]{\left(2+11i\right)}+\sqrt[3]{\left(2-11i\right)}=r^{1/3}e\frac{i\left(\theta+2k\pi\right)}{3}+r^{1/3}e\frac{i\left(-\theta-2k\pi\right)}{3}=2r^{1/3}\cos\frac{\left(\theta+2k\pi\right)}{3}$, you get the three solutions of Cardano’s equation, $x=4,-2+\sqrt{3},-2-\sqrt{3}$. It is a bit fiddly, but all the steps use only senior high school or freshman university maths.

[^ch01n21]: *Harriot’s quotation*: British Library Additional Manuscript 6783 fol. 186. See also Jacqueline Stedall, “Notes Made by Thomas Harriot on the Treatises of François Viète,” *Archive for Exact Sciences* 62, no. 2 (March 2008): 179–200.

[^ch01n22]: *Seltman’s quotation* is in her “Harriot’s Algebra,” in *Thomas Harriot*, vol. 1, *An Elizabethan Man of Science*, ed. Robert Fox (Aldershot: Ashgate, 2000), 184, my emphasis. Regarding Harriot’s use of complex and negative solutions, Seltman gives a fine analysis of the superiority of Harriot’s manuscripts to the posthumously published *Artis Analyticae Praxis*, which was put together by his less capable friends, on the basis of what they understood from his papers. This includes their rejection of Harriot’s use of imaginary and negative numbers.

## CHAPTER 2

[^ch02n1]: Sound waves are changes of air pressure, and the pebbles’ shock waves travel through the water in the pond—but light travels from the sun through *empty space*. So what could possibly be rippling in a light wave? The mysterious, undetectable “ether” had long been postulated, but Maxwell would eventually provide the answer (chap. 6). Mary Somerville’s recollection is in her memoir, *Personal Recollections from Early Life to Old Age of Mary Somerville*, edited by her daughter Martha Charters Somerville (London: John Murray, 1873), 132.

[^ch02n2]: *Optical tweezers* use the laser-beams’ radiation pressure to move the tiny particles, and this is another example of a mathematical prediction: it was Maxwell who mathematically predicted the existence of radiation pressure, which was experimentally confirmed three decades later, in 1901. *Maxwell on radiation pressure: Treatise on Electricity and Magnetism* (Oxford: Clarendon Press, 1873, 3rd edition (1891) reprinted in 1954 by Dover), 2:440–41 (arts. 792–93).

[^ch02n3]: Ahmes wrote what is now known as the Rhind papyrus, after the collector who bought it in Egypt in the 1850s; it’s now in the British Museum.

[^ch02n4]: *On Newton*: Richard S. Westfall, *Never at Rest: A Biography of Isaac Newton* (Cambridge: Cambridge University Press, 1980); Westfall also wrote the entry on Newton in the *Encylopaedia Britannica*.

[^ch02n5]: The description of Leibniz is from the first page of the introduction to Philip P. Wiener, ed., *Leibniz Selections* (New York: Charles Scribner’s Sons, 1951).

<!--p350-->
[^ch02n6]: *Attempts at defining infinitesimals and limits*: Leibniz: “A differential is less than any given quantity,” and “If one preferred to reject infinitesimally small quantities, it was possible instead to assume them to be as small as one judges necessary in order that they should be incomparable and the error produced should be of no consequence, or less than any given magnitude.” Newton: “Quantities, and the ratios of quantities, which in any finite time converge continually to equality, and before the end of that time approach nearer to each other than by any given difference, become ultimately equal.”

    *Modern definition*: Defining *f*(*x*) in a suitable domain, $\lim_{x\to\alpha}f\left(x\right)=L$ if, given any number ε > 0, we can find a number δ > 0 such that *f*(*x*) satisfies *L* − ε < *f*(*x*) < *L* + ε whenever *a* − δ < *x* < *a* + δ. For limits where *x* approaches infinity, we have $\lim_{x\to\infty}f\left(x\right)=L$ if for any number ε > 0 we can find a number *M* such that *L* − ε < *f*(*x*) < *L* + ε when *n* > *M*. This definition arises from work by the likes of Augustin Louis Cauchy and Karl Weierstrass two centuries after Newton’s attempt at defining a limit.

[^ch02n7]: *Wallis acknowledged Harriot* (and also Oughtred and Descartes) in his *Arithmetica Infinitorum*—quoted in Boyer, *The History of Calculus and Its Conceptual Development* (New York: Dover, 1959), 170; see also 168–69. For more details on Wallis’s debt to and exceptionally informed admiration of Harriot, see Stedall, “Rob’d of Glories,” 481–90. *Newton’s first published account of his calculus* was in *Principia*, bk. 2. Although he gave most of his proofs geometrically, he sometimes gave the algorithms of calculus in terms of algebraic symbolism, e.g., in bk. 2, sec. 2, lemma 2. When he gave geometrical diagrams, he sometimes used symbolic algebra to explain the algorithm or construction, as in bk. 2, prop. 10, problem 3. Even in bk. 1, calculus concepts are often clearly evident in the relevant geometrical constructions (such as his proof of prop. 39). In his first manuscripts on calculus, however, he’d used algebra rather than geometry.

<!--p351-->
[^ch02n8]: *Wallis vs. Fermat et al*.: Jacqueline Stedall, “John Wallis and the French: His Quarrels with Fermat, Pascal, Dulaurens, and Descartes,” *Historia Mathematica* 39 (2012): 265–79. *Descartes and Harriot*: Wallis’s claims were exaggerated, but they were not original to him for there is some uncertainty about whether or not Descartes had seen Harriot’s *Praxis* before he wrote his famous *La géometrie*; of course independent codiscovery is not uncommon, and Descartes went much further than Harriot, but Descartes was notoriously vague about his sources, and even his compatriot, Viète’s editor Jean Beaugrand, noted similarities between Descartes’s work and Harriot’s. See Stedall, “Rob’d of Glories,” 488–89, and Jacqueline Stedall, “Reconstructing Thomas Harriot’s Treatise on Equations,” in *Thomas Harriot*, vol. 2, *Mathematics, Exploration, and Natural Philosophy in Early Modern England*, ed. Robert Fox (Farnham, Surrey: Ashgate, 2012), 62, and also Carl Boyer, *The Rainbow: From Myth to Mathematics* (Princeton, NJ: Princeton University Press, 1987), 203, 211.

[^ch02n9]: *Wallis*: excerpt from his biography in John Stillwell, *Mathematics and Its History* (New York: Springer-Verlag, 1989), 110–12.

[^ch02n10]: *Wallis’s political fortunes*: See the Bodleian Library’s description of J. Wallis, *A Collection of Letters and Other Papers*, MS e Mus. 203, at https://archives.bodleian.ox.ac.uk/repositories/2/resources/5805; and J. J. O’Connor and E. F. Robertson, https://mathshistory.st-andrews.ac.uk/Biographies/Wallis/.

[^ch02n11]: *Einstein’s assessment of Newton* is from his *Ideas and Opinions* (1954; New York: Three Rivers Press, 1982), 254–55.

[^ch02n12]: *Hooke’s work on planetary motion*: e.g., Michael Nauenberg, “Robert Hooke’s Seminal Contributions to Orbital Dynamics,” *Physics in Perspective* 7 (2005): 1–31. Nauenberg has made a detailed study of Hooke’s work and how Newton made use of it. It is important to give Hooke the credit he deserves, although I tend to think Nauenberg overplays Hooke’s mathematical ability, given that his argument is based on a single construction, made in 1685 after he had most likely seen Newton’s preliminary paper *De Motu*. Either way, Hooke constructed the orbit resulting from a force that varies directly with distance, and while he did it in a novel way, it is *one* calculation compared with the *hundreds* in *Principia*, for all kinds of forces and motions.

<!--p352-->
[^ch02n13]: *Newton “dry calculators”*: letter to Halley quoted in Nauenberg, “Robert Hooke,” 7. Nauenberg calls this a “diatribe,” which suggests to me, in light of the breadth of *Principia* compared with Hooke’s contribution (cf. previous note), that he is making his case for Hooke a little too vehemently. *Modern mathematics, computation versus creativity*: Patrick Bangert’s whimsical report—published in the Australian Mathematical Society’s *Gazette* 32, no. 3 ( July 2005)—suggests that many mathematicians think their subject has more to do with patterns, language, art, or logic than applications. Similarly, in July 2021, Ole Warnaar reported in the *Gazette* (vol. 48, no. 3) on feedback from the society’s members regarding proposed revisions to the Australian mathematics curriculum: criticisms included its excessively utilitarian approach. It’s certainly exciting, and socially vital, to apply mathematics usefully, and Warnaar applauds teaching such skills; but he also laments that “not enough effort has been made to try to convey the intrinsic beauty of mathematics and the enjoyment one can derive from learning and understanding new mathematical concepts.”

[^ch02n14]: *During evaporation*, heat raises the kinetic energy of the water molecules so they can escape the electrical bonds that bound the molecules together as a liquid. The violet cloth reflects cooler violet light to our eyes, absorbing the other warmer colours. So it dries fastest because it absorbs heat more quickly than the other colours on the bedsheet. Du Châtelet’s result, in an expanded version of her 1738 *Essay on Fire* (*Dissertation sur la nature et la propagation du feu*), was published in 1744 (Paris: Chez Prault Fils).

[^ch02n15]: *Newton’s geometrical version of calculus* in *Principia*: For example, try translating into modern symbols Newton’s proof of proposition 39 in book 1. He wants to find the velocity of a falling body under a centripetal force, and he defines force as proportional to the increment of velocity (*I*) divided by the increment of time, a geometric/differential version of *dv*/*dt*; but he also finds the derivative of *v*^**2**^ in an almost modern way, writing in effect [(*v* + *I*)^**2**^ − *v*^**2**^]/Δ*y* to get 2*vdv*/*dy*. (He uses *v*^**2**^ because he’s effectively proving a theorem about kinetic energy as the work done by the force.)

[^ch02n16]: For more on du Châtelet’s Newtonian work, see my *Seduced by Logic: Émilie du Châtelet, Mary Somerville and the Newtonian Revolution* (New York: Oxford University Press, 2012).

## CHAPTER 3

[^ch03n1]: *SI unit*: the Système international d’unités—the International System of Units—is abbreviated internationally as SI.

[^ch03n2]: On *Questiones Mechanicae* and its influence: David Marshall Miller, “The Parallelogram Rule from Pseudo-Aristotle to Newton,” *Archive for History of Exact Sciences* 71 (2017): 157–91, esp. 161–66. By modern standards, the *Questiones* contains only a proto-parallelogram rule, but even then, few grasped its importance.

[^ch03n3]: *Tartaglia*: his 45° calculation assumes you’re firing from the ground rather than from a height. *“Vituperative” work*: quoted in Michael Brooks, *The Art of More* (Melbourne: Scribe, 2021), 94. Here and in the next paragraph, I’m indebted to Brooks, and also to J. J. O’Connor and E. F. Robertson’s University of St Andrews MacTutor article on Tartaglia, https://mathshistory.st-andrews.ac.uk/Biographies/Tartaglia/#:~:text=Quick%20Info&text=Tartaglia%20as%20an%20Italian%20mathematician,published%20in%20Cardan%27s%20Ars%20Magna.

[^ch03n4]: Miller, “Parallelogram Rule,” 164.

<!--p353-->
[^ch03n5]: Joseph Jarrett—in “Algebra and the Art of War: Marlowe’s Military Mathematics in Marlowe’s ‘Tamburlaine I and II,’” *Cahiers Élizabéthain* 95, no. 1 (2018): 19–39—suggests that Marlowe was able to represent huge battle scenes on a small stage by applying a kind of compact representation similar to the algebraic symbolism pioneered by Harriot. Jarrett also alerted me to Altdorfer’s battle paintings.

[^ch03n6]: Galileo and Harriot got falling motion and horizontal projection right, but they treated the oblique motion of a projectile as a single decelerated motion rather than in terms of independent components: Matthias Schemmel, “Thomas Harriot as an English Galileo: The Force of Shared Knowledge in Early Modern Mechanics,” in *Thomas Harriot*, vol. 2, *Mathematics, Exploration and Natural Philosophy in Early Modern England*, ed. Robert Fox (Farnham, Surrey: Ashgate, 2012), 89–111, esp. 95, 97.

[^ch03n7]: *Galileo, Stevin, and Descartes and the parallelogram rule*: Miller, “Parallelogram Rule,” 166, 167, 170, 183, 186.

[^ch03n8]: *Harriot’s calculations (fig. 3.3)*: In each diagram the solid circles *a* and *A* on the left show the starting points of the two balls. They collide in the middle and rebound to the positions shown with dotted circles. The calculations below the diagram take account of the velocities and masses of the balls: Harriot is looking at what happens in a given time interval *x*, so the velocities are expressed in terms of the directions and lengths of the lines between the balls, analogously to what we would do with vectors today.

    Harriot explains his use of the parallelogram rule carefully. For instance, he says that if there had been no collision, then in the second time interval *x* the ball *a* would have continued moving with the same speed in the same line *ab*—so he has intuited the first law of motion. On collision, though, this motion is “translated” to the parallel line *fc*—not physically, he stresses, but for the purposes of “compos[ing] the apparent motion.” Similarly for the second ball, the motion *AB* is translated to *FC*.

    The points *f* and *F* are found from the composition of the motion of each ball before and after the collision. For example, for the first ball, *bf* equals the sum of (what we would call) two vectors: (minus) the vertical component of the ball’s initial motion, *bd*—that is, the motion as if it had simply rebounded from a stationary ball of equal mass—plus the vertical component of the extra motion imparted by the larger ball’s momentum (as we would put it), *df*(=*gb*).

    It can be done more easily using conservation of momentum and kinetic energy, but these concepts weren’t available to Harriot. The symmetry of his diagram, however, shows that he is assuming the conservation of “impetus,” and the calculations below the diagram—where his $\bar{b},\bar{B}$ represent the velocities of the two balls and *b, B* their masses—are essentially the same as in our conservation of momentum calculations. Note that

<!--p354-->
![](images/p382.jpg)

    is his notation for $\left(\bar{b}+\bar{B}\right)\left(b+B\right)/B$. (He’s made a slight error in this term.)

    *Harriot’s minor error* (plus analysis of his paper): Johannes Lohne, “Essays on Thomas Harriot,” *Archive for History of Exact Sciences* 20, nos. 3/4 (1979): 189–312, and Jon V. Pepper, “Harriot’s Manuscript on the Theory of Impacts,” *Annals of Science* 33, no. 2 (1976): 131–51, DOI: 10.1080/00033797600200191.

[^ch03n9]: *“As if ”* is Harriot’s wording, just as in modern accounts such as Miller, “Parallelogram Rule,” 158. Harriot’s paper was first published in the 1970s: see Lohne, “Essays on Thomas Harriot,” for an English translation from the original Latin.

[^ch03n10]: *Wallis and Harriot*: Jacqueline Stedall, “Rob’d of Glories: The Posthumous Misfortunes of Thomas Harriot and His Algebra,” *Archive for History of Exact Sciences* 54, no. 6 ( June 2000): 483. *Wallis and Fermat*: Miller, “Parallelogram Rule,” 171–72, 186–87.

[^ch03n11]: Wallis was trying to find a way to think about complex solutions to quadratic equations of the form *x*^**2**^ + 2*bx* + *c*^**2**^ = 0—and if you remember the quadratic formula that you can deduce by completing the square, you’ll know that $x=-b\pm\sqrt{\left(b^{2}-c^{2}\right)}$. When *b* ≥ *c*, Wallis found a way to represent the two solutions as points on the real number line—so he tried something similar for the complex solutions you get when *b* < *c*. He avoided having to deal explicitly with *i* by considering $x=-b\pm\sqrt{\left(c^{2}-b^{2}\right)}$, and he’d used cumbersome constructions with triangles to represent his solutions rather than representing them as points on a complex plane as we would do today. John Stillwell shows Wallis’s attempt and its flaws in fig. 13.3, *Mathematics and Its History* (New York: Springer-Verlag, 1989).

[^ch03n12]: The modern version of Euler’s definition of *e* is $\lim_{x\to\infty}\left(1+\frac{1}{n}\right)^{n}$. The idea of it first arose in a study of compound interest by Jakob (or Jacques) Bernoulli ( Johann/Jean’s older brother), and even earlier, although implicitly, in John Napier’s logarithms and Thomas Harriot’s unpublished calculations for continuously compounding interest and meridional parts. But it was Euler who recognised the power of this number and brought it to proper attention. He also wrote it as a Taylor series, which is the way decimal approximations of *e* are worked out, such as the one on your calculator (mine gives 2.718281828).

<!--p355-->
[^ch03n13]: *On Euler and his identity*: Ed Sandifer, “How Euler Did It,” *MAA Online*, August 2007. See also Carl Boyer, *History of Mathematics*, rev. Uta Merzbach (New York: John Wiley and Sons, 1991), 443–44 (and 441–42 on Euler and uni maths). *De Moivre and Newton*: Orlando Merlino, “A Short History of Complex Numbers,” University of Rhode Island, January 2006.

[^ch03n14]: *Euler and Fermat’s last theorem*: Later mathematicians found that Fermat hadn’t proven one of the steps in his proof, but the step itself was correct; this, and Euler’s use of complex numbers in the proof, is explained well in Harold M. Edwards, “Fermat’s Last Theorem,” *Scientific American* 239, no. 4 (October 1978): 104–23.

[^ch03n15]: *Euler/d’Alembert*: Stillwell, *Mathematics and Its History*, 202. *Sophie Germain* didn’t publish her work on Fermat’s theorem, but Legendre credited her with a result he used in his proof when *n* = 5.

[^ch03n16]: *Hamilton’s apples and oranges*: Karen Hunger Parshall, “The Development of Abstract Algebra,” in *The Princeton Companion to Mathematics*, ed. Timothy Gowers et al. (Princeton, NJ: Princeton University Press, 2010), 95–106, esp. 105.

[^ch03n17]: Gauss quoted by Christian Gérini, “Argand’s Geometric Representation of Imaginary Numbers,” University of Toulon, January 2009, English trans. Helen Tomlinson, April 2017, online at http://www.bibnum.education.fr/sites/default/files/21-argand-analysis.pdf. See this also for Argand’s “directed lines.” *De Morgan quoted* in Raymond Flood and Robin Wilson, *The Great Mathematicians* (London: Arcturus, 2011), 143. *For more context on De Morgan*: Morris Kline, *Mathematics: The Loss of Certainty* (New York: Oxford University Press 1982), 155–56.

[^ch03n18]: Babbage quoted in Dirk Struik, *A Concise History of Mathematics* (New York: Dover, 1967), 168.

[^ch03n19]: Hamilton quoted in Janet Folina, “Newton and Hamilton: In Defense of Truth in Algebra,” *Southern Journal of Philosophy* 50, no. 3 (2012): 515.

[^ch03n20]: *Hamilton’s process*, from negative numbers/science of time to complex couples to quaternions, is explained in detail by Teun Koetsier, “Explanation in the Historiography of Mathematics: The Case of Hamilton’s Quaternions,” *Studies in History and Philosophy of Science Part A* 26, no. 4 (1995): 593–616. *Hamilton’s “steps” as vectors*: see his *Lectures on Quaternions* (Dublin: Hodges and Smith; London: Whittaker; and Cambridge: Macmillan, 1853), 3ff.

    *Hamilton’s importance re: complex numbers*: Parshall, “Development of Abstract Algebra,” 105; Boyer, *History of Mathematics*, 583. *Hamilton citing Newton* on algebra of time: Folina, “Newton and Hamilton,” 513.

[^ch03n21]: *De Morgan on Hamilton’s couples*: quoted in Diana Willment, “Complex Numbers from 1600 to 1840” (master’s thesis, Middlesex University, 1985), 102. *Hamilton, symbolism, De Morgan*: Koetsier, “Explanation,” 610.

<!--p356-->
[^ch03n22]: *Literary friends*, including Wordsworth, admiring Hamilton: Michael J. Crowe, *A History of Vector Analysis* (Notre Dame, IN: University of Notre Dame Press, 1967), 22; and Daniel Brown, *The Poetry of Victorian Scientists: Style, Science and Nonsense* (Cambridge: Cambridge University Press, 2013), 1. *Maria Edgeworth on Hamilton*: “Miss Edgeworth Advises,” Royal Irish Academy (RIA) (blog), June 24, 2018, https://www.ria.ie/news/library-library-blog/miss-edgeworth-advises.

[^ch03n23]: *Maria Edgeworth, Peacock, and Somerville*: see my *Seduced by Logic: Émilie du Châtelet, Mary Somerville and the Newtonian Revolution* (New York: Oxford University Press, 2012), 195, 197–98.

[^ch03n24]: *Maria Edgeworth and Royal Irish Academy*: RIA (blog), “Miss Edgeworth Advises,” and Clare O’Halloran, “‘Better without the Ladies’: The Royal Irish Academy and the Admission of Women Members,” *18^th^–19^th^ Century Social Perspectives (History Ireland)* 19, no. 6 (November/December 2011): 42–46.

[^ch03n25]: *Hamilton on vectors as directed lines*: e.g., his *Lectures on Quaternions*, 35.

## CHAPTER 4

[^ch04n1]: *Papa, can you multiply triplets?* Hamilton’s letter to Archibald, 1865, in Robert P. Graves, *Life of Sir William Rowan Hamilton*, 3 vols. (Dublin: Hodges, Figgis, 1882, 1885, 1889), 2:434–35, widely quoted, e.g., in Michael J. Crowe, *A History of Vector Analysis* (Notre Dame, IN: University of Notre Dame Press, 1967), 29. *Explaining to “my boys”*: letter to De Morgan, 1852, Graves, *Life of Hamilton* (1889), 3: #59, 307–8.

[^ch04n2]: *Laws of algebra/arithmetic*: For example, (3 + 2) + 5 = 5 + 5 = 10; but in this case, it doesn’t matter where the brackets go, because 3 + (2 + 5) = 3 + 7 which also equals 10. This is called the associative law for addition, and there’s a similar one for multiplication. Similarly, 2 × 3 = 3 × 2, and 2 + 3 = 3 + 2; this is the famous commutative law for multiplication and addition. Peacock also introduced the distributive law, *a*(*b* + *c*) = *ab* + *bc*.

[^ch04n3]: *Law of moduli*: With an ordinary complex number *z* = *x* + *iy*, Hamilton had shown that you can define the “modulus” (the magnitude or “absolute value”) of this number by taking the square root of

::: {.displayeq}

(*x* + *iy*)(*x* − *iy*) = *x*^**2**^ + *y*^**2**^,

:::

    where the second factor on the left-hand side is the “conjugate” of the first. (This may have been known as early as Euler.) It also turns out that *the modulus of the product of two complex numbers equals the product of the two moduli*—what Hamilton referred to as “the law of moduli,” written symbolically in today’s textbooks as |*zw*| = |*z*||*w*|.

    For example, let *z* = *x* + *iy, w* = *a* + *ib*. Then

    $\left|zw\right|=|(x+iy)(a+ib)|=|(xa-yb)+i(xb+ya)|=\sqrt{(xa-yb)^{2}+(xb+ya)^{2}}$

    and

<!--p357-->
::: {.displayeq}

$$\left|z\right|\left|w\right|=\sqrt{\left(x^{2}+y^{2}\right)\left(a^{2}+b^{2}\right)}=\sqrt{\left(xa-yb\right)^{2}+\left(xb+ya\right)^{2}}.$$

:::

    So |*zw*| = |*z*||*w*|, and the law of moduli holds in two dimensions.

    If you try this with *x* + *iy* + *jz* and *a* + *ib* + *jc*, however, for the law of moduli to hold you have to make simplifying assumptions about the relationships between *x, y, a, b*—which Hamilton tried, but which destroys the generality of the law of moduli—or about the relationships between *i, j, ij*, and *ji*. See the narrative for what Hamilton did next. And see Teun Koetsier, “Explanation in the Historiography of Mathematics: The Case of Hamilton’s Quaternions,” *Studies in the History and Philosophy of Science Part A* 26, no. 4 (1995): 593–616, for Hamilton’s process, including letters to Graves.

[^ch04n4]: Hamilton explained this process in the preface to his *Lectures on Quaternions*.

[^ch04n5]: Augustus De Morgan, *Essays on the Life and Work of Newton*, edited, with notes and appendices, by Philip Jourdain (Chicago: Open Court, 1914). *Biographical notes on De Morgan*: Leslie Stephen, *Dictionary of National Biography* 14 (1885–1900), s.v. De Morgan; incidentally, Stephen was the father of the famous novelist Virginia Woolf. Also see, e.g., Carl Boyer, *History of Mathematics*, rev. Uta Merzbach (New York: John Wiley and Sons, 1991), 581.

[^ch04n6]: *“Deeply reverential”*: Alexander MacFarlane, *Lectures on Ten British Mathematicians* (London: Chapman and Hall, 1916), chap. 3 (from a lecture delivered in 1901).

[^ch04n7]: Recent scholarship has traced the evolution of the gossip about Hamilton, and put it in the context of women’s roles and social constraints and painting a more positive picture of his and Helen’s life: Anne van Weerden and Stephen Wepster, “A Most Gossiped about Genius: Sir William Rowan Hamilton,” *BSHM Bulletin* 33, no. 1 (2018): 2–20. They also give a more balanced account than earlier records suggested, e.g., putting an episode where Hamilton was supposed to be violently drunk into the context of the temperance movement.

<!--p358-->
[^ch04n8]: *De Morgan and Lovelace*: two papers by Christopher Hollings, Ursula Martin, and Adrian Rice: “The Early Mathematical Education of Ada Lovelace,” *BHSM Bulletin* 32, no. 3 (2017): 221–34, and “Lovelace-De Morgan Correspondence: A Critical Re-appraisal,” *Historia Mathematica* 44 (2017): 202–31. Note that Babbage’s “difference engine” was ahead of its time and never went into production.

[^ch04n9]: De Morgan quoted in Janet Folina, “Newton and Hamilton: In Defense of Truth in Algebra,” *Southern Journal of Philosophy* 50, no. 3 (2012): 511. Note that Hamilton and De Morgan had different approaches to algebraic foundations (511–12).

[^ch04n10]: *Hamilton to De Morgan, 1841*, quoted, e.g., Michael J. Crowe, *A History of Vector Analysis* (Notre Dame, IN: University of Notre Dame Press, 1967), 27.

[^ch04n11]: *Invoking k = ij*: For triples *a* + *ib* + *jc* and *x* + *iy* + *jz*, the law of moduli says that

::: {.displayeq}

|(*a* + *ib* + *jc*)(*x* + *iy* + *jz*)| = |*a* + *ib* + *jc*||*x* + *iy* + *jz*|.

:::

    The right-hand side (RHS) is just

::: {.displayeq}

(*a*^**2**^ + *b*^**2**^ + *c*^**2**^)(*x*^**2**^ + *y*^**2**^ + *z*^**2**^).

:::

    Now for the left-hand side (LHS): assume *ij* = −*ji*, and consider the LHS when you’ve expanded the brackets:

::: {.displayeq}

|*ax* − *by* − *cz* + *i*(*ay* + *bx*) + *j*(*az* + *cx*) + *ij*(*bz* − *cy*)| = (*ax* − *by* − *cz*)^**2**^ + (*ay* + *bx*)^**2**^ + (*az* + *cx*)^**2**^ + (*bz* − *cy*)^**2**^.

:::

    But you only get this last term—which you need to balance with the RHS—by incorporating the conjugate of *ij*(*bz* − *cy*) into the modulus definition, *as if ij were a complex number like i and j*. This is what led Hamilton to suppose that to solve his problems of triplet multiplication, he had to invoke a *third* imaginary vector *k* = *ij*.

    *Hamilton’s “electric circuit”*: I’ve slightly modified the tense on “closed”; cf. Hamilton’s 1865 letter to Archibald, quoted in Crowe, *History of Vectors*, 29. *Hamilton to Graves*: quoted in B. L. van der Waerden, “Hamilton’s Discovery of Quaternions,” *Mathematics Magazine* 49, no. 5 (November 1976): 227–34, esp. 230.

<!--p359-->
[^ch04n12]: De Morgan quoted in Folina, “Newton and Hamilton,” 505. *Wordsworth* on Hamilton’s mediocre poetry: Daniel Brown, *The Poetry of Victorian Scientists: Style, Science and Nonsense* (Cambridge: Cambridge University Press, 2013), 1–2. *Schrödinger*: Crowe, *History of Vector Analysis*, 17. Schrödinger was referring to what is now called Hamiltonian dynamics, an alternative, coordinate-free form of the laws of motion, equivalent to Newton’s approach but more flexible.

[^ch04n13]: *Playing with Hamilton’s graffiti* only works if you assume that you can cancel terms only at the beginning or end of the string, and if products of pairs are anticommutative. So, to find *j* from *j*^**2**^ = *ijk*, rewrite as *j*^**2**^ = −*jik*, and then, canceling *j* from both sides, you have *j* = −*ik* = *ki*.

[^ch04n14]: *Scalar products* just multiply the components, so that ***p*** ∙ ***q*** = *p*~1~*q*~1~ + *p*~2~*q*~2~ + *p*~3~*q*~3~ is a number, or scalar, not a vector. (In Hamilton’s full quaternion product, there’s a minus sign in front of ***p*** ∙ ***q***, which will prove controversial, as we’ll see in chap. 7.)

    *Vector products* give vectors; the component form of ***p*** × ***q*** is easiest to remember and calculate from the determinant $\left|\begin{matrix} \boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\ p_{1} & p_{2} & p_{3} \\ q_{1} & q_{2} & q_{3} \end{matrix}\right|$

[^ch04n15]: *Cayley and quaternions*: Crowe, *History of Vector Analysis*, 35. *Cayley’s life*: Tony Crilly, “Arthur Cayley: The Road Not Taken,” *Mathematical Intelligencer* 20, no. 4 (1998): 49–53; Crilly also wrote the *Britannica* entry on Cayley.

[^ch04n16]: A computer algorithm for Gaussian elimination is given, e.g., in Erwin Kreyszig, *Advanced Engineering Mathematics* (New York: Wiley, 1993), 976.

[^ch04n17]: *Sylvester “invariants”*: Crilly, “Arthur Cayley: The Road Not Taken,” 51.

[^ch04n18]: *Boole and Cayley*: Tony Crilly, “The Rise of Cayley’s Invariant Theory,” *Historia Mathematica* 13 (1986): 241–54.

[^ch04n19]: Eunice Foote, “Circumstances Affecting the Heat of the Sun’s Rays,” *American Journal of Science and Arts* (1856): 382–83. John Tyndall, apparently independently, put the physics into Foote’s empirical discovery just a few years later: see Roland Jackson, “John Tyndall: The Forgotten Cofounder of Climate Science,” *The Conversation*, July 31, 2020. Jean-Baptiste Fourier was the first to look at the heating effect of the atmosphere, in 1820, but he did it in the context of calculating Earth’s temperature.

[^ch04n20]: *Search engines*: The form of the scalar product needed to deduce the angle between two vectors a and b is ***a*** ∙ ***b*** = |***a***||***b***|cosθ. For my description I’ve drawn on Amy Langville’s excellent introduction, “The Linear Algebra behind Search Engines: Focus on the Vector Space Model,” *Convergence*, Mathematical Association of America (December 2006); https://www.maa.org/press/periodicals/loci/joma/the-linear-algebra-behind-search-engines-focus-on-the-vector-space-model.

<!--p360-->
[^ch04n21]: *Google PageRank algorithm*: I’ve drawn on Cornell University’s informative lecture, http://pi.math.cornell.edu/~mec/Winter2009/RalucaRemus/Lecture3/lecture3.html.

[^ch04n22]: *Critiques of AI, social media, and search algorithms*: See, e.g., Cathy O’Neill, *Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy* (New York: Crown Publishing, 2017); Safiyah Umoja Noble, *Algorithms of Oppression* (New York: NYU Press, 2018); Shoshana Zuboff, *The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power* (London: Profile Books, 2019); and many others.

[^ch04n23]: Sarah Flannery’s algorithm failed the safety protocol (cf. her book *In Code* [London: Profile Books, 2001]), but researchers still believe noncommutative multiplication will prove a valuable cryptographic tool.

[^ch04n24]: *Quaternion rotations*: Hamilton briefly outlined the following approach in his *Lectures on Quaternions*, 269 (art. 282):

    To take a simple example, to rotate a vector ***p*** about the *i*-axis, you could choose the unit quaternion *U* = cos θ + *i* sin θ, by analogy with the complex numbers in my fig. 4.3. (This is the quaternion *U* = (cosθ, sin θ, 0, 0), because the *j* and *k* (or *y* and *z*) components of the axis of rotation in this case are zero.) Then, using Euler’s theorem, you have *U* = *e^i^***θ**. This form makes multiplications easier—the index laws turn multiplications into additions—and shows clearly how they are related to rotations, as we saw also in figure 3.8.

    Now form a new vector,

::: {.displayeq}

***a*** = *U**p**U***^−1^** = *e*^*i***θ**^***p*** *e*^**−***i***θ**^ = *e^i^*^**θ**^(*ix* + *jy* + *kz*)*e***−**^*i***θ**^.

:::

    It must have taken Hamilton a bit of experimenting to come up with this combination, for you don’t need to also multiply by *U*^**−1**^ when you’re in the Argand plane (cf. figs. 4.3, 3.8). (By the way, for unit quaternions, the inverse is the complex conjugate, so I could have written ***a*** = *U**p**U*^*****^ rather than ***a*** = *U**p**U*^**−1**^.) Geometrically, this *U*^**−1**^ factor is needed to counteract an extraneous rotation that happens because it’s taking place in a 4-D hyperspace, but that is beyond my scope here. Algebraically we’re talking about the quaternion analogue of a matrix *similarity transformation*. But you don’t need these technicalities to carry out the simple algebra that results from this “machinery”:

    If you replace *k* by Hamilton’s definition *ij*, you get

::: {.displayeq}

***a*** = *e^i^*^**θ**^(*ix* + *jy* + *kz*)*e***−**^*i*^^**θ**^ = *e^i^*^**θ**^(*ix* + (*y* + *iz*)*j*)*e***−**^*i*^^**θ**^ = *e^i^*^**θ**^(*ix*)*e***−**^*i*^^**θ**^ + *e^i^*^**θ**^(*y* + *iz*)*je***−**^*i*^^**θ**^.

:::

    Now comes the nifty part: remembering that *e***−**^*i*^^**θ**^ = cos θ − *i* sin θ, the *je***−**^*i*^^**θ**^ in the last term becomes

<!--p361-->
::: {.displayeq}

*j*(cos θ − *i* sin θ) = *j* cos θ − *ji* sin θ.

:::

    But Hamilton defined *ij* = *k* = −*ji*, so we have

::: {.displayeq}

*j* cos θ − *ji* sin θ = *j* cos θ + *ij* sin θ = (cos θ)*j* + (*i* sin θ)*j* = (cos θ + *i* sin θ)*j* = *e^i^*^**θ**^*j*.

:::

    (I wrote *j* cos θ = (cos θ)*j* because cosθ is just a real number or scalar; it is only when both numbers are complex that multiplications are not necessarily commutative—as when *ij* = *k* = −*ji*. Similarly for *j* sin θ = (sin θ)*j*.)

    Finally, using index laws and Hamilton’s rules for products of the *i, j, k*, we have the rotated version of the vector ***p***:

::: {.displayeq}

***a*** = *xi* + *e^i^*^**2θ**^( *y* + *zi*)*j* = *xi* + *e^i^*^**2θ**^(*yj* + *zk*).

:::

    This looks right, because ***p*** has been rotated about the *i*-axis, so its *i*-component doesn’t change, for it moves only in the *j*-*k* plane. And the *e^i^*^**2θ**^ factor shows that ***p***’s *j* and *k* components have, indeed, been rotated in the *j*-*k* plane, by an angle of 2θ. (So if you want to rotate by θ, choose the unit quaternion to be *U* = *e^i^*^**θ/2**^.)

    *To rotate about an arbitrary axis* in the direction of a unit vector ***u*** = *ai* + *bj* + *ck*, rather than just *i* as in the above calculation, put *U* = cos θ + ***u*** sin θ = *e***^*u*^^θ^**, by analogy with Euler’s formula. (You can prove Euler’s formula by comparing the series for the expressions on each side of the equation.) My account in the above is an expanded version of Hamilton’s outline, and of the example in the lecture notes, “Introducing the Quaternions,” by John Huerta, Fullerton College.

    ***Alternatively***, you can do the above calculations by expanding ***a*** = *U**p**U*^**−1**^ using the *scalar and vector products* that come from quaternion multiplication, as I showed in the narrative:

::: {.displayeq}

*PQ* = *wa* − ***p*** ∙ ***q*** + *w**q*** + *a**p*** + ***p*** × ***q***.

:::

[^ch04n25]: For an example of matrices giving gimbal lock, see Justin Wyss-Gallifent’s MATH431 lecture “Gimbal Lock,” November 3, 2021: http://www.math.umd.edu/~immortal/MATH431/book/ch_gimballock.pdf.

<!--p362-->
[^ch04n26]: *Spectral lines*: If an atom absorbs energy, its electrons jump to a higher energy state; when they return to their original, more stable state, the atom emits a photon, which shows up as a coloured spectral line. The colour corresponds to the emitted light’s wavelength, which in turn is related to the size of the energy jump and the makeup of the atom. Which is why the pioneering female astronomer Annie Jump Cannon had been working at Harvard College Observatory since 1896, painstakingly classifying the spectra of stars to determine their chemical composition. She continued doing this till 1941, the year she died.

[^ch04n27]: Actually, the connection with Stern-Gerlach was made a little later. Anyway, Uhlenbeck and Goudsmit’s values were ±*h*/4π; the sign depends on whether the spin axis is aligned with or against the magnetic field, and the magnitude is *half* the “normalised” Planck constant *h*/2π (which is represented as *ħ*, pronounced “h-bar”). That’s why the electron is now said to have a spin of ½.

[^ch04n28]: *Ehrenfest, Lorentz*: Goudsmit gave an account of the discovery of electron spin in a delightful paper he read for the golden jubilee of the Dutch Physical Society in April 1971; https://www.lorentz.leidenuniv.nl/history/spin/goudsmit.html.

[^ch04n29]: *Pauli matrices and quaternions*: What the relationship between Pauli matrices and quaternions also shows is that you can have a “vector space” of vectors that are actually matrices. It is the rules of vectors that matter: if something behaves like a vector, it can be treated as one. *Pauli on quaternions*: W. Pauli, *General Principles of Quantum Mechanics*, Springer-Verlag, Berlin/Heidelberg, 115; he noted that *i* times the matrix obeys the rules of unit quaternion multiplication. *Dirac*: P. A. M. Dirac, “The Quantum Theory of the Electron,” *Proceedings of the Royal Society of London*, series A, 117, 778 (February 1, 1928): 610–24; and Paul A. M. Dirac, “Theory of Electrons and Positrons,” 1933 Nobel Prize speech, https://www.nobelprize.org/uploads/2018/06/dirac-lecture.pdf.

[^ch04n30]: *Quaternion and spin rotations*: Dirac’s new theory showed that all the building blocks of matter—electrons, protons, and neutrons—have spins that contain a ½; that is, they are odd-number multiples of ½, and they are called fermions. (Photons and other so-called bosons have integer spins.)

    It’s the ½ in a particle’s spin that causes the strange behavior in which you need *two* 360° rotations to bring a fermion back to its original state. This discovery came out of the maths you need to rotate a quantum particle’s spin axis—similar maths to quaternion rotations, as it happens. Which isn’t really surprising, given that each gives the same counterintuitive type of rotation. I’ve given a brief summary here:

    As I implied in fig. 4.4 and the endnote on quaternion rotations, to rotate a vector through an angle θ around the *x*-axis, the unit quaternion is $U=e^{i\frac{\theta}{2}}$. Similarly, to rotate a spin half angular momentum vector through θ about the *x*-axis, you need a unitary operator $U=e^{-i\frac{\theta}{2}\sigma x}$, where units are chosen so that 2π/*h* = 1, and σ^*x*^ is a Pauli spin matrix. *Note the* θ*/2 in both cases*—it’s why you need two full 2π rotations to get back to the original unrotated (θ = 0 + 2*n*π) state.

    By contrast, to rotate the orbital rather than the spin angular momentum through an angle θ around the *x*-axis, the unitary operator is *U* = *e***–**^*i*^^**θ**^ ^*Jx*^. Rotate through 2π and you *are* back where you started. Note, too, that in both quaternion and quantum rotations, you also need to postmultiply by the inverse or conjugate; this is called a “similarity transformation.”

    Another way of describing the connection between quaternions and spin is that both quaternion and spin half rotation matrices are elements of the group *SU*(2). *Group theory* deals with underlying structures, so by studying group properties of various mathematical or physical structures, you can sometimes spot similarities between two apparently very different things.

<!--p363-->
[^ch04n31]: Klein and Opat used neutrons rather than electrons, because the charge on electrons would interfere too strongly with the external magnetic field in the experiment. They used a ferromagnetic crystal to diffract a beam of neutrons (traveling as a matter wave) into two parts, one of which interacted with the external magnetic field. (In quantum mechanics the “matter wave” or “wave function” describes the probability of a particle being detected at a certain time and place.) What they found was that when one beam—one part of the wave—has been rotated by an odd-integer multiple of 360° or 2π radians— which, of course, includes 2π itself—it interfered *destructively* with the other, nonrotated half, producing a distinctive interference pattern. For even multiples of 2π, the destructive interference disappeared. So in the odd-integer 2π case, you need to rotate the spin again, so that all up it goes through an even multiple such as 4π to get the interference pattern back to normal. A. G. Klein and G. I. Opat, “Observation of 2π Rotations by Fresnel Diffraction of Neutrons,” *Physical Review Letters* 37, no. 5 (August 2, 1976): 238–40.

[^ch04n32]: The other teams were headed by Helmut Rauch and Sam Werner, but instead of being rivals the three teams subsequently worked together, as Klein describes in “Neutron Interferometry: A Tale of Three Continents,” available at http://www.europhysicsnews.org or http://dx.doi.org/10.1051/epn/2009802.

[^ch04n33]: Hamilton’s *Ode* is analysed by Brown, *Poetry of Victorian Scientists*, 7–9.

<!--p364-->
[^ch04n34]: *Octonions today*: For a technical overview of current research, see Peter Rowlands and Sydney Rowlands, “Are Octonions Necessary to the Standard Model?,” *Journal of Physics: Conference Series* 1251, 012044 (2019), DOI 10.1088/1742-6596/1251/1/012044. One of these researchers is a young Canadian woman, Cohl Furey; another is University of California mathematician John Baez. In 2021, Baez gave an update on the situation at https://math.ucr.edu/home/baez/standard/.

## CHAPTER 5

[^ch05n1]: Robert P. Graves, *The Life of Sir William Rowan Hamilton*, 3 vols. (Dublin: Hodges, Figgis, 1882, 1885, 1889), 2:585–86.

[^ch05n2]: Graves, *Life of Hamilton*, 2:586.

[^ch05n3]: For Grassmann’s early life and work here and in much of the following, I’m indebted primarily to Michael J. Crowe, *History of Vector Analysis* (Notre Dame, IN: University of Notre Dame Press, 1967), chap. 3 (for more detail see Hans-Joachim Petsche, *Hermann Grassmann* [Basel: Birkhäuser, 2009]); and for an overview of the discovery of vectors, including Hamilton and Grassmann, Jean-Luc Dorier, “A General Outline of the Genesis of Vector Space Theory,” *Historia Mathematica* 22 (1995): 227–61.

[^ch05n4]: *Grassmann “astounded”*: 1847 letter to Saint-Venant, quoted in Crowe, *History of Vector Analysis*, 56.

[^ch05n5]: Crowe, *History of Vector Analysis*, 70–72.

[^ch05n6]: The fanatical new authorities had hesitated over Italian-born Lagrange— foreigners were usually stripped of their posts and possessions—but in the end a special decree enabled him to stay on, and as head of the committee, no less. This was largely thanks to the efforts on behalf of foreign scientists by pioneering chemist Antoine Lavoisier—he and his wife Marie have been dubbed the “father and mother” of modern chemistry. Lavoisier famously and tragically ended up at the guillotine for his business interests in a taxcollecting company, and Lagrange famously declared that while it took the mob but a moment to cut off his head, it might take a century to see its like again. Eighteen months later the government declared Lavoisier innocent of any wrongdoing by the tax company.

[^ch05n7]: Some sources say two children survived: either way, how tragic—especially for his poor mother! No wonder Lagrange himself had no children.

<!--p365-->
[^ch05n8]: If you multiply the vectors representing the two directed lines defining a parallelogram via the *vector product*, you get another vector. (This makes the vector product “closed.”) The product vector is perpendicular to the plane of the two original vectors. But if you multiply the two sides of the parallelogram via *Grassmann’s outer product*, you get not another “line”— Grassmann didn’t use the term “vector”—but a directed *area*. So the outer product is conceptually different from the vector product. (It is related to a tensor product, though, as we’ll see.) However, they are equivalent in that the vector you get from the vector product of the two sides is in the same direction as Grassmann’s directed area and has the same magnitude.

[^ch05n9]: *Hamilton’s letter* to Mortimer O’Sullivan was published in Graves, *Life of Hamilton*, 2:683.

[^ch05n10]: *Herschel to Hamilton*, quoted in Graves, *Life of Hamilton*, 3:121.

[^ch05n11]: Möbius, Apelt, Baltzer, quoted in Crowe, *History of Vector Analysis*, 78–80.

[^ch05n12]: Möbius, Apelt, Baltzer, quoted in Crowe, *History of Vector Analysis*, 78–80.

[^ch05n13]: Möbius, Apelt, Baltzer, quoted in Crowe, *History of Vector Analysis*, 78–80.

[^ch05n14]: *Ampère vs. Grassmann*: For a contemporary and well-judged assessment, see Maxwell’s *Treatise on Electricity and Magnetism*, 1891 (3rd edition of the 1873 original, Clarendon Press or Dover reprint), arts. 482, 509–10 (511–25 for Maxwell’s own analysis), 526 (Maxwell favours Ampère because Grassmann’s formula violated Newton’s third law), but 687 for Maxwell’s conclusion that it was impossible to decide *experimentally* between the two formulae.

    *Recent attempts to experimentally and conceptually decide*: Christine Blondel and Bertrand Wolff, trans. Andrew Butricia, “Ampère’s Force Law: An Obsolete Formula?” *Histoire de l’Électricité et du Magnetisme* (May 2009; trans. 2013, rev. 2021), http://www.ampere.cnrs.fr/histoire/parcours-historique/lois-courants/force-obsolete/eng.

    This paper gives a brief nonpartisan overview of recent research. For a detailed, ultimately pro-Ampère account: A. K. T. Assis and J. P. M. C. Chaib, *Ampère’s Electrodynamics* (Apeiron, 2015), chaps. 14, 16.4, and conclusion, 491; still, in 1996 Assis had shown (with Marcelo A. Bueno) that Grassmann’s and Ampère’s formulae were equivalent in the experimental set-up espoused by Ampère: “Equivalence between Ampère and Grassmann’s Forces,” *IEEE Transactions on Magnetics* 32, no. 2 (March 1996): 431–36.

    Note that some modern authors are using the Ampère vs. Grassmann debate to question the field theory approach (into which Grassmann’s result was integrated post-Maxwell); cf. Ampère’s action-at-a-distance. Maxwell himself said it was always a good idea to have more than one way of seeing things!

    *Grassmann’s original paper*: Hermann Grassmann, “Neue Theorie der Elektrodynamik,” *Annalen der Physik und Chemie* 1 (1845): 1–18.

<!--p366-->
[^ch05n15]: *Leibniz and Grassmann*: Joseph Kouneiher, “Broken Symmetry, Pointless Space and Leibniz’s Legacy: The Origin of Physics,” *Advanced Studies in Theoretical Physics* (September 2015), accessed from ResearchGate, https://www.researchgate.net/publication/281526332_Broken_symmetry_Pointless_Space_and_Leibniz%27s_Legacy_the_origin_of_physics.

[^ch05n16]: Graves, *Life of Hamilton*, 3:424.

[^ch05n17]: Graves, *Life of Hamilton*, 3:441–42.

[^ch05n18]: William Rowan Hamilton, *Lectures on Quaternions* (London: Whittaker, and Cambridge: Macmillan, 1853), e.g., 59, for multiplication by *j* and changing the orientation of a telescope.

[^ch05n19]: Crowe has made a convincing case for the historiography of vector analysis proceeding from Hamilton and his successors rather than Grassmann (*History of Vector Analysis*, 77, chap. 4). Much later, as we’ll see, Grassmann will influence Cartan, Clifford, and *their* followers.

## CHAPTER 6

[^ch06n1]: For an accessible account of Maxwell’s life and work, see my *Einstein’s Heroes: Imagining the World through the Language of Mathematics* (St. Lucia: University of Queensland Press, 2003; New York: Oxford University Press, 2005).

[^ch06n2]: *Tait’s excited letter*: Cargill Gilston Knott, *The Life and Scientific Work of P. G. Tait* (London: Cambridge University Press, 1911), 9. *On the Tripos*: the figure of sixteen exams over eight days was for 1854 (Maxwell’s year): D. O. Forfar, “What Became of the Senior Wranglers?” *Mathematical Spectrum* 29, no. 1 (1996); available at www.clerkmaxwellfoundation.org.

[^ch06n3]: *Maxwell at Cambridge*: Lewis Campbell and William Garnett, *The Life of James Clerk Maxwell* (London: Macmillan, 1882), 94–95. (There is a 1997 digital edition by Sonnet Software.)

[^ch06n4]: The poem—whose full title is “A Vision of a Wrangler, of a University, of Pedantry, and of Philosophy”—is published in Campbell and Garnett, *Life of Maxwell*, 307.

[^ch06n5]: *Maxwell as examiner*: Campbell and Garnett, *Life of Maxwell*, 175.

[^ch06n6]: *Tait on Maxwell*: Obituary, *Proceedings of the Royal Society of Edinburgh* 10 (1878–80): 331–39. *His father’s letter to Maxwell*: Campbell and Garnett, *Life of Maxwell*, 109. *His old teacher*: David O. Forfar and Chris Pritchard, “The Remarkable Story of Maxwell and Tait,” *James Clerk Maxwell Commemorative Booklet* (Edinburgh, 1999), 3.

<!--p367-->
[^ch06n7]: *On Stokes’s theorem*: Maxwell credits proof to Thomson and Tait (and also notes its first appearance in the Smith’s Prize exam) in his *A Treatise on Electricity and Magnetism* (Oxford: Clarendon Press, 1873), 1:27. Thomson is the theorem’s likely originator, for he had included it in a letter to Stokes back in 1850. Victor J. Katz (“The History of Stokes’ Theorem,” *Mathematics Magazine* [MAA] 52, no. 3 [May 1979]: 146–56) credits Hermann Hankel with the first published proof (in 1861), but it wasn’t as general as Thomson’s (1867).

[^ch06n8]: *Area of a circle as a surface integral*: imagining a tiny element *dS* of the surface bounded by the circle, the idea is to integrate *dS* over the whole surface to find the area. Here the *x* and *y* axes represent the two dimensions that define the surface, so you can imagine little line segments in each direction, *dx* and *dy*, which border a rectangular elemental area of the surface—so in the surface integral you are integrating with respect to *dS* = *dxdy*. (Because the surface is a plane, this is actually just a double integral rather than a surface integral, where *dS* is more complicated than *dxdy* because it requires the use of vectors to find the normal to the surface.) Transforming this to polar coordinates (as in fig. 2.2a), and not forgetting the Jacobian factor for changing the coordinates, you get *dS* = *dx dy* = *rdr d*θ. Integrate this around the circle of radius *R*:

::: {.displayeq}

$$\text{Area}=\int _{0}^{2\pi}\int _{0}^{R}rdrd\theta=\int _{0}^{2x}\frac{1}{2}R^{2}d\theta=\pi R^{2}$$.

:::

    If the Jacobian is not familiar, for polar coordinates you can think of a tiny sector of a circle with angle *d*θ and radius *r*: the arc length *s* of the sector is *rd*θ (since $\frac{s}{2\pi r}=\frac{d\theta}{2\pi}$, by definition of a radian), and a radial element has length *dr*, so the element of area is *rdr d*θ.

[^ch06n9]: The survival of the grounds, along with the restoration of Glenlair House and outbuildings, is thanks largely to the efforts of the estate’s current owner, Captain Duncan Ferguson. I’ve had the pleasure of meeting Duncan at Glenlair, and you can see more about his and the Glenlair Trust’s work on behalf of Maxwell and Glenlair at http://www.glenlair.org.uk.

[^ch06n10]: *Maxwell at British Association meeting*, recollected by William Swan, in Campbell and Garnett, *Life of Maxwell*, 236.

[^ch06n11]: *Stationary gravity?* The sun and planets are moving, of course, but at any given point in the orbit they are stationary with respect to each other and are at a given distance apart. Newton’s law treats the force arising just from this distance and the two masses. *Coulomb’s law*: Maxwell described more accurate experiments establishing the inverse square law in his *Treatise on Electricity and Magnetism*, 1:34, 75.

<!--p368-->
[^ch06n12]: *The (simplified) maths of Lagrange’s potential*: Work = force times distance, so if the distance moved is in the vertical direction (*y*, say), then *W* = *f* × *y*. This formula is fine if the force remains constant, but for forces that change with distance, such as gravity, you need integral calculus to “add up” the force times the incremental distance *at each point* as the force moves the object.

    Newton had given a geometrical calculus definition of this in terms of the area under the force curve, but in Leibnizian notation we’d have $W=\int _{a}^{b}fdy$, which gives *F*(*b*) − *F*(*a*), where *F* is the antiderivative of *f*. (Actually, this is true only for “conservative” forces, including gravity, which depend only on the endpoints of the integral; for other forces, such as friction, you need a *line integral*, to take account of the characteristics of the entire path between the starting point *a* and finishing point *b*.)

    What Lagrange showed, in effect, was that $f=\frac{dF}{dy}$. This is just the fundamental theorem of calculus taught in introductory calculus classes, but Lagrange extended it to three dimensions, to allow for the force and distance moved to be in any direction, not just up and down—so he found that the force has components $\frac{\partial F}{\partial x},\frac{\partial F}{\partial y},\frac{\partial F}{\partial z}$. (The “curly d” notation wasn’t standard then, but I’m using it so as not to confuse modern mathematical readers.) Following Newton, he had the idea of force as a vectorial quantity, but like everyone before Hamilton and Grassmann, he dealt only with components, not with whole vectors.

    Drawing on the relationship between work and potential energy, *F* is called the “potential” associated with the force *f*. Generally force is written with an uppercase *F*, so a common symbol for potential is *V*. (George Green was the first to use the term “potential,” in 1828.)

[^ch06n13]: *Partial derivatives*: in the $\frac{\partial F}{\partial x}$ term, *F* is differentiated only with respect to *x*, so this term tells how *F* changes in the *x*-direction while *y* and *z* remain fixed—and similarly for the other two terms.

[^ch06n14]: “*Newton of electricity*”: Maxwell, *Treatise on Electricity and Magnetism*, 2:175.

[^ch06n15]: Such forces, which depend only on the endpoints and not on the nature of the path between them, are called “conservative,” because they lead to conservation of energy. For Newtonian gravity, for example, the motion is radial, so the inverse square law can be written as $m\ddot{r}=-\frac{GmM}{r^{2}};$; writing $\ddot{r}=\dot{r}d\dot{r}/dr$, integrate to find the work done by the force in moving an object from point 1 to point 2:

::: {.displayeq}

$$m\int _{\dot{r}_{1}}^{\dot{r}_{2}}\dot{r}d\dot{r}=-GMm\int _{r_{1}}^{r_{2}}\frac{1}{r^{2}}dr\Rightarrow\frac{1}{2}m\dot{r}^{2}-\frac{GMm}{r}=\text{constant},$$

:::

    which means the sum of the kinetic and potential energies is conserved; the constant is found from the endpoints in the definite integrals.

<!--p369-->
[^ch06n16]: Maxwell, *Lecture on Faraday’s Lines of Force*, a talk he presented in 1873, in his collected works, *The Scientific Letters and Papers of James Clerk Maxwell*, ed. P. M. Harman, 2 vols. (Cambridge: Cambridge University Press, 1990, 1995), 803.

[^ch06n17]: *Thomson and Faraday on fields*: Ernan McMullin, “The Origins of the Field Concept in Physics,” *Physics in Perspective* 4 (2002): 13–39 (esp. 14). This paper gives a detailed overview of the field concept and its evolution up till Maxwell gave the first full-blown field theory.

[^ch06n18]: *The Marischal professorship*: Forfar and Pritchard (“Remarkable Story,” 3–4) noted that College records were not extant, but that it was believed Tait was a candidate for the job that Maxwell got—and later John S. Reid, of the University of Aberdeen, stated that Tait was a candidate, in “James Clerk Maxwell’s Scottish Chair,” *Philosophical Transactions of the Royal Society A* (2008), 366, 1661–84, DOI:10.1098/rsta.2007.2177. If so, as Forfar and Pritchard note, Maxwell and Tait’s correspondence shows there were no hard feelings between them—in 1856 or in 1860 (when Tait beat Maxwell to a job at Edinburgh). *Cayley applying*: Crilly, “Arthur Cayley: The Road Not Taken,” 52.

[^ch06n19]: *Maxwell explaining his choice of language*: He alludes to it at the beginning of his 1865 paper ( J. Clerk Maxwell, “A Dynamical Theory of the Electromagnetic Field,” *Philosophical Transactions of the Royal Society London* 155 [1865]: 459–512), and explains it fully in his *Treatise on Electricity and Magnetism*, 1:98–99 (art. 95), and vol. 2 (3rd ed.), 176–77 (art. 529). He says that ordinary integrals, and line and surface integrals over finite spaces, suit the action-at-a-distance approach, while partial differential equations, and (volume) integrals throughout all of space, are the natural language for fields.

[^ch06n20]: *Maxwell’s definitions of current and their relation to flux*: He included two types of current: the conventional one in conductors such as a loop of wire—where the current is the flux of the current density—and the effective current in a capacitor, which he called the “displacement current,” and which is proportional to the changing flux of the electric force between the capacitor plates.

[^ch06n21]: *Converting integrals to derivatives in Maxwell’s field equations*: The “first fundamental theorem of integral calculus” links integrals and derivatives:

    $\int _{a}^{b}f\left(x\right)dx=F\left(b\right)-F\left(a\right)$, where *F* (*x*)is the antiderivative of *f* (*x*).

    In other words, $f\left(x\right)=\frac{dF\left(x\right)}{dx}$, assuming the relevant functions are integrable/differentiable! What this means is that you can go from *f*(*x*) to *F*(*x*) via integration, or from *F*(*x*) to *f*(*x*) via differentiation. *Stokes’s theorem* is an extension of this idea, where you can go from (single) line integrals to (double) surface integrals, and vice versa. Similarly, you can go from surface integrals to volume (triple) integrals and back via what is now, post-vectors, known as the “divergence theorem.” For example, this is how Maxwell deduced the differential form of Gauss’s laws for static electricity and magnetism (in his *Treatise on Electricity and Magnetism*, 1:68, 79, 98–99):

    It was known experimentally that the amount of electric charge *e* contained in a given volume could be written as the volume integral of the charge density ρ:

<!--p370-->
::: {.displayeq}

*e* = ∫∫∫ρ *dx dy dz* … I’ll call this equation (1).

:::

    It was also known (from Coulomb’s law) that the force *R* exerted on a charge *e* by a unit test charge is *R* = *e*/*r*^**2**^, and that the electric flux through a closed surface was

::: {.displayeq}

∫∫ *R* cos ε *dS* = 4π*e*, … (2)

:::

    where ε is the angle of the direction of the force. Maxwell, adapting Faraday, called *R*cos ε*dS* the “induction” through the surface. Maxwell labeled the components of *R* as *X, Y, Z*, which he linked to the following theorem (now known as the divergence theorem, but it didn’t have a name then, and it was only known in component form as shown):

::: {.displayeq}

$$\iint R\cos\epsilon dS=\iiint\left(\frac{dX}{dx}+\frac{dY}{dy}+\frac{dZ}{dz}\right)dxdydz$$ … (3)

:::

    So then Maxwell multiplied (1) by 4π and equated the result with (2), to get

::: {.displayeq}

∫∫ *R* cos ε *dS* = 4π ∫∫∫ ρ *dx dy dz*.... (4)

:::

    Finally, equate (3) and (4), and take the closed surface from (3) as an element of the volume in (4), to get:

::: {.displayeq}

$$\frac{dX}{dx}+\frac{dY}{dy}+\frac{dZ}{dz}=4\pi\rho$$...(5)

:::

    If you are familiar with vector calculus already, you’ll recognise the lefthand side is the *divergence* of *R*, but we’ll come to this in the narrative when Tait and Maxwell (and Heaviside) put it into vector form.

    Meantime, as Maxwell then explained, if you can write the electric force in terms of a potential *V*, then (5) becomes Poisson’s extension of Laplace’s equation. The vector form of (5) is the way Coulomb’s law appears in Maxwell’s equations today. The result for static magnetism follows in a similar way.

    Maxwell’s working that I’ve shown here makes the links between flux/surface integrals and divergence clear—and it is analogous to the way Maxwell used Stokes’s theorem to express Ampère’s and Faraday’s laws as differential equations (see *Treatise on Electricity and Magnetism*, 2:29, 45, 147–48, 233, 251, 255). It involves another vector calculus operation, not divergence but *curl*, and in the next chapter we’ll meet both these vector operations.

<!--p371-->
[^ch06n22]: *Einstein’s quote* is from Albert Einstein, *Ideas and Opinions* (1954; New York: Three Rivers Press, 1982), 327. *Maxwell’s great guns* is from a letter to Charles Cay, reprinted in Campbell and Garnett, *Life of Maxwell*, 169.

[^ch06n23]: This is because the general wave equation is differential; but to get out the electromagnetic wave equation you also need Maxwell’s theoretical change to Ampère’s law, i.e., the addition of the “displacement current.”

[^ch06n24]: Quotes are from Anne van Weerden, *A Victorian Marriage: Sir William Rowan Hamilton* (Stedum, Netherlands: J. Fransje van Weerden, 2017), 10, 56, 326.

[^ch06n25]: Van Weerden, *A Victorian Marriage*, 326.

[^ch06n26]: *On the Edinburgh posting (and Barrie)*: Forfar and Pritchard, “Remarkable Story.” *Quote from Barrie*: Raymond Flood, “Thomson and Tait: The Treatise on Natural Philosophy,” in Raymond Flood, Mark McCartney, and Andrew Whitaker, *Kelvin: Life, Labours and Legacy*, Oxford Scholarship Online (May 2008): DOI: 10.1093/acprof:oso/9780199231256.001.0001. *Gill on Maxwell’s teaching*: Reid, “Maxwell’s Scottish Chair,” 1673.

## CHAPTER 7

[^ch07n1]: *Tait to Thomson*: in R. Flood, “Thomson and Tait: The Treatise on Natural Philosophy,” in Raymond Flood, Mark McCartney, and Andrew Whitaker, *Kelvin: Life, Labours and Legacy* (Oxford: Oxford University Press, 2008) and Scholarship Online (2021), 176. DOI: 10.1093/acprof:oso/9780199231 256.003.0011.

[^ch07n2]: *Tait’s study and list*: Cargill Gilston Knott, *The Life and Scientific Work of P. G. Tait* (London: Cambridge University Press, 1911), 33, 43.

<!--p372-->
[^ch07n3]: *On the origins of Maxwell’s nickname*: The equation appears in section 162 of Tait’s *Sketch of Thermodynamics* (Edinburgh: Edmonston and Douglas, 1868). See also M. J. Klein, “Maxwell, His Demon, and the Second Law of Thermodynamics,” in *Maxwell’s Demon: Entropy, Information, Computing*, ed. Harvey Leff and Andrew Rex (Princeton, NJ: Princeton University Press, 1990), 85–86. Klein’s article is from 1970; Maxwell’s “demon” was a thought experiment that helped clarify the nature of thermodynamics.

[^ch07n4]: *Maxwell’s review*: *Scientific Papers of James Clerk Maxwell*, ed. W. D. Niven (Cambridge: Cambridge University Press, 1890), 326–27. *Maxwell to Tait*, December 21, 1871, Knott, *Life of Tait*, 150.

[^ch07n5]: *Maxwell to Tait* (with my emphasis), November 14, 1870, in Michael J. Crowe, *A History of Vector Analysis* (Notre Dame, IN: University of Notre Dame Press, 1967), 132; Maxwell to Campbell, October 19, 1872, in Lewis Campbell and William Garnett, *The Life of James Clerk Maxwell* (London: Macmillan, 1882), 186. Maxwell’s “Classification” paper was published in *Proceedings of the London Mathematical Society* (March 9, 1871): 224–33.

[^ch07n6]: *Maxwell to Tait* about vector calculus names: November 7, 1870, quoted in Knott, *Life of Tait*, 167.

[^ch07n7]: Maxwell defined “convergence,” the negative of divergence, in his *Treatise on Electricity and Magnetism* (Oxford: Clarendon Press, 1873), 1:28 (art. 25). The whole-vector equations in the narrative are given in Maxwell’s *Treatise*, vol. 2 (3rd ed.), 252, 259. Minus sign aside, you can see that his version is the same as ours when you look at his component versions, in articles 77 (or my fig. 7.1) and 612. Maxwell has an additional proportionality constant *K* in his definition of 𝔇, but he notes that for air *K* = 1. So, to keep the vector ideas foremost, I’ll generally write his equations assuming units are chosen to make various electrical and magnetic constants equal to 1. (Some modern texts have also scaled out the 4π in the div ***E*** equation.) 𝔇 is the electric displacement; Maxwell’s definition given in the narrative is for isotropic substances. Note that in his whole vector equation in vol. 2 he uses *e* instead of ρ, which he’d used in article 77 of vol. 1, and which is used today—so I’ve used ρ in my narrative.

[^ch07n8]: *Maxwell to Tait* (with my emphasis), November 2, 1871, in Crowe, *History of Vectors*, 133.

[^ch07n9]: The analogous equations in electromagnetism and general relativity include the Bianchi identities, which we’ll meet briefly in chapter 13. In electromagnetism, these identities include the div ***B*** equation reflecting that there are no magnetic monopoles. Tony and I have not yet written up our partial results, but an early paper is R. Arianrhod, A. W.-C. Lun, C. B. G. McIntosh, and Z. Perjés, “Magnetic Curvatures,” *Classical and Quantum Gravity* 11 (1994): 2331–34.

<!--p373-->
[^ch07n10]: Maxwell writes (what we would call) the div ***B*** equation in component form in his *Treatise*, 2:248 (art. 604), noting it follows from equation (A) art. 591 (233). Bruce Hunt (*The Maxwellians* [Ithaca, NY: Cornell University Press, 1991], 245) mentions the component form (which Hunt labels A′) but says that Maxwell wrote this as *S*. ∇𝔅 = 0. This is certainly the equivalent in Hamiltonian notation of the component equation on 248, although I can’t find it in my third edition copy of the *Treatise*.

[^ch07n11]: *Vector potential*: Maxwell, *Treatise*, vol. 2, arts. 405, 422–23, 592: he defines the vector potential ***A*** so that the line integral of ***A*** equals (via Stokes’s theorem) the surface integral of the magnetic field ***B*** (which is the curl of the vector potential ***A***). He also gives it a physical interpretation, in terms of magnetic moments (art. 405) and electromagnetic momentum, arts. 590, 592, 618—although this is via mathematical analogy rather than by a direct physical match; for example, he chooses the term “electromagnetic momentum” because mathematically it is the time integral of a force (art. 590)—that is, its time-derivative is a force, just like ordinary Newtonian momentum.

[^ch07n12]: *The whole-vector equation*: *Treatise on Electricity and Magnetism*, vol. 2 (3rd ed.), 258 (component form, 233, 248). *Potential*: modern notation varies, but ***A*** is used fairly widely, e.g., Luciano Maiani and Omar Benhar, *Relativistic Quantum Mechanics* (Boca Raton, FL: CRC Press, 2016), 56; Ray D’Inverno, *Introducing Einstein’s Relativity* (Oxford: Clarendon Press, 1992), 160; Walter Strauss, *Partial Differential Equations* (New York: Wiley, 1992), 342; Bernard Schutz, *A First Course in General Relativity* (Cambridge: Cambridge University Press, 1985), 211.

[^ch07n13]: *Maxwell to Campbell*: Campbell and Garnett, *Life of Maxwell*, 186.

[^ch07n14]: *Maxwell’s Watt Lecture*: *The Scientific Letters and Papers of James Clerk Maxwell*, ed. P. M. Harman, 2 vols. (Cambridge: Cambridge University Press, 1990, 1995), 791.

[^ch07n15]: Tait’s book, *Introduction to Quaternions*, was coauthored with his former teacher Philip Kelland. *Maxwell’s review* (with my emphasis): *Nature* 9 (1873): 137–38; Crowe, *History of Vectors*, 133. *Newton*: letter to Halley, in, e.g., Nicolae Sfetcu, “Isaac Newton vs Robert Hooke on the Law of Universal Gravitation,” SetThings ( January 14, 2019), MultiMedia Publishing, DOI:10.13140/RG.2.2.19370.26567, Creative Commons.

[^ch07n16]: *Maxwell, Tait, and Balfour*: Knott, *Life of Tait*, 149–50. *Kovalevsky*: Sophie Kowalevski, “Sur le problème de la rotation d’un corps solide autour d’un point fixe,” *Acta Mathematica* 12 ( January 1889): 177–232. It won the Prix Bordin in 1888.

[^ch07n17]: *Maxwell’s “physical reasoning”*: *Treatise on Electricity and Magnetism* 1:9 (art. 11).

<!--p374-->
[^ch07n18]: *Thomson to R. B. Hayward*, 1892, in Crowe, *History of Vectors*, 120.

[^ch07n19]: *Cayley’s portrait/Maxwell’s poem*: Alexander MacFarlane, *Lectures on Ten British Mathematicians* (1916), chap. 5. *Clifford’s gymnastics*: Carl Boyer, *A History of Mathematics*, rev. Uta Merzbach (New York: John Wiley and Sons, 1991), 592; see also Monty Chisholm, “Science and Literature Linked: The Story of William and Lucy Clifford,” *Advances in Applied Clifford Algebras* 19 (2009): 657–71.

[^ch07n20]: *Clifford’s atheism*: Sally Shuttleworth, “Science and Periodicals: Animal Instinct and Whispering Machines,” in Juliet John, ed., *The Oxford Handbook of Victorian Literary Culture* (2016), DOI: 10.1093./oxfordhb/9780199593736.013.31.

[^ch07n21]: *Tait’s review*: reprinted in Knott, *Life of Tait*, 270–72.

[^ch07n22]: *Inverse of a quaternion q* is *q*^**−1**^ = *q*^*****^/*qq*^*****^, where *q*^*****^ is the complex conjugate of *q*. If you multiply out *qq*^**−1**^ you’ll find that it does indeed give 1.

[^ch07n23]: The American mathematician David Hestenes was the first modern mathematician to recognise, in the 1960s, the importance of Clifford and Grassmann for geometric algebra, which Hestenes and others have since developed further. Wedge products are important in modern tensor analysis (they are defined in terms of the tensor products we’ll see in chap. 11).

[^ch07n24]: *Tait to Cayley*: Knott, *Life of Tait*, 155.

[^ch07n25]: *Liberal utilitarian*: David Weinstein, “Herbert Spencer,” in Edward Zalta, ed., *Stanford Encyclopedia of Philosophy* (Fall 2019), plato.stanford.edu. *Maxwell and Tait*: e.g., Knott, *Life of Tait*, 284–88.

[^ch07n26]: *Lewes’s mind-body analysis today*: Elfed Huw Price, “George Henry Lewes (1817–1878): Embodied Cognition, Vitalism, and the Evolution of Symbolic Perception,” in *Brain, Mind and Consciousness in the History of Neuroscience*, ed. Chris Smith and Harry Whitaker (New York: Springer, 2014), 105–23. *Tait, Lewes, Blackwood*: Gordon Haight, ed., *The George Eliot Letters* (New Haven, CT: Yale University Press, 1955), 5:401, 417, and 9n181.

[^ch07n27]: *Maxwell’s poem*: “British Association, 1874” was published in the December 1874 issue of *Blackwood’s*: Campbell and Garnett: *Life of Maxwell*, 8 (poem reprinted, 326).

[^ch07n28]: *Tait and Blackwood at Golf (and Maxwell “better ½”)*: Martin Goldman, *The Demon in the Aether* (Edinburgh: Paul Harris Publishing, 1983), 105.

[^ch07n29]: For more on Maxwell’s poem and related debates, see Raymond Flood, Mark McCartney, and Andrew Whitaker, *James Clerk Maxwell: Perspectives on His Life and Work* (Oxford: Oxford University Press, 2014).

<!--p375-->
[^ch07n30]: *Maxwell to Campbell*: Campbell and Garnett, *Life of Maxwell*, 202.

[^ch07n31]: Knott, *Life of Tait*, 261.

[^ch07n32]: *Shaw to Lucy*: quoted in Chisholm, “Science and Literature Linked,” 668.

## CHAPTER 8

[^ch08n1]: Bruce Hunt coined the term “Maxwellians,” in his *The Maxwellians* (Ithaca, NY: Cornell University Press, 1991). *Lodge scooped*: James Rautio, “Twentythree Years: Acceptance of Maxwell’s Theory,” *Applied Computational Electromagnetics Society Journal* 25, no. 12 (December 2010), 998–1006.

[^ch08n2]: *On Heaviside*: Here and in the following paragraphs I’ve drawn on Bruce Hunt, “Oliver Heaviside: A First-Rate Oddity,” *Physics Today* 65, no. 11 (2012): 48–54, DOI: 10.1063/PT.3.1788; Jed Buchwald, “Oliver Heaviside, Maxwell’s Apostle and Maxwellian Apostate,” *Centaurus* 28 (1985): 288–330; I. Yavetz, *From Obscurity to Enigma: The Work of Oliver Heaviside, 1872–1889* (Basel: Springer, 2011); and Heaviside’s papers, which I’ll generally cite as I go.

[^ch08n3]: *Maxwell’s Reference to Heaviside* was added to his list of errata (p. 2) for vol. 1, with reference to p. 404. *Heaviside on Maxwell’s* Treatise: Rautio, “Twentythree Years.”

[^ch08n4]: *Heaven-sent Maxwell*: Oliver Heaviside, *Electromagnetic Theory* (London, 1893; New York: Chelsea Publishing, 1971), 1:14.

[^ch08n5]: *Worshipping quaternions*: Heaviside, *Electromagnetic Theory*, 1:136.

[^ch08n6]: Heaviside, *Electromagnetic Theory*, 1:137, 139.

[^ch08n7]: *Heaviside eliminating imaginary numbers* from vectors: *Electromagnetic Theory*, 1:137, 142, 149. *His drollery*: *Electromagnetic Theory*, 1:135.

[^ch08n8]: Heaviside missed at BAAS: *Engineering* 46 (1888): 352; cited in Hunt, “Oliver Heaviside,” 52–53.

[^ch08n9]: *Pot and kettle*: Heaviside, *Electromagnetic Theory*, 1:203; *Murdering potentials*: letter to FitzGerald, quoted in Rautio, “Twenty-three Years,” 1004.

[^ch08n10]: *Heaviside not quite in “modern” form*: In most undergrad textbooks, Maxwell’s equations are written in terms of ***E*** and ***B***, but for Heaviside it is ***E*** and ***H*** that are singled out. Maxwell had distinguished between the magnetic induction or magnetic field, ***B***, which is a *flux*, and the magnetic *force, **H***. When the magnetic field is induced entirely by the magnetic force, then ***B*** = μ***H***, where μ is the coefficient of the magnetic permittivity. This is the definition Heaviside used, so it is straightforward to change from ***H*** to ***B*** when looking at his equations. He also used Maxwell’s definition of the electric displacement ***D***, a flux, in terms of the force ***E***, namely ***D*** = *c**E***/4π.

    Today some authors still use ***H***, but using ***B*** makes Heaviside’s equations more symmetrical. Some authors also use ***D*** instead of ***E*** in the divergence equation, following Maxwell and Heaviside, but as I mentioned it is numerically proportional to ***E***.

<!--p376-->
[^ch08n11]: *Potentials unphysical (for localized energy)*: This is explained in detail in Buchwald, “Oliver Heaviside,” 293. *Maxwell’s wave equations*: in terms of potential, *Treatise* 2, 434 (art. 784); in terms of magnetic field, “A Note on the Electromagnetic Theory of Light,” *Philosophical Transactions of the Royal Society* 158 (1868): 643–57, esp. 655.

    In this 1868 paper, Maxwell’s four field equations are not quite the four modern equations, but he deduces from them the wave equation for the magnetic field. This is just what Heaviside was trying to do when he “murdered” the potentials! It’s a pity Maxwell didn’t take this approach further— but as Heaviside noted (*Electromagnetic Theory*, 1:69), Maxwell didn’t do his own theory justice in the *Treatise*: instead he provided a brilliant overview of all the contributions to the study of electromagnetism that had been made so far. He certainly showed how and why he developed his theory from the earlier known work, and how it compared with others’ action-at-a-distance models, but he definitely wasn’t a self-promoter.

[^ch08n12]: These four equations look slightly different in different texts; it depends on how the units of the electrical and magnetic constants are chosen. In particular, along with electric and magnetic constants the speed of light *c* is often set to 1 (as I’ve done here), but, following Heaviside, the factor of 4π is often effectively set to 1 by adjusting the units of the constants. (Also, some texts use Heaviside’s “div” and “curl” instead of Gibbs’s dot and cross.)

[^ch08n13]: Heaviside was so entranced by the symmetry between the electric and magnetic fields in the four key Maxwell equations that he added a fictitious magnetic “charge” to the equation ∇ ∙ ***B*** = 0 (thereby positing that there *are* magnetic monopoles—just as Dirac did nearly half a century later) and a magnetic “current” to the ∇ × ***E*** equation. But these additions don’t yet have any known physical basis (aside from artificially generated short-lived quantum monopoles), so they are generally left out of the modern electromagnetic equations; this means that—vector formalism aside—the modern equations are indeed *Maxwell’s* equations, as my narrative shows.

<!--p377-->
[^ch08n14]: *Finding* ∇ × ***E** from Maxwell’s whole vector equation* in his *Treatise on Electricity and Magnetism*, vol. 2 (3rd ed., 1891; reprint, Dover, 1954): For example, on 2:232 (art. 590), Maxwell gives (in words) the definition ***A*** = ∫***E** dt*, or equivalently (equation 29 of his 1865 paper), ***E*** = −*d**A***/*dt*. Taking the curl of both sides of this, and remembering that Maxwell defined ***B*** = ∇ × ***A***, you have (using the fact that you can interchange the order of derivatives)

::: {.displayeq}

$$\nabla\times\boldsymbol{E}=-\frac{d}{dt}\left(\nabla\times\boldsymbol{A}\right)=-\frac{d\boldsymbol{B}}{dt}.$$

:::

    Alternatively, begin with Maxwell’s equation (*Treatise* 2:258 [art. 619]) as given in my narrative,

::: {.displayeq}

$$\boldsymbol{E}=v\times\boldsymbol{B}-\frac{d\boldsymbol{A}}{dt}-\nabla\phi,$$

:::

    and then take the curl of both sides. Using the identity curl grad = 0, the last term drops out. If there are no moving charges, so the electric field is induced only by a time-varying magnetic field (cf. *Treatise* 2:240–41 [art. 599], 2:433 [art. 783]), then ***v*** = 0. So again you $\nabla\times\boldsymbol{E}=-\frac{d}{dt}\left(\nabla\times\boldsymbol{A}\right)=-\frac{d\boldsymbol{B}}{dt}$

[^ch08n15]: *Maxwell’s five vector (quaternion) equations* are in his *Treatise* 2:258–59. (There are also seven definition equations on these pages—just as Heaviside used.) Heaviside specifically said that his form of the equations should still be called Maxwell’s equations: *Electromagnetic Theory*, vol. 1, preface (fifth page), and 69. Hertz agreed: Rautio, “Twenty-three Years,” 1005.

[^ch08n16]: Heaviside, *Electromagnetic Theory*, 1:297.

[^ch08n17]: *Gibbs’s path to vectors*: he was first inspired by Maxwell, then branched out on his own—independently of Grassmann, whom he discovered several years later. We know this from his letter to Victor Schlegel, published much later by Gibbs’s student Lynde Phelps Wheeler, in his book *Josiah Willard Gibbs: The History of a Great Mind* (New Haven, CT: Yale University Press, 1952).

[^ch08n18]: *Gibbs’s reply to Tait’s “monster”*: “On the Role of Quaternions in the Algebra of Vectors,” *Nature* 43 (April 2, 1891): 511–13. *Heaviside* (incl. “hermaphrodite monster” quote and citation): *Electromagnetic Theory*, 1:137–38, 301.

[^ch08n19]: Peter Guthrie Tait, “The Role of Quaternions in the Algebra of Vectors,” *Nature* 43 (April 30, 1891): 608. For a detailed analysis of the vector wars on which I’ve gratefully drawn, see Michael J. Crowe, *A History of Vector Analysis* (Notre Dame, IN: University of Notre Dame Press, 1967), chap. 6.

[^ch08n20]: *Thomson’s “war over quaternions”*: Cargill Gilston Knott, *The Life and Scientific Work of P. G. Tait* (London: Cambridge University Press, 1911), 185.

<!--p378-->
[^ch08n21]: Knott, *Life of Tait*, 185; Alexander Macfarlane, “Principles of the Algebra of Vectors,” *Proceedings of the American Association for the Advancement of Science* 40 (1891, published 1892): 65–117; Alexander McAulay, “Quaternions as a Practical Instrument of Physical Research,” *Philosophical Magazine*, 5th ser., 33 ( June 1892): 477–95; Crowe, *History of Vectors*, 189–97.

[^ch08n22]: Martin Rees offers solutions to these problems in *If Science Is to Save Us* (Cambridge: Polity Press, 2022).

[^ch08n23]: McAulay quoted in Crowe, *History of Vectors*, 195. *Ida McAulay*: Bruce Scott, “McAulay, Alexander,” *Australian Dictionary of Biography*, adb.anu.edu.au.

[^ch08n24]: *Tait’s review of McAulay*: *Nature* 49 (December 28, 1893): 193–94.

[^ch08n25]: Heaviside, “Vectors versus Quaternions,” *Nature* (April 6, 1893): quoted in Crowe, *History of Vectors*, 200. *Hydroelectricity*: Scott, “McAulay, Alexander”; Carol Raabus and Leon Compton, “The Engineering Feats of Tasmania’s Hydroelectric System,” ABC Radio, July 29, 2013.

[^ch08n26]: Gibbs, “Quaternions and the Algebra of Vectors,” *Nature* 47 (March 16, 1893): 463–64.

## CHAPTER 9

[^ch09n1]: *Grace Chisholm on Cayley*: I. Grattan-Guinness, “A Mathematical Union: William Henry and Grace Chisholm Young,” *Annals of Science* 29, no. 2 (August 1972): 117–18.

[^ch09n2]: *History of Newnham*: https://newn.cam.ac.uk/about/history/history-of-newnham/. Women were finally allowed to take full degrees at Oxford in 1920 but not at Cambridge until 1948.

[^ch09n3]: Cayley and Tait’s letters are in Cargill Gilston Knott, *The Life and Scientific Work of P. G. Tait* (London: Cambridge University Press, 1911), 154–96.

[^ch09n4]: At the time of writing, many of these machine-made predictions still need to be verified in the lab, but even so they can point the way for genomics research.

[^ch09n5]: *Invariance of the discriminant under translations*: The quadratic equation *ax*^**2**^ + *bx* + *c* = 0 has the solution $x=\left[-b\pm\sqrt{b^{2}-4ac}\right]/2a$. If we transform *x* to *x′* = *x* + *h*, the associated quadratic equation is now *ax′*^**2**^ + *bx′* + *c* = 0, whose solution is $x'=\left[-b\pm\sqrt{b^{2}-4ac}\right]/2a$. The discriminants are the same, *b*^**2**^ − 4*ac*, but the solutions are not the same: for the translated equation we have $x'=x+h=\left[-b\pm\sqrt{b^{2}-4ac}\right]/2a$, which implies that $x=\left[-b-2ah\pm\sqrt{b^{2}-4ac}\right]/2a$; but this is not equal to the original solution, $x=\left[-b\pm\sqrt{b^{2}-4ac}\right]/2a$.

[^ch09n6]: *Cayley and Tait quotes*: Michael J. Crowe, *A History of Vector Analysis* (Notre Dame, IN: University of Notre Dame Press, 1967), 212, 214. *Grace Chisholm on Cayley*: Grattan-Guinness, “A Mathematical Union,” 117.

[^ch09n7]: Crowe, *History of Vectors*, 214.

<!--p379-->
[^ch09n8]: Crowe, *History of Vectors*, 217.

[^ch09n9]: He mentioned anti-Semitism in connection with his job-hunting in a letter to Mileva Marić on March 27, 1901: *Collected Papers of Albert Einstein*, vol. 1, ed. John Stachel, David C. Cassidy, and Robert Schulmann (Princeton, NJ: Princeton University Press, 1987; English Supplement translated by Anna Beck), document 94, https://einsteinpapers.press.princeton.edu/vol1-trans/182.

<!--p380-->
[^ch09n10]: In the letter of March 27, 1901, referred to in the previous endnote (https://einsteinpapers.press.princeton.edu/vol1-trans/182), Einstein looks forward to the day when “the two of us together will have brought our work on the relative motion to a victorious conclusion.” This has been cited by some scholars as evidence that Einstein and Marić were working together on relativity, although the context, and the words “victorious conclusion,” also suggest it might be a metaphor for their marriage plans (being held up by disapproval from relatives, Mileva’s struggle to graduate, and Einstein’s lack of employment). The only prior (and subsequent) times Einstein mentions relativity in the extant letters to Marić are, as far as I could find, in a letter of September 10, 1899 (*Collected Papers of Albert Einstein*, vol. 1, document 54), where he tells Mileva he’s had an idea about how relative motion with respect to the ether affects the velocity of light, adding, “But enough of that!” (because she is studying for her exams): https://einsteinpapers.press.princeton.edu/vol1-trans/155; and again in document 57, September 28, 1899, where there is no mention of “our” theory, and similarly in document 128, December 17, 1901. Evidently, she never responded with comments on the subject, judging from her letters and Einstein’s letters to her—rather, she was focussed on topics relevant to her exams. If only we knew what went on between them when they were together and didn’t need to write letters! Einstein certainly nourished early dreams that they would have a scientific life together—and in document 72 of this volume (August 14, 1900), he tells her that he lacks self-confidence and pleasure in work when he is not with her. Few of Marić’s letters from this time survive: those that do are focussed on her dreams of getting married, passing her diploma exams, and starting her PhD (and her diploma thesis was on heat and energy, not relativity). As for her “doing Einstein’s maths for him,” their exam results in 1900 suggest that Einstein excelled at maths and she failed: document 67 of vol. 1, https://einsteinpapers.press.princeton.edu/vol1-trans/163. Exam results are not everything of course, but it does put to rest claims of Einstein’s mathematical incompetence. In my view we can do more justice to Marić as a female scientific pioneer by examining the prejudice that blighted her career, rather than claiming things for which there is no clear evidence. More information about the relationship, and about the special theory of relativity, is in my short e-book *Young Einstein and the Story of E = mc*^2^ (Sydney: Ligature, 2014), and the references therein. For a very brief, updated overview of the evidence for the claim of Mileva Marić as coauthor, see Ann Finkbeiner, “The Debated Legacy of Einstein’s First Wife,” *Nature* 567 (2019): 28–29.

[^ch09n11]: *Maxwell’s idea* was expressed in his entry “Ether” in the 9th edition of *Encyclopaedia Britannica* (1878), 8:568–72, and in more detail in a letter to David Peck Todd, March 19, 1879, a few months before he died. Todd recognised its importance and sent it to Stokes, who communicated it to the Royal Society, which published it in its proceedings: “‘On a possible method of detecting the motion of the solar system through the luminiferous ether’ by the late Professor J. Clerk Maxwell,” *Proceedings of the Royal Society*, January 22, 1880, 108–10. *Michelson studied this letter*, for he worked in Todd’s office. See also Robert Shankland, “Michelson and His Interferometer,” *Physics Today* 27, no. 4 (1974): 37, DOI: 10.1063/1.3128534; Shankland includes a photo of Michelson’s interferometer. *In their paper reporting their results, however*, Michelson and Morley mention the satellite method as a possible future experiment in light of their negative result, but they do not cite Maxwell; presumably they didn’t know his letter had been published: Albert A. Michelson and Edward W. Morley, “On the Relative Motion of the Earth and the Luminiferous Ether,” *American Journal of Science*, ser. 3, 34, no. 203 (November 1887): 345.

[^ch09n12]: *Lorentz electron theory*: Maxwell had assumed charge was continuously distributed—hence the charge density term ρ and current density ***J*** in his equations; Lorentz showed that these densities are an approximation or average of the distribution of charges (points), and that Maxwell’s equations are singular at these points, but hold everywhere else. *Einstein on Lorentz*: Albert Einstein, *Ideas and Opinions* (1954; New York: Three Rivers Press, 1982), 73–76, and Banesh Hoffman (with the collaboration of Helen Dukas), *Einstein* (Frogmore: Paladin, 1975), 98.

<!--p381-->
[^ch09n13]: H. Poincaré, “Sur la dynamique de l’électron,” *Rendiconti del Circolo Matematica di Palermo* 21 (1906): 18–76. He’d already presented a preliminary “Note” on this paper, to the Académie des Sciences, June 5, 1905, and had written on related ideas several years earlier. For the English version of Einstein’s 1905 paper (originally published in *Annalen der Physik*): A. Einstein, “On the Electrodynamics of Moving Bodies,” in H. A. Lorentz et al., *The Principle of Relativity* (New York: Dover, 1952), 37–65.

[^ch09n14]: As early as 1910, Felix Klein, who had been working on the geometry of Lorentz groups that are fundamental in Einstein’s special theory, claimed that one could, “if one really wanted to, replace the term ‘theory of invariants with respect to a group of transformations’ with the term ‘relativity with respect to a group’” (quoted in Yvette Kosmann-Schwarzbach [translated by Bertram E. Schwarzbach], *The Noether Theorems: Invariance and Conservation Laws in the Twentieth Century* [New York: Springer, 2011], 70). In 2022 (in *If Science Is to Save Us* [Cambridge: Polity, 2022], 93), Martin Rees suggested the name “theory of invariance” instead of “relativity” would have avoided “misleading analogies with relativism in human contexts.”

[^ch09n15]: *Grace Chisholm and higher dimensions*: Her recollection is reproduced in Grattan-Guinness, “A Mathematical Union,” 128–29.

[^ch09n16]: For a beautiful account of these 4-D efforts and their context (including the Booles, and hyper-square analogy), see Nicholas Mee, *Celestial Tapestry: The Warp and Weft of Art and Mathematics* (Oxford: Oxford University Press, 2020).

[^ch09n17]: For a modern analysis of (bi-)quaternions in SR, see Joachim Lambek, “In Praise of Quaternions,” *Comptes Rendues Mathematical Reports*, Academy of Sciences, Canada, 35, no. 4 (2013): 121–36; https://www.math.mcgill.ca/barr/lambek/pdffiles/Quater2013.pdf. Hamilton himself discussed biquaternions (which have complex coefficients).

[^ch09n18]: *“Lazy dog”*: quoted in Michael White and John Gribbin, *Einstein: A Life in Science* (London: Simon and Schuster, 1993), 39. *Minkowski on quaternions*: Scott Walter, “Breaking in the 4-vectors: The Four-dimensional Movement in Gravitation, 1905–1910,” in *The Genesis of General Relativity*, ed. Jürgen Renn (Dordrecht: Springer, 2007), 3:212.

[^ch09n19]: Minkowski quoted in Constance Reid, *Hilbert* (Berlin: Springer-Verlag, 1970), 105, 112.

[^ch09n20]: *The interval* tells you how to take account of the “distance” between two events taking place at two different places and times:

::: {.displayeq}

$$\sqrt{\left(x_{2}-x_{1}\right)^{2}+\left(y_{2}-y_{1}\right)^{2}+\left(z_{2}-z_{1}\right)^{2}-\left(c\left(t_{2}-t_{1}\right)\right)^{2}}.$$

:::

    If you observe two events, one after the other, from the *same* point in space, then the interval tells you the time between them according to your own wristwatch (because *x*~2~ − *x*~1~, *y*~2~ − *y*~1~, *z*~2~ − *z*~1~ are all zero). This is called the “proper” time. Similarly, if you measure two events at the same time, the metric tells you the (proper) distance between them (because *t*~2~ − *t*~1~ is now zero). But as the Lorentz transformations show, there is no agreement from a relatively moving observer on these times and distances—both of you only agree that the *interval as a whole is invariant*.

    By the way, to turn the “signature” (as it’s called) of this quadratic interval measure into + + + + rather than + + + − Minkowski made the time imaginary, to fit with the original idea of a quadratic form.

<!--p382-->
[^ch09n21]: H. Minkowski, “Space and Time,” 1908, English translation in H. A. Lorentz et al., *Principle of Relativity*, 75–91. Turning red: Reid, *Hilbert*, 92. On the 1907 lecture: Walter, “Breaking in the 4-vectors,” 219.

[^ch09n22]: *On Minkowski’s death*: Reid, *Hilbert*, 115.

[^ch09n23]: *Klein and Justus*: Crowe, *History of Vectors*, 92.

[^ch09n24]: *Invariant space-time interval/constant c*: Speed is distance/time, so in 3-D space, the speed of light can be defined using Pythagoras’s theorem for the distance:

::: {.displayeq}

*c*^**2**^ = (*x*^**2**^ + *y*^**2**^ + *z*^**2**^)/*t*^**2**^;

:::

    another way of writing this equation is, of course,

::: {.displayeq}

*x*^**2**^ + *y*^**2**^ + *z*^**2**^ − (*ct*)^**2**^ = 0.

:::

    The expression on the left is invariant under Lorentz transformations, which means that when the coordinates (*x, y, z, t*) and (*x′, y′, z′, t′*) are related via a Lorentz transformation, you still get

::: {.displayeq}

*x*^**2**^ + *y*^**2**^ + *z*^**2**^ − (*ct*)^**2**^ = *x′*^**2**^ + *y′*^**2**^ + *z′*^**2**^ − (*ct′*)^**2**^.

:::

    Which means that *x′* ^**2**^ + *y′* ^**2**^ + *z′* ^**2**^ − (*ct′*)^**2**^ = 0, too, and so the speed of light in the (*x′, y′, z′, t′*) frame must also be *c*.

[^ch09n25]: William Thomson, “Elements of a Mathematical Theory of Elasticity,” *Philosophical Transactions of the Royal Society of London* 146 (1856): 481–98; Augustin Cauchy, “Sur les equations qui experiment les conditions d’équilibre ou les lois du movement intérieur d’un corps solide, élastique ou nonélastique,” *Exercises de Mathématiques* 3 (1828): 160–87.

[^ch09n26]: Maxwell, *Treatise on Electricity and Magnetism* (Oxford: Clarendon Press, 1873), 2:278–81.

<!--p383-->
[^ch09n27]: Minkowski had called these particular two-index quantities “vectors of the second kind,” and Sommerfeld called them “six-vectors.” Today they are simply called tensors—in this case, antisymmetric second-rank or second-order tensors, where the “rank” or “order” refers to the number of indices on its components. (If these tensors are defined through space, rather than at one point, then technically they are tensor fields.)

## CHAPTER 10

[^ch10n1]: *Einstein’s PhD*: Banesh Hoffmann, *Einstein* (Frogmore: Paladin, 1975), 55. *Grossmann seeing Einstein’s greatness*: see my *Young Einstein* and references therein.

[^ch10n2]: Albert Einstein, *Ideas and Opinions* (1954; New York: Three Rivers Press, 1982), 289.

[^ch10n3]: *Einstein to Sommerfeld*: Judith Goodstein, *Einstein’s Italian Mathematicians* (Providence, RI: American Mathematical Society, 2018), 95.

[^ch10n4]: *Gauss, surveying, and least squares*: Martin Vermeer and Antti Rasilia, *Map of the World: An Introduction to Mathematical Geodesy* (Milton Park, UK: Taylor and Francis, 2019), 181; Frank Reid, “The Mathematician on the Bank Note: Carl Friedrich Gauss,” *Parabola* 36, no. 2 (2000). Although Gauss retired from fieldwork in 1825, he directed the survey until its completion in 1844.

[^ch10n5]: Actually, Minkowski and Einstein wrote this metric with the plus and minus signs reversed:

::: {.displayeq}

*ds*^**2**^ = −*dx*^**2**^ − *dy*^**2**^ − *dz*^**2**^ + *c*^**2**^*t*^**2**^, or *ds*^**2**^ = *c*^**2**^*t*^**2**^ − *dx*^**2**^ − *dy*^**2**^ − *dz*^**2**^;

:::

    the choice of signs is called the “signature,” and for our purposes the key thing is that the time differential has the opposite sign from the spatial ones.

[^ch10n6]: *Outline of Gauss’s argument*: The page numbers here (and elsewhere) refer to the English version of Gauss’s 1828 paper, *General Investigations of Curved Surfaces of 1827 and 1825*, by Karl Friedrich Gauss, translated by James Morehead and Adam Hiltebeitel, Project Gutenberg, 2011 (from the 1902 edition, Princeton: Princeton University Library); https://www.gutenberg.org/files/36856/36856-pdf.pdf.

    I mentioned that for his 2-D surface Gauss transformed his three *x, y, z* coordinates to functions of two new variables, which he called *p, q*—so you can write the coordinate transformations (which I’ll make linear) as

::: {.displayeq}

*x* = *f*(*p, q*), *y* = *g*(*p, q*), *z* = *h*(*p, q*).

:::

    Then the chain rule gives

::: {.displayeq}

$$dx=\frac{\partial f}{\partial p}dp+\frac{\partial f}{\partial p}dq=adp+a'dq$$ in Gauss’s notation (p. 7).

:::

    (Unfortunately Gauss, like Riemann, used dashes instead of different letters.)

    Similarly, *dy* = *bdp* + *b′dq, dz* = *cdp* + *c′dq*. If you square these expressions and add, you get (cf. Gauss pp. 18, 20):

<!--p384-->
::: {.displayeq}

*dx*^**2**^ + *dy*^**2**^ + *dz*^**2**^ = (*a*^**2**^ + *b*^**2**^ + *c*^**2**^)*dp*^**2**^ + 2(*aa′* + *bb′* + *cc′*)*dpdq* + (*a′*^**2**^ + *b′*^**2**^ + *c′*^**2**^)*dq*^**2**^ = *Edp*^**2**^ + 2*Fdpdq* + *Gdq*^**2**^,

:::

    where Gauss used *E, F, G* to simplify the expression.

    But here’s the fascinating thing in hindsight: from the algebraic definition of scalar products, you can see that *E, F, G* are what we would now call scalar products of the vectors

::: {.displayeq}

***v*** = *a**i*** + *b**j*** + *c**k, v′*** = *a′**i*** + *b′**j*** + *c′**k***;

:::

    in other words,

::: {.displayeq}

*E* = ***v*** ∙ ***v**, F* = ***v*** ∙ ***v′**, G* = ***v′*** ∙ ***v′***.

:::

    These two vectors are the *unit tangent vectors* to the coordinate lines *p, q* as in fig. 10.4 in the narrative. (To see this, consider the infinitesimal displacement vector, using shorthand bracket notation for vectors:

::: {.displayeq}

*d**r*** = (*dx, dy, dz*) = (*a, b, c*)*dp* + (*a′, b′, c′*)*dq* = ***v**dp* + ***v′**dq*;

:::

    the *tangent vectors* are found by differentiating this with respect to the two coordinates, just as we differentiate an ordinary function to find the slope of its tangent:

::: {.displayeq}

$$\frac{dr}{dp}=v,\frac{dr}{dq}=v'.)$$

:::

    The geometric definition of the scalar product of two vectors is ***a.b*** = |***a***||***b***| cosθ, and as we saw in chapter 9, $|\boldsymbol{a}|=\sqrt{\boldsymbol{a}\cdot\boldsymbol{a}}$. So the angle between these two tangent vectors is

::: {.displayeq}

$$\cos\theta=\frac{v\cdot v'}{(\sqrt{v\cdot v)(v\cdot v'})}=\frac{F}{\sqrt{EG}}.$$

:::

    Later mathematicians will generalise this to arbitrary metrics and dimensions, where the coefficients in the metric are written as *g~ij~*: for the 2-D case here we’d have

::: {.displayeq}

$$\cos\theta=\frac{g_{12}}{\sqrt{g_{11}g_{22}}}.$$

:::

    To find the curvature of the surface, these formulae are applied to triangles whose sides are bounded by the coordinate lines, as in fig. 10.4, and then, as I explained in the narrative, the sum of the angles gives the nature of the curvature.

    By the way, if you’re familiar with double integrals, then the expression $\sqrt{EG-F^{2}}$ in the area integral I mentioned in the narrative is the Jacobian. It’s the determinant of the matrix of coefficients of the metric, and in terms of a general metric, as in GR, it is written as $\sqrt{-g}$.

    *Gauss’s definition of curvature in terms of angles*: p. 46 (and 44).

    *Harriot’s work*: see my *Thomas Harriot: A Life in Science* (New York: Oxford University Press, 2019), 160–61, and also John Stillwell, *Mathematics and Its History* (New York: Springer-Verlag, 1989), 249–50.

<!--p385-->
[^ch10n7]: *Hawking on black hole horizon (boundary)*: He published this result in 1972; he also proved it in S. W. Hawking and G. F. R. Ellis, *The Large Scale Structure of Space-time* (Cambridge: Cambridge University Press, 1973), 335–37. For a simple sketch of Hawking’s proof and a useful brief history of curvature, see Greg Galloway, “From the Shape of the Earth to the Shape of Black Holes: Aristotle to Hawking and Beyond,” Miami University’s Mathematics Department, Arts and Sciences Cooper Lecture, November 2017. For an interesting outline of the history of black holes, see the overview on the Nobel Prize website for the 2020 physics prize. Note that some researchers have suggested that the Event Horizon Telescope’s (EHT’s) first direct image of a black hole could, in fact, be that of a gravitomagnetic monopole rather than a black hole; they have calculated parameters that would distinguish the two possibilities when future, more accurate EHT observations are made: M. Ghasemi-Noedi et al., “Investigating the Existence of Gravitomagnetic Monopole in M87*,” *European Physics Journal C* 81, no. 939 (2021); https://doi.org/10.1140/epjc/s10052-021-09696-3.

[^ch10n8]: To take just one example, for an account that includes the role Gaussian curvature is playing in the study of the way materials wrinkle, and the possibilities for using these wrinkles in innovative new ways, see Stephen Ornes, “The New Math of Wrinkling,” *Quanta* magazine (September 22, 2022); https://www.quantamagazine.org/the-new-math-of-wrinkling-patterns-20220922/.

[^ch10n9]: Lewis Campbell and William Garnett, *The Life of James Clerk Maxwell* (London: Macmillan, 1882), 324–25.

[^ch10n10]: *Einstein Privatdozent*: Hoffmann, *Einstein*, 86–87. *Gauss on Riemann*: Raymond Flood and Robin Wilson, *The Great Mathematicians* (London: Arcturus, 2011), 160. *Seventy-seven-year-old Gauss*: Goodstein, *Einstein’s Italian Mathematicians*, 31. *Gauss devastated*: Stillwell, *Mathematics and Its History*, 253–54.

[^ch10n11]: An excellent, more technical account of Riemann’s working—and an English translation of the paper—is in Ruth Farwell and Christopher Knee, “The Missing Link: Riemann’s ‘Commentatio,’ Differential Geometry and Tensor Analysis,” *Historia Mathematica* 17 (1990): 223–55.

<!--p386-->
[^ch10n12]: Maxwell, *Treatise on Electricity and Magnetism* (Oxford: Clarendon, 1873), 1:333 (art. 280). Note that Thomson and Tait (in their *T&T′*, 1:515) denote coefficients of elasticity by pairs of letters, as Riemann did, rather than using indices as Maxwell did.

[^ch10n13]: Conductivity is a two-index tensor if the material is anisotropic, as Riemann assumed. For isotropic materials the heat spreads out in all directions, so there’s no need to worry about variations with direction, and you can use a scalar representation.

[^ch10n14]: Bernhard Riemann, translated into English by William Kingdon Clifford, “On the Hypotheses Which Lie at the Bases of Geometry,” *Nature* 8, no. 183 (1873): 14–17, and no. 184, 36–37.

[^ch10n15]: For detailed analyses of Riemann’s 1854 and 1861 papers, and the work of followers including Christoffel, see Olivier Darrigol, “The Mystery of Riemann’s Curvature,” *Historia Mathematica* 42 (2015): 47–83. See also Farwell and Knee, “Missing Link.” An English translation of Christoffel’s 1869 paper is given in chap. 8 of Bas Fagginger Auer’s “Christoffel Revisited” (master’s thesis, Mathematical Institute, University of Utrecht, 2009).

[^ch10n16]: If units are chosen so that *c* = 1, the coefficients are 1, 1, 1, −1. Riemann showed that if the metric has constant coefficients, the coordinates can be scaled so that all the coefficients in the metric are 1 (or −1, as Minkowski later showed).

## CHAPTER 11

[^ch11n1]: For Ricci’s biographical details, including political context, I’ve drawn throughout this chapter on Judith Goodstein, *Einstein’s Italian Mathematicians* (Providence, RI: American Mathematical Society, 2018).

[^ch11n2]: Goodstein, *Einstein’s Italian Mathematicians*, 2.

[^ch11n3]: *Ricci to Antonio Manzoni*, November 24, 1872, quoted in Goodstein, *Einstein’s Italian Mathematicians*, 6.

[^ch11n4]: Goodstein, *Einstein’s Italian Mathematicians*, 16.

[^ch11n5]: *Ricci and Chisholm on Klein*: quoted in Goodstein, *Einstein’s Italian Mathematicians*, 16, 17. NB: Sophie Kovalevsky’s Göttingen doctorate in 1874 was “unofficial,” like Chisholm’s Cambridge degree.

[^ch11n6]: Goodstein (*Einstein’s Italian Mathematicians*, 27–30) uses Ricci and Bianca’s letters to build a tender picture of their courtship.

[^ch11n7]: *Ricci’s introduction to his 1884 paper*: quoted in Goodstein, *Einstein’s Italian Mathematicians*, 32.

[^ch11n8]: W. H. and G. Chisholm Young, *Nature* 58, no. 1492 (June 2, 1898): 99–100.

<!--p387-->
[^ch11n9]: *Indices on the Riemann tensor*: Roughly speaking, since this tensor is made up of second derivatives of the two-index metric components, its four indices relate to which metric component is being differentiated by which pair of coordinates. It’s a little more complicated than this because the Riemann tensor is made of sums of derivatives of the metric components, but this is the general idea.

[^ch11n10]: Maxwell’s process is “additive”—you add the light from the three filters and project the image onto a screen. It is used today in slides and in TV and digital images. Printed images use the “subtractive” method (discovered after Maxwell paved the way), where the three colours are reflected from the pigment on the paper rather than transmitted through the filters/layers of pixels to a screen. The three primary colours of the subtractive method are the “opposites” of Maxwell’s—they are cyan, magenta, and yellow.

[^ch11n11]: *On the theft of data in training models for AI*: See, e.g., Nick Vincent and Hanlin Li, “ChatGPT Stole Your Work. So What Are You Going to Do?,” *Wired* ( January 28, 2023), https://www.wired.com/story/chatgpt-generative-artificial-intelligence-regulation/. For writers fighting back, see, e.g., Vanessa Thorpe, “‘ChatGPT Said I Did Not Exist’: How Writers and Artists Are Fighting Back against AI,” *The Guardian*, March 19, 2023.

<!--p388-->
[^ch11n12]: *Benefits and problems with NLP including LLMs*: Much will have changed by the time this book goes to press, such is the pace of AI development, but here are some recent references. For another example of the benefits, see Samantha Spengler, “For Some Autistic People, ChatGPT Is a Lifeline,” *Wired*, May 30, 2023; https://www.wired.com/story/for-some-autistic-people-chatgpt-is-a-lifeline/#. On the problems, in addition to the theft of training data, much has been written about the unreliability of some of ChatGPT’s output—so although there are clear benefits, the jury is still out on its role in education: see, e.g., Hayden Horner, “ChatGPT: Brilliance or a Bother for Education,” Engineering Institute of Technology’s news website, March 13, 2023, https://www.eit.edu.au/chatgpt-brilliance-or-a-bother-for-education/. Similarly, in telehealth (and much else), there are advantages and disadvantages: see, e.g., Som Biswas, “Role of ChatGPT in Public Health,” *Annals of Biomedical Engineering* (March 2023), published online at https://www.researchgate.net/profile/Som-Biswas-2/publication/369269117. There are obvious social problems with sophisticated AI, from enabling surveillance to creating deep fakes and fake news. I mentioned the problem of bias in the notes for chap. 4, but see also, e.g., Grace Browne, “AI Is Steeped in Big Tech’s ‘Digital Colonialism,’” *Wired UK* (May 25, 2023); https://www.wired.co.uk/article/abeba-birhane-ai-datasets. On a similar theme, see the series of articles “AI Colonialism” by *MIT Technology Review*, https://www.technologyreview.com/supertopic/ai-colonialism-supertopic/, which also includes examples where oppressed peoples are fighting back by using AI in positive ways. Then there are environmental issues, e.g., Maanvi Singh, “As the AI Industry Booms, What Toll Will It Take on the Environment?,” *The Guardian* (June 9, 2003). More than ever, informed public debate about science and technology is crucial!

[^ch11n13]: There’s much, much more to NLP and LLMs than tensor products, of course. For my account (and for more on NLP), I’m particularly indebted to Qiuyuan Huang, Paul Smolensky, Xiaodong He, Li Deng, Dapeng Wu, “Tensor Product Generation Networks for Deep NLP Modeling,” *Proceedings of NAACL-HLT 2018* (New Orleans): 1263–73; Lipeng Ahang et al., “A Generalized Language Model in Tensor Space,” 33rd Annual Conference of the AAAI (2019); and Matthew Kramer, “Word Embeddings,” Medium.com, August 31, 2021.

[^ch11n14]: “In principle, a quantum computer with 300 qubits could perform more calculations in an instant than there are atoms in the visible universe”: Charles Q. Choi, “How Many Qubits Are Needed for Quantum Supremacy?” *IEEE News*, May 21, 2020; https://spectrum.ieee.org/qubit-supremacy#:~:text=Superposition%20lets%20one%20qubit%20perform,eight%20calculations%3B%20and%20so%20on.

[^ch11n15]: *Enrico Betti*: Stokes’s theorem in *n*-D: Victor Katz, “The History of Differential Forms from Clairaut to Poincaré,” *Historia Mathematica* 8 (1981): 161– 88, esp. 175. *Betti as soldier, contributor to journal*: Goodstein, *Einstein’s Italian Mathematicians*, 7. *Betti and Ricci’s papers*: Goodstein, *Einstein’s Italian Mathematicians*, 148.

[^ch11n16]: Ricci’s letter, quoted in Goodstein, *Einstein’s Italian Mathematicians*, 9–10.

[^ch11n17]: *Ricci’s long fight for promotion*: Goodstein, *Einstein’s Italian Mathematicians*, 35–43, 59–61.

[^ch11n18]: G. Ricci and T. Levi-Civita, “Méthodes de calcul différential absolu et leurs applications,” *Mathematische Annalen* 54 (1900): 125–201; see 128 for effort and reward in learning a new skill (my translation).

[^ch11n19]: For instance, if, following fig. 11.1, you form a second-order tensor *T* via the tensor (or outer) product of two *contravariant* vectors ***a*** and ***b***, you’ll have the transformation rule

::: {.displayeq}

$$T^{\mu'v'}\equiv a^{\mu'}b^{v'}=\left(A_{\sigma}^{\mu'}a^{\sigma}\right)\left(A_{\lambda}^{v'}a^{\lambda}\right)=A_{\sigma}^{\mu'}A_{\lambda}^{v'}a^{\sigma}a^{\lambda}\equiv A_{\sigma}^{\mu'}A_{\lambda}^{v'}T^{\sigma\lambda}.$$

:::

    Don’t forget that the letters used for the tensors, transformation matrix coefficients, and indices here are arbitrary, like *x* in algebra. But what marvelous flexibility they offer, since you can move the transformation symbols around so easily, giving the rule for any kind of tensor you like!

<!--p389-->
[^ch11n20]: *Unruh effect*: In 1976 the Canadian physicist William Unruh found, with the help of quantum theory, that the general theory of relativity predicts that temperature is not exactly the coordinate-independent scalar I said it was in fig. 11.1. Rather, an accelerating observer will measure a slightly different space-time temperature than a stationary observer will. This “Unruh effect” hasn’t yet been detected—you’d need to be traveling close to the speed of light to detect one degree of temperature change. But in 2022 a University of Adelaide team led by James Quach invented a “quantum thermometer” that might very soon prove Unruh, and general relativity, right.

[^ch11n21]: Note, though, that here we are talking about vectors in a single frame— unlike the rotation example above, this summation is not about transformations between frames.

[^ch11n22]: *Proving invariance of the scalar product for coordinate transformations in n-D*: It’s easiest to see this using the differential form of the matrix coefficients in the transformation equations. For example, the first of the 2-D rotation transformation equations is *x′* = *x* cosθ + *y* sin θ. Using partial derivatives, the differential form of this equation is

::: {.displayeq}

$$dx'=\frac{\partial x'}{\partial x}dx+\frac{\partial x'}{\partial y}dy,$$

:::

    and you can see that $\frac{\partial x'}{\partial x}=\cos\theta$, and so on for the other derivatives—so that these derivatives are just the components that I labeled $A_{\sigma}^{\mu'}$ in the narrative. For the scalar (or inner) product of the column and row vector you’d have (using the chain rule to get the last term):

::: {.displayeq}

$$u^{\mu'}v_{\mu'}=A_{\sigma}^{\mu'}A_{\mu'}^{\lambda}u^{\sigma}v_{\lambda}\equiv\frac{\partial x^{\mu'}}{\partial x^{\sigma}}\frac{\partial x^{\lambda}}{\partial x^{\mu'}}u^{\sigma}v_{\lambda}=\frac{\partial x^{\lambda}}{\partial x^{\sigma}}u^{\sigma}v_{\lambda}.$$

:::

    The repeated indices mean the right-hand side is

::: {.displayeq}

$$\frac{\partial x^{\lambda}}{\partial x^{1}}u^{1}v_{\lambda}+\frac{\partial x^{\lambda}}{\partial x^{2}}u^{2}v_{\lambda}+\dots+\frac{\partial x^{\lambda}}{\partial x^{n}}u^{n}v_{\lambda}.$$

:::

    These derivatives are with respect to the *independent* coordinates, so the only derivative that makes sense is $\frac{\partial x^{\lambda}}{\partial x^{\lambda}}=1$. It’s analogous to school calculus, where we usually have just one independent variable, say *x*, and then $\frac{dx}{dx}=1.$. So the only possible value for σ on that right-hand side expression above is λ. Which means we have

<!--p390-->
::: {.displayeq}

*u*^**μ´**^ *v*~μ´~ = *u*^**λ**^*v*~λ~.

:::

    The expression is the same in the transformed coordinate system (with the dashes) as it is in the original coordinates. (It doesn’t matter what letter I use for the repeated indices, because they are just place-holders telling you to sum. So I can swap μ for λ.)

    In other words, the scalar product is invariant under this change of coordinates.

[^ch11n23]: *Invariance of ds^2^*: We saw earlier that the coordinate transformation matrices for contravariant and covariant tensors are inverses, $A_{\sigma}^{\mu'}\to A_{\mu'}^{\sigma}$ (or using derivative notation for the matrix components, $\frac{\partial x^{\mu'}}{\partial x^{\sigma}}\to\frac{\partial x^{\sigma}}{\partial x^{\mu'}}).$ So the inverse pairs will “cancel,” and we’ll have

::: {.displayeq}

$$ds^{2}=g_{\mu'v'}dx^{\mu'}dx^{v'}=A_{\mu'}^{\sigma}A_{v'}^{\lambda}A_{\sigma}^{\mu'}A_{\lambda}^{v'}g_{\sigma\lambda}dx^{\sigma}dx^{\lambda}=g_{\sigma\lambda}dx^{\sigma}dx^{\lambda}.$$

:::

    The distance measure *ds*^**2**^ has the same form and the same value in each frame. (Remember it’s the pattern of the indices that matters, not the choice of letters.)

[^ch11n24]: *Beltrami on Ricci’s tensors*: Goodstein, *Einstein’s Italian Mathematicians*, 49.

[^ch11n25]: Ricci and Levi-Civita, “Méthodes de calcul différential absolu,” 128 (my translation).

## CHAPTER 12

[^ch12n1]: G. Ricci and T. Levi-Civita, “Méthodes de calcul différential absolu et leurs applications,” *Mathematische Annalen* 54 (1900): 125–201.

[^ch12n2]: R. H. Dicke (“The Eötvös Experiment,” *Scientific American* 205, no. 6 (December 1961): 84–95), suggests it’s unclear whether or not Einstein knew about Eötvös’s result during his early thinking about gravity, but that Einstein would certainly have heard if the experiment had shown that Galileo’s law was wrong. For the 2022 test: Pierre Touboul et al., “MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle,” *Physical Review Letters* 129 (2022): 121102.1–121102.8.

[^ch12n3]: Urbain LeVerrier was the first to calculate this discrepancy; with updated measurements his method gave about 43 arc seconds.

[^ch12n4]: Quoted in Abraham Pais, *Subtle Is the Lord* (Oxford: Oxford University Press, 1982), 178. Some translate “happiest” as “most fortunate.”

[^ch12n5]: Because the strength of Earth’s gravity increases the closer the falling observer gets to the centre of the Earth, there are measurable differences between the falling observer and the uniformly accelerating one. Similarly, ocean tides are caused because one side of the earth is closer to the moon and feels its pull more strongly.

<!--p391-->
[^ch12n6]: *Einstein’s appointment at Prague*: Banesh Hoffmann, *Einstein* (Frogmore: Paladin, 1975), 94. In 1882, the University of Prague, known as Charles University, had split into a Czech and a German part in the wake of Czech nationalism and ethnic disputes: https://cuni.cz/UKEN-298.html.

[^ch12n7]: *Potential form of Newtonian gravity, from Newton’s laws* $F=ma=\frac{GmM}{r^{2}}\Rightarrow a=\frac{GM}{r^{2}}$. In Cartesian coordinates, designate the components of the gravitational acceleration *a* by *X, Y, Z*, and note that the vector ***a*** is in the same direction as *r*, the distance between the two masses. Putting one mass, *m*, at the origin, then ***r*** is the position vector of the second mass, *M*, which is at the point (*x, y, z*). The horizontal component of ***a*** is found from $\boldsymbol{a}\cdot\boldsymbol{i}=a\cos\theta=\frac{ax}{r}=\frac{GMx}{r^{3}},$ and similarly for the other components. Differentiating these (using $r=\sqrt{x^{2}+y^{2}+z^{2}}$ and the chain rule), and adding, you get $\frac{\partial V}{\partial x}+\frac{\partial Y}{\partial y}+\frac{\partial Z}{\partial z}=0.$ Since acceleration is proportional to the (conservative) force, we can write its components in terms of a potential $V:X=\frac{\partial V}{\partial x},Y=\frac{\partial V}{\partial y},Z=\frac{\partial V}{\partial z},$ and so the above equation becomes Laplace’s equation, $\frac{\partial^{2}V}{\partial x^{2}}+\frac{\partial^{2}V}{\partial y^{2}}+\frac{\partial^{2}V}{\partial z^{2}}=0.$ If there is a continuous distribution of matter with density ρ, then Poisson’s equation holds instead, and the right-hand side is 4π*G*ρ.

[^ch12n8]: *Charge and mass density caveats*: In electromagnetism there is a need to distinguish between charge density and point charges. In the case of gravity, Newtonian and Einsteinian, the distinction is between an average distribution of matter—across the solar system or in a nebula or galaxy—and a point source like a single star or planet. (Newton proved that spherical bodies act as if all their mass is concentrated at a point, the centre of the body.) What this means is that the equations are singular at a point—that is, they don’t work—but they’re fine outside this point source, where they are called “vacuum equations.” And they’re fine for an average distribution of matter with density ρ. For more, see Peter Gabriel Bergmann, *Introduction to the Theory of Relativity* (New York: Dover, 1976), 175–77.

[^ch12n9]: Einstein to Besso, quoted in Hanoch Gutfreund and Jürgen Renn, *The Road to Relativity: The History and Meaning of Einstein’s “The Foundation of General Relativity”* (Princeton, NJ: Princeton University Press, 2015), 9. *“Serious mistakes”* quoted in Judith Goodstein, *Einstein’s Italian Mathematicians* (Providence, RI: American Mathematical Society, 2018), 102–3.

[^ch12n10]: Quoted in Goodstein, *Einstein’s Italian Mathematicians*, 104. I’m also indebted to Goodstein for my summary of Abraham and Einstein’s relationship.

<!--p392-->
[^ch12n11]: Einstein’s plea was recollected by his fellow ETH student and professor Louis Kollros; quoted in N. Straumann, “Einstein’s ‘Zürich Notebook’ and His Journey to General Relativity,” *Annals of Physics* (Berlin) 523, no. 6 (2011): 488–500, esp. 490.

[^ch12n12]: In his 1916 paper (*The Foundation of the General Theory of Relativity*, 1916, English translation in H. A. Lorentz et al., *The Principle of Relativity* [New York: Dover, 1952], 113), Einstein defined the general principle of relativity this way: “The laws of physics must be of such a nature that they apply to systems of reference in any kind of motion.” In other words, these laws must keep the same form for all observers (all frames of reference), and this means they must be expressed in tensor form.

[^ch12n13]: Albert Einstein, *Ideas and Opinions* (1954; New York: Three Rivers Press, 1982), 309.

[^ch12n14]: *Any coordinate transformations?* There were many confusing aspects that Einstein had to try to sort out. For instance, what about transformations that don’t change the location of points, such as from Cartesian to polar coordinates? Einstein realised the problem, which is why he struggled with the idea of general covariance, as we’ll see. See John D. Norton, “General Covariance and the Foundations of General Relativity: Eight Decades of Dispute,” *Reports on Progress in Physics* 56 (1993): 791–858, esp. 833–34. Further, on a manifold these transformations are found for points, not for the whole space. For an analysis of this subtlety, see Norton, “General Covariance,” 804; and John Earman and Clark Glymour, “Lost in the Tensors: Einstein’s Struggle with Covariance Principles 1912–1916,” *Studies in History and Philosophy of Science* 9 (1978): 4, 251–78, esp. 254.

[^ch12n15]: Einstein, *Ideas and Opinions*, 288.

[^ch12n16]: I used the word “minimising,” but technically I mean “extremising” the integral, for the route is longest on time-like geodesics (because of time dilation as opposed to space contraction); but we don’t need to worry about this here.

[^ch12n17]: *“Caught fire”*: Einstein’s recollection, quoted in Straumann, “Einstein’s ‘Zürich Notebook,’” 490.

[^ch12n18]: *Is F^μν^ a tensor*: yes, because (cf. chap. 11) it transforms like this:

::: {.displayeq}

$$F^{\mu'v'}=A_{\sigma}^{\mu'}A_{\lambda}^{v'}F^{\sigma\lambda},$$

:::

    where in Minkowski space-time the transformation matrices *A* represent the Lorentz transformations (LTs). Under LTs, however, where time and space coordinates are intertwined, vectors whose components are functions of space and time (such as velocity or the electric and magnetic field vectors) don’t transform quite so simply as we saw in chapter 11.

<!--p393-->
[^ch12n19]: Different authors prefer one name or the other, but fairness is restored because in differential geometry there’s a dual tensor, denoted with a star as in the box, so both names get used.

[^ch12n20]: This symmetry is warranted physically by considering an element of the matter and mathematically by considering what happens when you lower the indices: $g_{\mu\nu}T_{\sigma}^{\mu}=T_{v\sigma}$, and $g_{\mu\nu}T_{\sigma}^{\mu}=T_{\sigma v}$. But the left-hand sides of these equations are the same because *g*~μν~ = *g*~νμ~, which means *T*~νσ~ = *T*~σν~.

[^ch12n21]: *Local laws*: Einstein’s mass-energy conservation law is *T* ^μν^~;ν~ = 0, but this is a local conservation law. The notion of global gravitational energy conservation is still especially problematic, but even local concepts such as the energy density of a gravitational field are hard to define physically. That’s because *T* ^μν^~;ν~ = 0 is a mathematical analogy; we’ll see more in the next chapter.

    On Earth, a “local” region must be small enough that there’s no measurable curvature of the surface—otherwise the inverse-square law of gravity shows that gravitation varies from place to place, and Galileo’s constant gravitational acceleration of 32 feet/sec/sec, which I used in fig. 12.1, no longer applies. In the solar system, a “local” region can be large, as long as the gravitational field from the sun and planets is roughly constant. Further afield, “local” can cover a huge area—perhaps half the distance between two stars. (I owe these estimates to Bertrand Russell’s brilliant *The ABC of Relativity*, originally published in 1925, excerpted in *The World Treasury of Physics and Mathematics*, ed. Timothy Ferris [Boston: Little, Brown, 1991], 194–202.)

    For detailed discussion on Einstein’s struggles with energy conservation and covariance, see Straumann, “Einstein’s ‘Zürich Notebook’”; Earman and Glymour, “Lost in the Tensors”; and Galina Weinstein, “Why Did Einstein Reject the November Tensor in 1912–1913, Only to Come Back to It in November 1915?,” *Studies in History and Philosophy of Modern Physics* 62 (2018): 98–122. The “November tensor” is the Ricci tensor.

    For detailed discussion on Einstein’s attempt to explain *Entwurf* ’s lack of general covariance, and its philosophical significance even today, see John D. Norton, “The Hole Argument,” *Stanford Encyclopedia of Philosophy*, online, updated 2019; https://plato.stanford.edu/entries/spacetime-holearg/.

[^ch12n22]: *Grossmann on trouble with tensors*: quoted in Earman and Glymour, “Lost in the Tensors,” 258–59. *Einstein’s “heavy heart”*: quoted in Straumann, “Einstein’s ‘Zürich Notebook,’” 489.

<!--p394-->
[^ch12n23]: *Einstein to Ehrenfest*, document 173, in *Collected Papers of Albert Einstein*, vol. 8, ed. Robert Schulman, A, J. Knox, Michel Janssen, and Jósef Illy; English translation by Ann M. Hentschel (Princeton, NJ: Princeton University Press, 1998); available online thanks to the Press and the Einstein Papers Project, https://einsteinpapers.press.princeton.edu/vol8-trans/195. Einstein to Besso, quoted in Goodstein, *Einstein’s Italian Mathematicians*, 105–6. See also Earman and Glymour, “Lost in the Tensors,” 264ff., for discussion of why Einstein’s colleagues rejected *Entwurf*.

[^ch12n24]: Quoted in Earman and Glymour, “Lost in the Tensors,” 260.

[^ch12n25]: Stern quoted in Hanoch Gutfreund, “Otto Stern—with Einstein in Prague and in Zürich,” Springer Link, June 20, 2021, open access, https://link.springer.com/chapter/10.1007/978-3-030-63963-1_6?error=cookies_not_supported&code=bb7fb68a-a41c-4c71-ace0-33a64d5f7756.

[^ch12n26]: *Mileva’s sad letter*: quoted in Roger Highfield and Paul Carter, *The Private Lives of Albert Einstein* (London: Faber and Faber, 1993), 128. Einstein’s acrimonious demands on Mileva are painfully outlined in letters of July 1914, e.g., document 22, *Collected Papers of Albert Einstein*, vol. 8, https://einstein papers.press.princeton.edu/vol8-trans/60.

[^ch12n27]: *Declaration to the Cultural World*: Constance Reid, *Hilbert* (Berlin: Springer-Verlag, 1970), 137–38.

[^ch12n28]: Einstein to Levi-Civita, document 60, *Collected Papers of Albert Einstein*, vol. 8, https://einsteinpapers.press.princeton.edu/vol8-trans/99.

[^ch12n29]: David E. Rowe, “Einstein Meets Hilbert: At the Crossroads of Physics and Mathematics,” *Physics in Perspective* 3 (2001): 379–424, esp. 393–96.

[^ch12n30]: As we saw in chapter 11, homogeneous coordinate transformations keep equations such as ***a*** ∙ ***b*** = 0 invariant. Similarly Einstein said, in his 1916 overview (*The Foundation of the General Theory of Relativity*, 1916, English translation in H. A. Lorentz et al., *The Principle of Relativity* [New York: Dover, 1952], 121), that “if a law of nature is expressed by equating all the components of a tensor to zero, it is generally covariant.” For discussion, see Norton, “General Covariance,” 833–34. Norton notes (834) that covariance of the metric is more restrictive than the usual transformations of tensor analysis.

<!--p395-->
[^ch12n31]: Einstein’s November 1915 letters to his family are in *Collected Papers of Albert Einstein*, vol. 8 (surrounded by letters to Hilbert!), e.g., documents 142–43, https://einsteinpapers.press.princeton.edu/vol8-trans/174, document 150, https://einsteinpapers.press.princeton.edu/vol8-trans/177. On November 5, 1915, Marić had indicated her own willingness for Einstein to see more of their boys, document 135, https://einsteinpapers.press.princeton.edu/vol8-trans/169. Einstein never managed a good relationship with his younger son, Eduard, who was brilliant but highly sensitive, later developing schizophrenia. Einstein paid for his care, but the emotional burden fell on Marić.

[^ch12n32]: *Einstein to his friend Ehrenfest*, quoted in Banesh Hoffmann, *Einstein* (Frogmore: Paladin, 1975), 125; *Einstein to Hilbert*, November 18, 1915, *Collected Papers of Albert Einstein*, vol. 8, document 148, https://einsteinpapers.press.princeton.edu/vol8-trans/176; *Einstein to Besso*, November 17, 1915, in *Collected Papers of Albert Einstein*, vol. 8, document 147, https://einsteinpapers.press.princeton.edu/vol8-trans/176. Note that Einstein did not yet have his full field equations, but he did have the correct vacuum equations, which is what he needed to calculate the geodesic path of Mercury; the result deviated from a Newtonian ellipse, and this gave him the discrepancy in the motion of the perihelion. For the derivation see general relativity textbooks such as Ray d’Inverno, *Introducing Einstein’s Relativity* (Oxford: Clarendon Press, 1992), 195–98 (including 198 for comparison of observed values of perihelion precession with the values calculated using general relativity).

<!--p396-->
[^ch12n33]: *No explicit equations in November 20 paper*: Leo Corry and his colleagues Jürgen Renn (Max Planck Institute for the History of Science) and John Stachel (Center for Einstein Studies, Boston University) compared the proofs with the published version in “Belated Decision in the Hilbert-Einstein Priority Dispute,” *Science* 278 (1997): 1270–73. More references are listed below. *Hilbert November 20 proofs not generally covariant*: see, e.g., Vladimir P. Vizgin, “On the Discovery of the Gravitational Field Equations by Einstein and Hilbert: New Materials,” *Physics-Uspekhi* 44, no. 12 (2001): 1289; Gutfreund and Renn, *Road to Relativity*, 33; Jürgen Renn and John Stachel, “Hilbert’s Foundation of Physics: From a Theory of Everything to a Constituent of General Relativity,” in *The Genesis of General Relativity*, ed. Jürgen Renn (Dordrecht: Springer, 2007), 4:858–59.

[^ch12n34]: Following Mie, Hilbert used a very different approach from Einstein—an elegant Lagrangian (variational) approach. But Einstein, too, had already tried this approach, in his 1914 paper, which Hilbert had read. Einstein included his variational method for discussing the conservation laws in his 1916 overview paper as well, using a Hamiltonian rather than a Lagrangian. For discussion on the two approaches see Rowe, “Einstein Meets Hilbert,” 414–15.

[^ch12n35]: *Einstein-Hilbert priority, and on the different routes of Einstein and Hilbert*: Tilman Sauer, “Einstein Equations and Hilbert Action: What Is Missing on Page 8 of the Proofs for Hilbert’s First Communication on the Foundations of Physics?,” *Archives for History of Exact Sciences* 59 (2005): 577–90. Vizgin, “On the Discovery of the Gravitational Field Equations,” 1283–98. Leo Corry, Jürgen Renn, and John Stachel, “Belated Decision,” 1270–73. F. Winterberg, “On ‘Belated Decision in the Hilbert-Einstein Priority Dispute,’ Published by L. Corry, J. Renn and J. Stachel,” *Z. Naturforsch* 59a (2004): 715–19. John Earman and Clark Glymour, “Einstein and Hilbert: Two Months in the History of General Relativity,” *Archives for History of Exact Sciences* 19 (1978): 291–308. Renn and Stachel, “Hilbert’s Foundation of Physics,” 4:857–973 (for Einstein’s account of his derivation, see, e.g., his letters to Sommerfeld (document 153) and Ehrenfest (document 185) in *Collected Papers of Albert Einstein*, vol. 8). David E. Rowe, “Einstein Meets Hilbert,” 379–424. Ivan T. Todorov, “Einstein and Hilbert: The Creation of General Relativity,” preprint online at arXiv:physics/0504179v1, April 25, 2005. Galina Weinstein, “Did Einstein ‘Nostrify’ Hilbert’s Final Form of the Field Equations?,” online at *Physics ArXiv:1412.1816*, December 11, 2014. And more! Note that there is much misinformation online about the priority issue. For instance, V. A. Petrov (“Einstein, Hilbert and Equations of Gravitation,” blog online at https://arxiv.org/pdf/gr-qc/0507136.pdf ) claims Einstein couldn’t have derived the correct advance of Mercury’s perihelion when he said he did, because he didn’t yet have the final equations; he implies Einstein must have seen Hilbert’s work (on the trace term), but the perihelion equations need only the vacuum solution where there is no trace; Petrov also implies that Hilbert derived the Bianchi identities, but this obscures the fact that Hilbert did not adequately understand the role these identities play in conservation of energy (as I’ll discuss in the next chapter). Petrov cites Winterberg (above), who cites C. J. Bjerknes (as Petrov does), but Bjerknes is not a credible scholar: see, e.g., John Stachel, “Anti-Einstein Sentiment Surfaces Again,” *Physics World* 16, no. 4 (2003): 40.

[^ch12n36]: Rowe discusses this well in “Einstein Meets Hilbert,” 408; he does note (418) that Hilbert should have changed the submission date on the published paper, although this was standard practice at the time. I should add that today, papers are published with the original submission date *and* revision dates.

[^ch12n37]: Renn and Stachel, “Hilbert’s Foundation of Physics,” shows in detail the ways that Hilbert modified his published paper after reading Einstein’s and notes the ways he’d originally tried to present essential Einstein contributions as his own (see, e.g., 920–21).

<!--p397-->
[^ch12n38]: Hilbert quoted in Reid, *Hilbert*, 142. Einstein’s poignant reconciliation letter is quoted in, e.g., Vizgin, “On the Discovery of the Gravitational Field Equations,” 1289.

[^ch12n39]: We saw earlier that in Minkowski space-time the scalar product (and hence the divergence sum) has a sign change for the *t*-component. But the point here is that these are *definitions*, so just keep your eye on the pattern of the indices in the divergence terms.

[^ch12n40]: This is because it is always possible to find a locally inertial (“free-falling”) frame at a point, one in which special relativity holds (and the Christoffel symbols used in the covariant derivative are zero). By the rules of tensor analysis, the form of a tensor equation will be invariant in any frame—as long as you use (torsion-free) covariant rather than partial derivatives, to take account of the curvature of space-time. This rule also assumes we are replacing the flat Minkowski metric by the general curved metric.

[^ch12n41]: In “nonrelativisitic” units, though, *k* = 8π*G*/*c*^**4**^, where *G* is the proportionality constant in Newton’s law of gravity; this highlights the fact that Einstein derived his equations by analogy with Newton’s and ensured that they reduced to Newton’s in weak gravitational fields such as Earth’s.

[^ch12n42]: These two equations are equivalent because contracting the indices on Einstein’s original equation, and noting that $g_{\mu}^{\mu}=4$ (by definition of *g*~**μν**~ and *g*^**μν**^ as inverses, as we saw in chap. 11), you find that $R_{\mu}^{\mu}=-kT_{\mu}^{\mu}\equiv R=-kT.$ (Note that in his original equation Einstein actually had −*k* as his coefficient, but since this is a constant, I’ve absorbed the minus sign into my definition of *k*, to fit with the way the equation is usually written today. Also, in his final equation Einstein wrote the left-hand side [Ricci tensor] out in full, in terms of Christoffel symbols, but he’d already defined this expression as *R*μν.)

[^ch12n43]: The difference between Einstein’s earlier equation, *R*μν = *kT*μν, and these two final forms hinges on the scalar *T* or Hilbert’s equivalent scalar *R*. (These scalars are called “traces.”) Whether Einstein or Hilbert realised this first is at the heart of the “priority dispute,” because it is only implicit in Hilbert’s November 20 Lagrangian formulation. Since Einstein and Hilbert exchanged papers, they certainly influenced each other, but it is likely they each took this final step independently, for they followed different routes. Today, Hilbert’s approach is widely used, and he is commemorated in the so-called Einstein-Hilbert action associated with the Lagrangian.

<!--p398-->
[^ch12n44]: *Recent tests of Einstein’s theory*: See, e.g., Pierre Touboul et al., “MICROSCOPE Mission: Final Results of the Test of the Equivalence Principle,” *Physical Review Letters* 129, no. 21102 (September 14, 2022); Ignazio Ciufolini et al., “An Improved Test of the General Relativistic Effect of Frame-Dragging Using the LARES and LAGEOS Satellites,” *European Physical Journal C* 79, article no. 872 (2019); Gemma Conroy, “Albert Einstein Was Right (Again): Astronomers Have Detected Light from Behind a Supermassive Black Hole,” ABC News, July 29, 2021, https://www.abc.net.au/news/science/2021-07-29/albert-einstein-astronomers-detect-light-behind-black-hole/100333436; Geraint Lewis, “Astronomers See Ancient Galaxies Flickering in Slow Motion Due to Expanding Space” (a test of Einstein’s predictions about time slowing down), *The Conversation*, July 4, 2023; Jet Propulsion Laboratory blog (August 24, 2022), “NASA Scientists Help Probe Dark Energy by Testing Gravity”—they found that Einstein’s equations hold firm. (Pavel Kroupa, University of Bonn, disagrees, in “Dark Matter Doesn’t Exist,” *IAE News*, July 12, 2022. But a new study used general relativity’s prediction of gravitational lensing to map dark matter: Robert Lea, “New Dark Matter Map Created with ‘Cosmic Fossil’ Shows Einstein Was Right (Again),” *Space* [April 18, 2023].) *On precession of black holes*: Brandon Specktor, “One of the Most Extreme Black Hole Collisions in the Universe Just Proved Einstein Right,” *LiveScience*, October 13, 2022. *On frame dragging*: See, e.g., Charles Q. Choi, “Spacetime Is Swirling around a Dead Star, Proving Einstein Right Again,” *Space.com*, January 31, 2020. And much more!

    For a popular overview of the eclipse expeditions (and light bending around a black hole), see my article “A ‘Revolution in Science’ 100 Years Later,” *Cosmos Magazine* 83 (2019): 29–35. Note it was Johann Soldner who had earlier used Newton’s theory to predict light bending, getting half the general relativity result. Also note that accusations of bias against the leaders of the expedition arose in 1980, but they have been overturned and the 1919 results confirmed.

    For a brief overview of gravitomagnetism, see my piece “The Amazing Concept of Gravito-electromagnetism,” *Cosmos Magazine* 84 (September 2019): 61–63. An abridged version is at https://cosmosmagazine.com/science/introducing-the-amazing-concept-of-gravito-electromagnetism/.

    My own research has been on the second analogy mentioned in the main article. See, e.g., C. B. G. McIntosh, R. Arianrhod, S. T. Wade, and C. Hoenselaers, “Electric and Magnetic Weyl Tensors: Classification and Analysis,” *Classical and Quantum Gravity* 11 (1994): 1555–64; and R. Arianrhod, A. W-C. Lun, C. B. G. McIntosh, and Z. Perjés, “Magnetic Curvatures,” *Classical and Quantum Gravity* 11 (1994): 2331–35. Einstein’s gravitational constant is added to the equations for some applications, especially dark energy.

<!--p399-->
[^ch12n45]: Einstein, *Ideas and Opinions*, 289–90.

[^ch12n46]: Einstein’s cover page was missing from English translations but was recently tracked down by Alicia Dickenstein, who gives Einstein’s full acknowledgment in “About the Cover: A Hidden Praise of Mathematics,” *Bulletin of the American Mathematical Society*, n.s., 46, no. 1 ( January 2009): 125–29.

[^ch12n47]: Levi-Civita quoted in Goodstein, *Einstein’s Italian Mathematicians*, 151, 155.

## CHAPTER 13

[^ch13n1]: *Klein and Hilbert on Miss Noether*: quoted in Yvette Kosmann-Schwarzbach, translated by Bertram E. Schwarzbach, *The Noether Theorems: Invariance and Conservation Laws in the Twentieth Century* (New York: Springer, 2011), 45, 66.

[^ch13n2]: In his 1993 paper “General Covariance and the Foundations of General Relativity,” John Norton gave a fascinating account not just of Einstein’s struggles but also of the way others responded to or reinterpreted the meaning of his principles of covariance, relativity, and equivalence. He illustrates this with the way textbook accounts evolved over the twentieth century and points out that there is still controversy or confusion. Of course, as I showed at the end of the previous chapter, physical observations so far have confirmed that the equations work brilliantly, no matter their foundations!

[^ch13n3]: An English translation of Noether’s paper is given in Kosmann-Schwarzbach, *Noether Theorems*, 3–22.

[^ch13n4]: In a weak gravitational field like that on Earth, it turns out that the time component of the “momentum” is, indeed, the sum of the particle’s rest mass, gravitational potential energy, and kinetic energy. See, e.g., Bernard Schutz, *A First Course in General Relativity* (Cambridge: Cambridge University Press, 1985), 190.

<!--p400-->
[^ch13n5]: To see the essence of Noether’s result, which she fully generalised in her 1918 theorems, let’s go back to those translations we talked about. Taking all values of *a*, these translations from *x* to *x* + *a* form a group (like the Lorentz transformations in fig. 9.3). Groups relating to invariance are called “symmetry groups.” The “symmetry” here is the invariance expressed by the fact that *V* is independent of *x*. If the same symmetry applies in each direction, then all the components of ***p*** are conserved and we have the familiar law of conservation of momentum. What Noether showed was that the symmetry groups for classical mechanics *and* for special relativity are finite, but the symmetry group in general relativity is infinite, because general relativity allows all possible coordinates and therefore all possible point transformations. This meant that the conservation law for the energy-momentum of the gravitational field is indeed different from the usual conservation laws in mechanics and special relativity. For technical details, see Kosmann-Schwarzbach, *Noether Theorems*, 56–64.

[^ch13n6]: *On physical laws as divergence*: Peter Gabriel Bergmann, *Introduction to the Theory of Relativity* (New York: Dover, 1976), 194–97. *On divergence in Noether’s theorems*: Kosmann-Schwarzbach, *Noether Theorems*, e.g., 6–10.

[^ch13n7]: *On defining energy in general relativity*: Robert M. Wald, *General Relativity* (Chicago: University of Chicago Press, 1984), 84, 286, and for Noether’s theorem, 457; S. W. Hawking and G. F. R. Ellis, *The Large-Scale Structure of Space-time* (1973; Cambridge: Cambridge University Press, 1991), 61–62, 73–74, 88–96. *On Noether’s theorems*: Kosmann-Schwarzbach, *Noether Theorems*; for a simpler overview, see David E. Rowe, “On Emmy Noether’s Role in the Relativity Revolution,” *Mathematical Intelligencer* 41, no. 2 (2019): 65–72.

[^ch13n8]: Einstein had insisted that any coordinates should be allowed for a truly general theory of relativity—his principle of covariance—but we saw that this allows for coordinates that represent the same point. This means that we can get different forms of the metric that actually represent the same spacetime—just as we saw for the equation of the circle in terms of Cartesian and polar coordinates. To mitigate this situation, the four energy-conservation equations (or the contracted Bianchi identities we’ll meet in the next section) impose additional constraints on the choice of coordinates (see note 10).

[^ch13n9]: In chapter 12, *T***μν** and *T*μν had the same content because the indices were raised with the Minkowski metric. In general relativity, tensors pick up terms from the metric when the indices are raised, but because this happens on both sides of a tensor equation, the essential content of the equation is the same.

[^ch13n10]: These four contracted Bianchi identities give additional information about the Ricci tensor, which means that of the ten Einstein equations, only six are independent. This allows the freedom to choose the four coordinates (the frame) arbitrarily, ensuring that every observer deduces the same laws of physics.

<!--p401-->
[^ch13n11]: T. Levi-Civita (1917), translated by S. Antoci and A. Loinger, “On the Analystic Expression That Must Be Given to the Gravitational Tensor in Einstein’s Theory,” https://arxiv.org/pdf/physics/9906004.pdf. *On Hilbert’s convoluted derivation via a variational approach*, see p. 59 of David E. Rowe, “Einstein’s Gravitational Field Equations and the Bianchi Identities,” *Mathematical Intelligencer* 24, no. 4 (2002): 57–66; Ivan T. Todorov, “Einstein and Hilbert: The Creation of General Relativity,” arXiv:physics/0504179v1; David E. Rowe, “Emmy Noether on Energy Conservation in General Relativity,” December 4, 2019, preprint online at https://arxiv.org/pdf/1912.03269.pdf, 21n32; Carlo Cattani and Michelangelo De Maria, “Conservation Laws and Gravitational Waves,” in *The Attraction of Gravitation: New Studies in the History of General Relativity*, ed. John Earman, Michel Janssen, and John D. Norton (Boston: Birkhäuser, 1993), 67.

[^ch13n12]: It would mean that the scalars *R* and *T* would be constant all throughout the universe. These scalars reflect curvature and mass-energy, so *T* should be different in a vacuum than amongst matter.

[^ch13n13]: *Bianchi identities*: David E. Rowe, “Einstein’s Gravitational Field Equations and the Bianchi Identities,” *Mathematical Intelligencer* 24, no. 4 (2002): 57– 66; *Struik and Schouten*: Rowe, “Einstein’s Gravitational Field Equations,” 66; Kosmann-Schwarzbach, *Noether Theorems*, 43.

[^ch13n14]: *On Struik*: Here and in the following paragraphs I’m indebted to David E. Rowe, “Interview with Dirk Jan Struik,” *Mathematical Intelligencer* 11, no. 1 (1989): 14–26. The interview also discusses how Struik’s Marxist ideas led to his suffering under McCarthyism. Struik was evidently remarkable, and, equally remarkably, he lived to be 106 years old (he died in 2000).

[^ch13n15]: Struik quoted in Rowe, “Interview with Struik,” 19. Einstein quotes in Constance Reid, *Hilbert* (Berlin: Springer-Verlag, 1970), 142.

[^ch13n16]: Quoted in Reid, *Hilbert*, 143.

[^ch13n17]: *Einstein in support of Noether*: quoted in Kosmann-Schwarzbach, *Noether Theorems*, 72. *Weimar*: Rowe, “Noether’s Role in Relativity,” 66.

[^ch13n18]: *Mother of modern algebra*: Norbert Schappacher and Cordula Tollmien, “Emmy Noether, Hermann Weyl, and the Göttingen Academy: A Marginal Note,” *Historia Mathematica* 43 (2016): 194–97.

[^ch13n19]: Struik quoted in Rowe, “Interview with Struik,” 16.

[^ch13n20]: *Struik*: Rowe, “Interview with Struik,” 17. *Hodge*: quoted in Judith Goodstein, *Einstein’s Italian Mathematicians* (Providence, RI: American Mathematical Society, 2018), 165.

<!--p402-->
[^ch13n21]: *1928 congress and Hilbert’s stirring speech*: Reid, *Hilbert*, 188.

[^ch13n22]: See, e.g., the Australian Mathematical Society’s *Gazette* 49, nos. 1 (Ole Warnaar’s President’s column) and 2 (Letters, from Aerwm Pulemotov).

[^ch13n23]: Einstein and Cartan quotes are from the letters of December 8, 1929, and February 17, 1930, respectively, in *Elie Cartan–Albert Einstein: Letters on Absolute Parallelism 1929–1930*, ed. Robert Debever (Princeton, NJ: Princeton University Press, 1979).

[^ch13n24]: *Einstein to Cartan*: in *Elie Cartan-Albert Einstein*, ed. Debever, 203; *Einstein to Mrs. Grossmann*: in Banesh Hoffmann, *Einstein* (Frogmore: Paladin, 1975, 36.

## EPILOGUE

[^ch14n1]: Particle colliders enabled physicists to build the Standard Model describing matter and its interaction with the various forces, and CERN points out that there have also been social benefits as well as scientific ones: https://home.cern/news/news/cern/society-benefits-investing-particle-physics. Former particle physicist Sabine Hossenfelder, however, is one who is skeptical about the scientific benefits; see, e.g., her blog post at https://backreaction.blogspot.com/2022/04/did-w-boson-just-break-standard-model.html. Similarly, this post on *Quora* suggests negative results in the LHC are vital for science, but in the sense of ruling out popular theories: https://www.quora.com/Was-building-the-Large-Hadron-Collider-worth-it-Did-they-discover-anything-from-it. Also see, e.g., Nick Scott, “CERN’s Grand Ambitions: Are Particle Accelerators Worth It?” *Varsity* ( January 26, 2021), https://www.varsity.co.uk/science/20486; Tom Hartsfield, “Please, Don’t Build Another Large Hadron Collider,” *Big Think* ( June 6, 2022), https://bigthink.com/hard-science/large-hadron-collider-economics/.

[^ch14n2]: In effect, Dirac used the *square* of *E* = *mc*^**2**^, which yielded positive and negative solutions: the positive one is Einstein’s equation for ordinary matter; the negative one, *E* = −*mc*^**2**^, refers to antimatter. For a brief introduction, see the excerpt from Dirac’s 1933 Nobel Prize address in *The World Treasury of Physics, Astronomy and Mathematics*, ed. Timothy Ferris (Boston: Little, Brown, 1993), 80–85. For a modern analysis, see Luciano Maiani and Omar Benhar, *Relativistic Quantum Mechanics* (Boca Raton, FL: CRC Press, 2016), 113–16.

[^ch14n3]: See Bertha Swirles, “The Relativistic Interaction of Two Electrons in the Self-Consistent Field Method,” *Proceedings of the Royal Society A* 157, no. 892 (December 2, 1936): 680–96.

<!--p403-->
[^ch14n4]: *Tensors in computational maths, esp. NLA*: See, e.g., Lek-Heng Lim, “Tensors in Computation,” *Acta Numerica* (2021): 555–764, DOI:10.1017/S09622 492921000076.

[^ch14n5]: Einstein to Heinrich Zangger, document 152, *Collected Papers of Albert Einstein*, https://einsteinpapers.press.princeton.edu/vol8-trans/179. This letter also shows Einstein’s bitterness at his ex-wife for apparently holding up his reconciliation with his son Hans Albert.

<!--stats: p=0 fig=1 eq=42 note=353-->
