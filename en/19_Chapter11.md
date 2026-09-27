<!--p240-->
# (11) INVENTING TENSORS—AND WHY THEY MATTER

In 1861, when Gregorio Ricci was eight years old, a long series of political and military machinations culminated in the proclamation of the Kingdom of Italy. This meant that most of the disparate Italian states, duchies, and kingdoms were formally, if not always willingly, united at last. But it was religion that dominated Ricci’s childhood. His father—an aristocratic landowner, businessman, and engineer—was a devout Roman Catholic, who expressed his faith not just through hefty donations to the church but also by feeding the hungry. And his mother would take her four children with her as she walked the streets seeking out the poor—especially the women. She seemed to act as a counselor, hearing the women’s troubles and offering comfort. Young Ricci grumbled at all the periodic stopping and waiting while his mother listened to each tale of woe, yet her dignity in the situation left a lasting impression on him, and he, too, was a lifelong and devout Catholic.[^ch11n1]

<!--p241-->
Incidentally, Ricci’s family name was Ricci Curbastro, but in his landmark paper on tensor calculus he signed himself Ricci, so that’s the name he’s known by today. (I should mention that similarly, James Clerk Maxwell’s family name was Clerk Maxwell, but his friends referred to him as Maxwell.) Young Ricci was a keen student, with an unusually “penetrating mind” and a “lively ingenuity,” as one of his teachers put it.[^ch11n2] Then in 1869 he began to study mathematics at the papal university in Rome—but in the summer of 1870, he had to return home because of yet another war. The French had been allied with the papal troops, and when the Prussians prevailed, the new king of Italy seized the chance to take over Rome and bring it into the new Italian kingdom.

With Rome now the secular capital of the new nation, and the former papal university building taken over by the state, Ricci set his sights on the venerable University of Bologna, which was much closer to his hometown of Lugo di Romagno in northeast Italy. He had to do some extra study to qualify for admission—two years’ worth, so all that political upheaval cost him dearly. Still, he was a supporter of the unification, and being at Bologna also meant, he told a friend, “I can follow more attentively and with more zeal the political reforms that our countrymen who have created a united Italy are going to carry out [in Lugo].”[^ch11n3]

After a stellar year at Bologna—he scored full marks for his exams in calculus, chemistry, and geometry—he decided to move once again, this time to Pisa for its vibrant mathematical school. He got his doctorate in 1875, and his teaching certificate the following year—not that he could get a job at the time, for university positions were scarce. So, he stayed on at Pisa as an independent scholar, reading up on the latest maths and physics. Like Einstein, he was particularly excited when he discovered Maxwell’s theory of electromagnetism—and in 1877, this really was cutting-edge research you couldn’t learn in school. Maxwell himself was still alive, and there was still a decade to go before Heinrich Hertz generated the radio waves that so spectacularly confirmed the theory.

<!--p242-->
After a couple of unsuccessful applications for teaching positions, Ricci obtained a fellowship from the ministry of public instruction—which is how he came to study under the famous Felix Klein. Klein, who was then based in Munich, was already celebrated for finding the relationship between invariant theory and groups of coordinate transformations—and three decades later, Henri Poincaré and Einstein would show that the Lorentz transformations form a group. They’re the coordinate changes under which the Minkowski metric and Maxwell’s equations remain invariant, as we saw earlier—and I briefly explained why they form a group in the boxed caption to figure 9.3. Klein also developed Arthur Cayley’s work on projections of curved surfaces, and all in all he had such wide-ranging mathematical interests that when Ricci arrived in Munich in the autumn of 1878, he was overwhelmed by the study and research program Klein offered him. Still, he found Klein to be a “kind” advisor who gave him “vigorous help” in his studies.[^ch11n4]

Even more important, working with Klein helped Ricci develop confidence in his own ability—a wonderful gift from a teacher to a student. When Chisholm did her PhD with Klein in the 1890s, she, too, would be struck not just by his brilliant mind, but also by the way he would encourage his students to have the confidence to “never be dull!” (Not long after she took her doctorate in 1895—the first official doctorate awarded to a woman in Germany—she married her former Girton tutor William Young, so she is better known today as Grace Chisholm Young. Her doctoral thesis was on algebraic groups, Klein’s specialty, applied to spherical geometry.)[^ch11n5]

After his year with Klein, Ricci spent a couple more years fruitlessly seeking a full-time university position—until finally, in the winter of 1880, he was appointed associate professor of mathematical physics at the University of Padua. Galileo, Copernicus, and Cardano were just three of his illustrious predecessors at this ancient and progressive institution, and Ricci would remain there for the next forty-five years.

<!--p243-->
His first published papers as a Padua academic were on electromagnetism and differential equations, but he soon became intrigued by the maths of invariance. He also decided it was time to find a wife. He’d first fallen in love when he was a student at Pisa, but the girl had disdained his awkward infatuation. Then his older brother’s “unsuitable” love interest had aroused fury from his conservative Catholic parents—she came from a poor and unconventional family, but what really upset Ricci senior was that she was a relative, and he was sure God would not approve of such an incestuous union. So, thirty-year-old Ricci decided the best way to avoid both heartache and parental displeasure was to seek matchmaking advice from the local priest. The priest was happy to oblige, and he arranged for Ricci to meet a lively, intelligent, and eminently suitable young woman named Bianca. It was a happy courtship, and she became his bride and lifelong companion.[^ch11n6]

Ricci had been doing more than courting, though. In the same year as his wedding, 1884, he published his first paper on the road to tensor analysis. He’d been inspired by the works of Riemann and Gauss, and his paper was on the transformation properties of “quadratic differential forms”— that is, sums of the squares or other products of pairs of differentials, such as we’ve seen in the distance metrics based on Pythagoras’s theorem. We saw some of these properties with Gauss’s metric, which is invariant under bending transformations—like the rolled-up piece of paper that shows the surface of a cylinder is just as intrinsically flat as the unrolled paper—and with the Lorentz-invariance of Minkowski’s metric. After the 1876 publication of Riemann’s 1861 essay on heat, which extended Gauss’s work to *n*-dimensions, several mathematicians had taken up his ideas. But Ricci’s aim was to “avoid lazy discussions about the existence and nature of spaces of more than three dimensions,” and to look beyond his colleagues’ focus on *applications* of differential forms. Rather, he wanted to provide a clear understanding of the mathematical *theory*.[^ch11n7]

<!--p244-->
We saw this emphasis on theory with Hamilton’s development of the rules of vector algebra and vector calculus, forty years earlier. He’d begun with the rules for multiplying his *i, j, k*, which he’d triumphantly carved on Broome Bridge, and they enabled him to define new kinds of multiplication—quaternion, scalar, and vector products. Once he had these in hand, he’d created the differential calculus vector operator nabla, ∇. It was only after Maxwell had learned all these rules from Tait—and had given names to the nabla operations grad, divergence, and curl—that he’d felt comfortable using vector calculus in his theory of electromagnetism. So now, establishing similar rules for tensors is just what Ricci set out to do.

Not that he called them tensors: rather, he simply referred to them as “systems of functions.” For example, the coefficients β~ι,ι′~ in Riemann’s “line element” (or metric) Σβ~ι,ι′~*ds*~ι~*ds*~ι′~ are now called the components of a tensor, and, as we saw in chapter 10, on curved surfaces they are functions of the coordinates—so, in fact, they’re a set (or “system”!) of functions. (So technically they are “tensor fields,” but as I mentioned in the previous chapter, less rigorously “tensors” will do nicely.) We’ll see mathematically why the metric is a tensor later—and Riemann’s four-index quantity, too, which Ricci called “the system of Riemann,” so it’s now called the Riemann tensor. And instead of saying “tensor calculus,” Ricci named the calculus of his systems the “absolute differential calculus.” By “absolute” he meant unchanging, because the interesting thing about tensors is that they encode the idea of invariance.

Before I get into Ricci’s maths, though, I’ll sketch out the basic idea of tensors as a way of representing, and calculating with, information—just like vectors. But first I’ll tell you how tensors got their modern name.

## HOW TENSORS GOT THEIR NAME— AND HOW THEY REPRESENT DATA

The term “tensor” comes to us from Hamilton via Göttingen maths professor Woldemar Voigt. But it is Einstein who would firmly establish this name, once he and Marcel Grossmann got their heads around Ricci’s absolute calculus. Hamilton had used the term in a different context—as the magnitude of a quaternion, which he defined by analogy with the modulus of a complex number. It’s the square root of the sum of the squares of the components of the quaternion—just as the magnitude of a vector is found from the sum of the squares of *its* components. But Voigt is the one who first used the term “tensor” in its modern context, in his 1898 book on crystallography—which, incidentally, Chisholm Young and her husband favourably reviewed in *Nature*.[^ch11n8]

<!--p245-->
Voigt was referring specifically to the stresses and tensions in crystals—and “tension” comes from the Latin “tensio,” which in turn comes from “tendere,” meaning “to stretch.” But Voigt said he was simply extending Hamilton’s use of “tensor.” For example, the vector or cross product, ***a*** × ***b***, produces a third vector ***c*** whose magnitude (or Hamiltonian “tensor”) is related to the magnitudes (“tensors”) of ***a*** and ***b***. In other words, the cross product gives a new magnitude (“tensor”) from two others—and as we’re about to see, one of the novel things about Ricci’s tensor analysis is that tensor multiplication produces new, “higher-order” tensors from old ones.

Grassmann had had this idea, too. As we saw in chapter 5, instead of the term “vector,” he’d used the German word *strecke*, which can be translated as “line or stretch”—and his basic geometric objects were “lines” that could be “stretched” or “extended” to form planes, just as two vectors form a plane in the parallelogram rule. Grassmann defined the outer product of two 3-D vectors as the *oriented area* of the parallelogram bounded by the two vectors. The usual vector or cross product does this, too, in effect, but only for parallelograms, whereas Grassmann’s definition of an outer product implied that you could then add a third vector to extend the parallelogram to a box, and so on, adding as many new dimensions as you like.

In the 1880s, Gibbs developed Grassmann’s idea further, essentially hitting on a similar definition of tensor multiplication as Ricci was creating around the same time. Today it is called a “tensor product” or, following Grassmann, an “outer product,” although Gibbs and Ricci didn’t use those names. It is a way of combining information from two tensors into one— a kind of multiplicative version of Roman numerals, where you add more symbols to increase the magnitude of a number: I, II, III, V, VI, VII, VIII, and so on. This analogy also illustrates the fact that outer products are generally not commutative: VI is a different number from IV.

<!--p246-->
You can see the idea of tensor (or outer) products in figure 11.1— which also highlights the fact that vectors and matrices can be thought of as tensors. There’s a sophisticated mathematical reason for this, but for now it’s enough to notice that like tensors, their components are represented with indices—one index for vectors, two for matrices, as the caption to figure 11.1 spells out. Of course, as I intimated in chapter 9, the mark of a tensor goes beyond the fact that its components are denoted with indices— but let’s go with this for now. For the tensor product is a way of producing new tensors, with even more indices, each index telling you something specific about the data represented by the tensor component.

![FIGURE 11.1. Tensor (or outer) products combine information from the tensors being multiplied. Ordinary numbers are represented by a symbol such as *a*. If they represent quantities that don’t depend on coordinates—such as temperature—then they are scalars, and since scalars don’t change under coordinate changes, they are tensors. We’ll see that vectors are tensors, too, and we’ve already seen that their components are denoted with an index to represent the axis from which the component is measured. The tensor product of a column vector ***u*** and a row vector ***v*** can be represented as a matrix. You’re likely familiar with the symbol *a~ij~* for the element in the *i*th row and *j*th column of a matrix, so here *a~ij~* = *u~i~v~j~*. I’ll spell this out in the 2-D example in the narrative. In the same way, you can build up more tensor products. For example, the tensor product of the 1-index vector ***u*** and a matrix *A* has components with 3 indices, as you can also see in the narrative. Similarly, if two matrices *A* and *B* were each formed from the outer product of vectors, the components of their tensor product would be *c~ijkl~* ≡ *u~i~v~j~w~k~s~l~*, and so on. This is not the only way to build new tensors, but notice that you can represent more information as the tensor “rank” increases. The “rank” is also called the “order” of the tensor, for this is what Ricci called it when he introduced the idea. It has to do with the number of transformation matrices needed to transform from one coordinate system to another, but it essentially corresponds to the number of indices, each one representing a different type of information. (If you’re familiar with matrix algebra, note that for matrices viewed as tensors, this is a different use of “rank” from that in linear algebra.) We’ll see more about this as we go.](images/fig11_1.jpg){width="80%"}

<!--p247-->
## TENSORS AND DATA SCIENCE (AND A PEEK AT QUANTUM MECHANICS)

Figure 11.1 also illustrates how tensors enable data to be stored and combined in data science today. In chapter 4, I outlined how vectors and matrices are used in machine learning and search engines, but with tensors you can add in not just *more* data but different *kinds* of data. For instance, we saw that in a search engine, information can be stored as a matrix, with rows representing key words, and columns representing different documents containing these key words. Tensors allow you not just to add more words or more documents—you can do that by making the matrix larger—but *additional* information that you can’t fit into the matrix. For example, if you want to add the date of publication of the document, and the author, you have to extend your original matrix to the 4-D shape shown in figure 11.1. The key thing is that each type of information has its own index.

Another modern application of tensors is signal processing, which is used in interpreting an electroencephalogram (EEG) or electrocardiogram (ECG), for example. In addition to the spatial components of the signal, you might want to know such things as its temporal and frequency components—and again, each type of information requires its own index.

<!--p248-->
So, there’s a difference between the number of components and the number of indices. In ordinary vector analysis we’ve seen that in *n*-dimensional space (or more properly, in an *n*-dimensional “vector space”— an *n*-D space with group properties), a vector has *n* components, each measured from one of the *n* coordinate axes. The particular axis gives the particular label on the component—so a vector has components *v*~1~ ≡ *v~x~*, say, and so on up to *v~n~*. In other words, you have *n* components, but each has only one index—and this one index takes one of *n* values, one for each dimension. We’ve also seen that each component (or element) of a matrix has two indices: one locating the row and the other locating the column. You need both locations to pinpoint the position of a particular element, so you need two indices. Similarly, we saw in figure 9.5 that the component of a stress tensor needs two indices, one to indicate the surface on which the stress is acting, and the other to indicate the force; in three-dimensional space, *each* index takes values from 1 to 3 (or from *x* to *z*), so that’s 3 × 3 = 9 components, as we saw in figure 9.4.

And so it goes for higher-order tensors. For example, I referred in the previous chapter to the Riemann tensor, which has four indices. It’s tempting at first glance to think that it needs four indices because it represents the curvature of 4-dimensional space-time—but the fact that we’re working in four dimensions just means that each index on the Riemann tensor can take four values, one for each dimension. The indices themselves each represent a different attribute or building block of the Riemann tensor.[^ch11n9] So, while the stress tensor in ordinary space has 3 × 3 = 9 components, a 4-index tensor in space-time will have 4 × 4 × 4 × 4 = 256 components: four coordinate choices for each of the four indices. That’s a lot of information you can fit into one tensor! And you can go on to tensors with as many dimensions and orders as you like. (But if a tensor has “symmetries,” as the Riemann tensor does—such as when interchanging or “reflecting” two indices doesn’t change the value of the component—some of its components are the same, so the possible amount of data it can represent is reduced.)

To take another digital tensor application, in image processing the location of each pixel is represented in a matrix whose rows and columns represent the dimensions of the picture—but to produce colour images *three layers* of matrices are needed, one for each of the colours red, green, and blue. (These three colours are a legacy of Maxwell’s discovery of colour slide photography: he and his assistant Thomas Sutton used red, green, and blue filters to take the first-ever permanent colour photograph, the tartan ribbon I mentioned in chap. 6.[^ch11n10]) So, the third index in the tensor encoding the relevant pixel information represents the colour. Similarly, and taking a different example, medical diagnoses are more accurate if they combine data from a variety of different types of test, each represented by an index. These kinds of multi-index constructions—these tensors, and their products—are so important in data science that Google named one of its machine-learning platforms TensorFlow, and there are various other programs and tools, such as Tensorlab and Tensorly.

<!--p249-->
Since tensor products are so important, I’ll spell out the idea of producing a matrix from the tensor product of a column vector ***u*** and a row vector ***v***, as in figure 11.1. For simplicity, I’ll make the vectors 2-D here:

::: {.displayeq}

$$\left(\begin{matrix} u_{1} \\ u_{2} \end{matrix}\right)\left(v_{1}v_{2}\right)=\left(\begin{matrix} u_{1}v_{1} & u_{1}v_{2} \\ u_{2}v_{1} & u_{2}v_{2} \end{matrix}\right).$$

:::

This is a neat way of combining the information from two vectors, and it also follows the rules of ordinary matrix multiplication in this case. But you can see the difference between matrix multiplication and tensor products when you try to multiply ***u*** by a 2 × 2 matrix: the ordinary matrix rules don’t allow you to multiply a 2 × 1 matrix by a 2 × 2 one at all, but the tensor product does:

::: {.displayeq}

$$\left(\begin{matrix} u_{1} \\ u_{2} \end{matrix}\right)\left(\begin{matrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{matrix}\right)=\left(\begin{matrix} u_{1}\left(\begin{matrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{matrix}\right) \\ u_{2}\left(\begin{matrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{matrix}\right) \end{matrix}\right)=\left(\begin{matrix} u_{1}a_{11} & u_{1}a_{12} \\ u_{1}a_{21} & u_{1}a_{22} \\ u_{2}a_{11} & u_{2}a_{12} \\ u_{2}a_{21} & u_{2}a_{22} \end{matrix}\right)$$.

:::

<!--p250-->
So, the tensor product is a way of combining information from two (or more) systems or sets into a single large one. For instance, consider the natural language processing (NLP) programs behind such marvels as email spam filters, language translators, converting spoken words to text (for use by those with hearing problems, for example, such as in captioning TV programs), the helpful voice on your GPS, the polite text from a company’s chatbot, the predictive text used in web searches, say, and apps such as email and Instagram, and the spectacularly human-like text generated by bots such as OpenAI’s ChatGPT. Tensor products can offer a way to combine a set of words with a set of grammatical instructions—where words are represented as vectors by assigning them a position within a dictionary of words, and similarly for the grammar. I should add here that much of the training data used to develop sophisticated NLP (especially large language models or LLMs) is human-generated content scraped from the web without the content creators’ knowledge or permission, and I’m heartened that writers and artists are attempting to fight back against this theft.[^ch11n11] But since tensors themselves are not the problem, and since there are benefits as well as problems[^ch11n12] with NLP and LLM programs and applications, I’ll venture on with this brilliant application of tensor products.

To keep it simple, suppose the word dictionary contains the three words, “cats, love, mice,” and each word is assigned a position number from 1 to 3. The dimension of the vector representations of these words will therefore be three, so if “cats” is in the first position, “love” is in the second, and “mice” is in the third, then these words would be represented as the vectors (1,0,0), (0,1,0), (0,0,1), which I’ll label ***C, L, M***, respectively. To create the sentence “Cats love mice,” just add the vectors: ***C*** + ***L*** + ***M*** = (1,1,1). But this is no different from the vector representation of “Mice love cats,” which is definitely not the case. So it’s here that tensor products can come to the rescue. Take a second set of vectors, representing key grammatical instructions for the roles these words will play: subject, object, verb, labeled as, say, ***S, O, V***, and represented as (1,0,0), (0,1,0), and (0,0,1), respectively. The tensor product of “cats” (represented as a column vector) and “subject” (a row vector) would be represented as we saw just before for column and row vectors:

::: {.displayeq}

$$\left(\begin{matrix} 1 \\ 0 \\ 0 \end{matrix}\right)\left(\begin{matrix} 1 & 0 & 0 \end{matrix}\right)=\left(\begin{matrix} 1 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{matrix}\right),$$

:::

and similarly for the tensor products of “mice” and “object,” and “like” and “verb.” Now you can construct an unambiguous sentence,

::: {.displayeq}

$$C\otimes S+L\otimes V+M\otimes O=\left(\begin{matrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 1 & 0 \end{matrix}\right),$$

:::

where ⊗ is the symbol for tensor products. This is different from “Mice love cats”:

::: {.displayeq}

$$M\otimes S+L\otimes V+C\otimes O=\left(\begin{matrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 1 & 0 & 0 \end{matrix}\right).$$

:::

<!--p251-->
Although this sentence is false, it *is* unambiguous.

This example is just one way of applying tensor products in NLP.[^ch11n13] And one way of applying them in quantum mechanics is in representing the “quantum state” of several particles.

We saw in the prologue that the spin of an electron can be “up,” represented by the vector (1, 0), or “down,” represented by (0, 1); so a “superposition” of these two possibilities—an in-between state in which either outcome is possible—is (α, β), where α is the “weight” or probability amplitude of being in the “up” state and β the probability amplitude of being in the “down” state. (“Probability amplitude” just means that |α^**2**^| + |β^**2**^| = 1. To make the probabilities work, α and β are complex numbers.) We also saw that spin can be used to represent the 0s and 1s in quantum computing, with the spin “up” state representing the binary digit 0, say, and “down” representing 1. I wrote these “up” and “down” states as row vectors for convenience, but in quantum mechanics state vectors are written as column vectors, and they are often called “kets.” In chapter 4 I spoke about the unit vectors ***i, j, k*** being a “basis” for constructing a vector ***v***—and analogously, the basis for the spin state ψ of an electron, or a qubit, can be chosen so that $\left(\begin{matrix} 1 \\ 0 \end{matrix}\right)$ represents the spin “up” state, and $\left(\begin{matrix} 0 \\ 1 \end{matrix}\right)$ for spin “down.” Using what is known as “Dirac notation,” after quantum pioneer Paul Dirac, these basis vectors are denoted by the kets |0〉 and |1〉. So the state vector for a qubit is represented in component form as

::: {.displayeq}

$$|\psi\rangle\alpha|0\rangle+\beta|1\rangle.$$

:::

What this means is that until it is actually observed, the qubit is in a state of superposition between the two states |0〉 and |1〉, α and β representing the respective likelihoods of it being in each state. Tensor products come into it when qubits are *combined*, as of course they must be to make a usable quantum computer. To go gently, though, let’s take just two qubits, and represent their states as

::: {.displayeq}

$$|\psi_{1}\rangle\left(\begin{matrix} \alpha \\ \beta \end{matrix}\right),|\psi_{2}\rangle=\left(\begin{matrix} \gamma \\ \delta \end{matrix}\right).$$

:::

<!--p252-->
To find the state of the combination of these two systems, take their tensor product:

::: {.displayeq}

$$|\psi\rangle=|\psi_{1}\rangle\otimes|\psi_{2}\rangle=\left(\begin{matrix} \alpha\gamma \\ \alpha\delta \\ \beta\lambda \\ \beta\delta \end{matrix}\right).$$

:::

It’s a 4 × 1 vector giving the probability amplitudes for four possibilities: both qubits are in the up state (both represent zeroes), the first is up and the other is down, the second is up and the first is down, and both are in the down state. It’s this ability for each qubit to represent a superposition of 0s and 1s that makes quantum computers so potentially powerful, for they can carry out multiple computations at the same time. You can sense this power from the fact that in a system of *n* qubits, the tensor product will have 2^*n*^ complex-number components. Even with a relatively modest number of qubits that’s a lot of 0’s and 1’s being processed simultaneously.[^ch11n14]

• • •

While column vectors representing quantum states are called “kets,” represented as |*A*〉 for an arbitrary state, row vectors are called “bras,” denoted by 〈*A*|. That’s because when you put a bra and a ket together—such as when you take the scalar (or inner) product of two states |*A*〉 and |*B*〉 —you complete the bracket (“bra-ket”):

::: {.displayeq}

$$\langle B|A\rangle.$$

:::

Scalar products are needed in the “normalisation” of state vectors that ensures weights such as α and β do relate to the probabilities of a measurement result—but the point here is that the content of the *B*〉 column vector is now acting as a bra or row vector, 〈*B*|, operating on the ket |*A*〉 to give the scalar product. This sounds complicated (and technically, a bra is a “dual” of a ket, and both reside in complex vector spaces)—but you can look at it as an application of a result from ordinary vector analysis, where vectors can play different roles, depending on how you write them.

<!--p253-->
For instance, going back to our column vector ***u*** and row vector ***v***, we saw a bit earlier that ordinary matrix multiplication of ***u*** times ***v*** gives a 2 × 2 matrix (which in this case is also their tensor product). But if you swap the order, ordinary matrix multiplication of ***v*** by ***u*** gives not a matrix but a number, *v*~1~*u*~1~ + *v*~2~*u*~2~. In fact, it is the scalar product of the two vectors. (At least, it is the scalar product in flat two-dimensional Euclidean space. As I mentioned in chapter 9, the scalar product depends on the metric. In Minkowski space-time, for example, the scalar product is

::: {.displayeq}

***a*** ∙ ***b*** = *a*~1~*b*~1~ + *a*~2~*b*~2~ + *a*~3~*b*~3~ − *a*~4~*b*~4~, or ***a*** ∙ ***b*** = − *a*~0~ *b*~0~ + *a*~1~*b*~1~ + *a*~2~*b*~2~ + *a*~3~*b*~3~

:::

if the time component is denoted by a 0 subscript rather than a 4). So, you can see that it makes a difference whether you write your vector, your data, as a row or column. This is the kind of thing that might make maths seem bizarre and contradictory—but it’s just this sort of detail that piques a creative mathematician’s curiosity. And Ricci and his successors came up with a neat way around it.

First, represent the two types of vector with different notation. Following Ricci, write the components of column vectors with an “upstairs index” or superscript—so you no longer write *u*~1~ and *u*~2~ but *u*~**1**~ and *u*~**2**~. (Actually he put upstairs indices in brackets, presumably to make it clear that these are labels, not powers. As mathematicians and physicists such as Einstein and Grossmann became more adept at using index notation, they discarded the brackets.) Keep the downstairs indices, the subscripts, for the row vectors. So, in the case of a matrix formed from a column vector times a row vector, the elements can be represented as *u*~**1**~*v*~1~, *u*~**1**~*v*~2~, *u*~**2**~*v*~1~, *u*~**2**~*v*~2~, and so on. Straightaway you can see, just by looking at the notation, that you are multiplying two different kinds of vector. Decades later, Dirac would apply this distinction via his bra and ket notation.

<!--p254-->
Second, give these two entities different names, to avoid confusion. Today the word “vector” in this context refers to column vectors, while row vectors are called “one-forms” or “dual vectors.” Early twentiethcentury researchers coined these terms; the idea originates with Grassmann, who had used the term “complement” instead of “dual.” Bras are examples of one-forms. Back in the 1880s, Ricci called vectors and one-forms “contravariant vectors” and “covariant vectors,” respectively, and these names are also used today.

Actually, Ricci didn’t talk specifically about row vectors and column vectors, for these are just examples of his two types of tensor. As we’ll see in the next two sections, the general idea behind this distinction—and behind Ricci’s choice of names—comes from a concept that goes beyond index notation and tensor products, which are often the main aspects of tensor maths needed in data science.

In fact, even the position of indices is not so important in data science as it is in maths and physics, for often the data are entered without any need for abstract symbols at all. Rather, it’s the rank and “shape” that many programmers use to characterise each different tensor. For example, in TensorFlow (and other programming language libraries such as Python’s Numpy), the shape refers to the dimension. A scalar has a shape 0, represented as an empty bracket: [ ]. A vector is programmed as a string of numbers, one for each component; its shape is the number of components, so a 3-D vector has shape [3]. Rank 2 tensors can be represented as matrices, and their shape is the number of rows and columns, so the 2 × 2 matrix above would have shape [2, 2]. A rank 3 tensor, such as a 2 × 3 × 5 array, has shape [2, 3, 5], and so on.

An advantage of emphasising shape is that programmers can include what TensorFlow calls “ragged tensors,” arrays with strings of different sizes—a string of words or sentences, perhaps, where the number of letters or words has nothing to do with the dimension of space. As I’ve mentioned, in *n*-dimensional space, each index on a tensor must take a value between 1 and *n*, but “ragged tensors” are allowed to have variable sizes. This is a nice example of the way data scientists have adapted a mathematical concept for their own needs.

<!--p255-->
All this is a long way from the way tensors were first used, albeit unwittingly—as stress and metric tensors in mathematical physics. Still, these earlier uses also had to do with representing and handling information. By “handling” I mean knowing how to combine information into new tensors and how to interpret and apply the results. So, to earn the title of tensor, it’s not enough simply to put information into a list or array—the Mesopotamians were doing that sort of thing four thousand years ago. To be a tensor, the arrays have to obey certain rules, just as we saw with vectors and matrices in chapter 4. We’ve already met tensor products, and there are also rules for addition, of course. We saw how the parallelogram rule for adding vectors takes account of their magnitude and direction, but more generally, vector and tensor addition—and multiplication, too— must obey the laws of “linearity.” (This means, for example, that

::: {.displayeq}

(2***a***) ∙ ***b*** = 2(***a*** ∙ ***b***) = ***a*** ∙ (2***b***), and ***a*** ∙ (***u*** + ***v***) = ***a*** ∙ ***u*** + ***a*** ∙ ***v***

:::

—analogous to the distributive law in arithmetic.)

But the most important thing in maths and physics is the ability of tensors to represent information invariantly—“absolutely”—without spurious data coming from the choice of coordinates. This is not an issue for many data science applications, although it is important in some of them, such as the neural networks we saw earlier. Either way, there’s much more to the idea of a tensor than figure 11.1 suggests.

## INVARIANCE (AND AN ACADEMIC SCANDAL)

The idea of invariants—things that stay the same when you rotate, translate or otherwise change your frame of reference—had been intriguing mathematicians at least since Cayley and Boole were working together in the 1840s. In chapter 9 we saw many examples of invariance, from the shape of snowflakes to the scalar product ***a*** ∙ ***b*** to the Minkowski metric,

::: {.displayeq}

*ds*^**2**^ = *dx*^**2**^ + *dy*^**2**^ + *dz*^**2**^ − (*cdt*)^**2**^

:::

(where units are often chosen so that *c* = 1). But each of these shapes and expressions is invariant only with respect to a particular group of coordinate transformations, as we saw in figures 9.1 and 9.3.

<!--p256-->
In studying invariants, mathematicians such as Riemann had their eye on physical applications—in his case, the curvature of surfaces—while others, including Cayley and Klein, were interested in the purely mathematical structure of these groups of coordinate transformations. Klein had been the managing editor of the journal *Mathematische Annalen*, a position he took up when his mentor Alfred Clebsch suddenly died of diphtheria. Clebsch is the professor to whom Justus Grassmann had given a copy of his father’s *Ausdehnungslehre* when he arrived as a student at Göttingen in 1869. Clebsch was impressed, and he went on both to extend Grassman’s ideas and to cofound the *Mathematische Annalen* as an outlet for research on invariant theory.

There are many other names I could add to the list of mathematicians working on invariants and/or differential forms during the latter half of the century—including Ricci’s former maths professor at Pisa, Enrico Betti. There’s an overlapping thread here, for one of Betti’s achievements was his generalisation of Stokes’s theorem to *n* dimensions. We saw earlier that the original 3-D version of this theorem had been first published in the 1854 Smith’s Prize exam, which Maxwell sat—and that it relates a surface integral to a line integral. The key thing is that it does this in an *invariant* way— you should get the *same* surface area no matter the coordinates you use. So Betti’s work on this is an example of the diverse reasons mathematicians were interested in coordinate transformations and invariance.

Betti also reminds us of the revolutionary upheavals taking place in Europe in the nineteenth century. As a student in 1848 he’d fought in two of the first battles for Italian independence—his thesis advisor had led the Tuscany university battalion. It lost, to the Austrians, but luckily Betti survived, and went on to become a significant mathematician and teacher— and it was on his advice that Ricci had gone to Berlin to study with Klein.[^ch11n15] Betti also contributed to the new Italian journal for pure and applied maths, *Annali di Matematica pura e applicata*. Specialist journals, such as *Annali* and Clebsch and Klein’s *Annalen*, were important places for mathematicians to publish their work—and had they existed in Thomas Harriot’s day, perhaps his work would not have been lost for so long: one of the world’s first modern scientific journals was the *Philosophical Transactions* of the Royal Society of London, which began in the 1660s, nearly half a century after Harriot’s death.

<!--p257-->
Countries with established universities, scientific societies, and journals tended to be at the centre of mathematical progress, and in 1884 Ricci published some of his first results on invariance in the *Annali*. He didn’t know of Riemann’s work when he first set out on this journey. Instead, he took his initial inspiration from the purely mathematical approach of Elwin Christoffel’s 1869 paper. As I’ve mentioned, Christoffel and Riemann both independently discovered what are now called the Christoffel symbols and the Riemann (or Riemann-Christoffel) tensor, which, as Riemann showed in his 1861 paper, gives the invariant condition for knowing whether a surface is flat or not. Christoffel didn’t refer to curvature at all—other than in a note at the end of his paper, saying that in his 1854 habilitation thesis Riemann had applied quadratic differential forms to the line element. But that was enough for Ricci, who went searching for Riemann’s papers.

At the same time, he had his teaching—not always an easy task for a reserved, diffident person like Ricci. But he was passionate about his subjects, and if his lectures lacked colour, they were nonetheless clear and rigorous—Ricci was a great one for proof. As he told a colleague, “I don’t deny that the proofs [in my lectures cause] some difficulty when they are presented to students who unfortunately don’t take their education seriously.” Still, he went on, that wasn’t going to stop him from presenting maths the way it should be presented. After all, “if my own judgment doesn’t deceive me, these proofs are beautiful.” Besides, the best students were inspired by such rigour, and the rest, he thought, might benefit from it, for they had come from secondary school with insufficient grounding in mathematical fundamentals.[^ch11n16] I’m sure many lecturers today can empathise with him.

<!--p258-->
Ricci was also busy applying for promotion to a full professorship. On his first attempt, in 1884, he and his young rival, Guiseppe Veronese, missed out to a more senior candidate. Ricci was happy to defer to seniority, but Veronese appealed. He also pointed out that he was from a working-class background (unlike Ricci) and needed the increased salary to “help my poor parents and my brothers.” The plea was treated kindly by the authorities, and he was given a permanent teaching position with an increase in pay. Unruffled, Ricci was hopeful when he tried again for a full professorship in 1887. He was now thirty-four and had a reputable publishing record—but so did Veronese, who applied for the same position. The ensuing battle made front-page news, with rumours that faculty skullduggery ultimately deprived Ricci of his rightful promotion. The saga dragged on, and it would take another three years for Ricci finally to gain his professorship.[^ch11n17]

Meantime, what else could he do, brilliant mathematician that he was, but throw himself into the work that would, ultimately, immortalise his name?

## HOW TO HANDLE ALL THOSE INDICES

Over the next few pages, I’m going to spend time showing why Ricci had two different kinds of vector—or in modern terms, a vector and a oneform—because they are prototypes for all tensors. (Actually, he started with general tensors and gave vectors as an example: perhaps because vector analysis wasn’t so well established then as it is today, but also because his theory arose primarily from the study of invariant differential forms rather than from vector analysis.) These two types of vector relate to Ricci’s index notation, which is a marvelous example of the way mathematicians use symbolism to bring out the underlying structure of mathematical concepts. We saw something of this with the rise of algebra in chapter 1 and the war over vector notation in chapter 8. Here, though, there’s detail and an approach that may be unfamiliar to you, although the only maths tools you need are vector and matrix multiplication.

<!--p259-->
As always, though, if you get to the point where you just want to take my word for it, skip down to the next section. And if, once you get there, you decide you just want to see how Einstein and Grossmann used tensors in formulating the framework for general relativity, then go ahead to the next chapter. Ricci would understand: it always takes effort to learn a new skill, he wrote in the introduction to his seminal overview of his “absolute differential calculus.”[^ch11n18] Tait had said something similar when he was trying to convince people of the advantages of quaternions. But like Tait, Ricci was sure that after “surmounting the difficulties of initiation,” readers would soon convince themselves of the “elegance and clarity” of these methods—methods that hinge on the right *notation* for the idea of invariance. It’s a notation that relies on spotting patterns, so it’s also rather fun.

• • •

If tensors were to encode the idea of invariance under coordinate changes, Ricci had to find the specific relationship between the components of a tensor in one frame and those of the same tensor in the new frame. We saw an implicit example of this for the position vectors in figure 9.1, where I showed geometrically that the magnitude of ***a***, and also the scalar product ***a*** ∙ ***b***, are invariant when you rotate the coordinate axes. What I didn’t show then was how each vector component changed, but this is the kind of question that Ricci was trying to answer.

He began by generalising the way coordinate transformations work. But I’ll start with a specific example, the rotation in figure 9.1, where the transformation equations from the usual *x*-*y* coordinates to the rotated *x′*-*y′* ones are:

::: {.displayeq}

*x′* = *x* cos θ + *y* sin θ, *y′* = −*x* sin θ + *y* cos θ.

:::

You might have noticed already that these are linear equations (they contain just *x* and *y*, with no powers or other products), and that you can write them as a matrix equation:

::: {.displayeq}

$$\left(\begin{matrix} x' \\ y' \end{matrix}\right)=\left(\begin{matrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{matrix}\right)\left(\begin{matrix} x \\ y \end{matrix}\right).$$

:::

This is another instance of the way vectors and matrices pop up again and again when mathematicians want to represent and handle information. (You might also have noticed that the rotation matrix here is similar to the one in fig. 4.2, but there we were rotating the robot arm, whereas here, as in fig. 9.1, the vector stays the same, but the axes themselves rotate.)

If you let $X=\left(\begin{matrix} x \\ y \end{matrix}\right)$ and let *A* represent the “transformation matrix,” you can write this coordinate transformation equation more economically as:

::: {.displayeq}

***X′*** = *A**X***.

:::

<!--p260-->
As we saw in chapter 1, when algebraists began to use symbols instead of words or specific numerical examples, they were able to generalise their results—so this equation can be generalised, and the symbol *A* can stand for *any* 2-D linear homogeneous coordinate transformation. (“Homogeneous” here just means that the transformation maps the origin *O* to the origin *O′* of the new frame, and you need this for tensors, because then tensor equations such as ***a*** ∙ ***b*** = 0—or the condition for flatness, Riemann tensor = 0— will remain invariant.) And from what we’ve already seen of vectors and matrices, this equation also suggests we can easily move from our original 2-D rotation to transformations in any number of dimensions.

Different authors use different symbols, but in teasing out and generalising the way coordinate transformations behave, I’ll adapt the notation widely used in textbooks on tensor analysis today. It differs only slightly from Ricci’s; in particular, both contravariant vector components *and* coordinates are written with upstairs indices, but Ricci denoted coordinates as we usually meet them in maths classes: *x*~1~, *x*~2~, So, to explore a bit further the structure of a coordinate rotation—and to get a handle on how coordinate transformations work in general—first up, I’ll use *x*^1^, *x*^2^ for the original coordinates (*x, y*), and *x*^1′^ ,*x*^2′^ for the new ones (*x′, y′*). Then the original rotation transformation equation *x′* = *x* cos θ + *y* sin θ can be generalised like this:

::: {.displayeq}

$$x^{1}=A_{1}^{1}x^{1}+A_{2}^{1}x^{2},$$

:::

where $A_{1}^{1'}=\cos\theta,A_{2}^{1'}=\sin\theta$ in our specific rotation case. (For the elements of the matrix representing the coordinate transformation, I’ve used $A_{1}^{1'}$, and so on, rather than the *a~ij~* notation of linear algebra. You’ll see why shortly.) Similarly, the transformation equation *y′* = −*x* sin θ + *y* cos θ can be generalised as

::: {.displayeq}

$$x^{2}=A_{1}^{2}x^{1}+A_{2}^{2}x^{2}.$$

:::

<!--p261-->
There’s a pattern in the indices here: in each of these general equations, the same dashed upstairs index appears throughout. This means you can represent these two equations in one, where the general upstairs index μ′ (pronounced “mu-dash”) is presumed to take the values 1 and 2 (each in turn), since there are two independent coordinates in 2-D space:

::: {.displayeq}

$$x^{\mu'}=A_{1}^{\mu'}x^{1}+A_{2}^{\mu'}x^{2}.$$

:::

Notice, too, that in each term in the sum on the right-hand side, the downstairs index on the matrix component is matched by an upstairs one on the original coordinate; so, using the Greek letter σ (sigma) and the summation notation I flagged at the end of chapter 10, you can simplify the above expression to:

::: {.displayeq}

$$x^{\mu'}=\sum_{\sigma=1}^{2}A_{\sigma}^{\mu'}x^{\sigma}.$$

:::

Once Einstein gets on top of all this, he’ll make this notation even simpler. He’ll say, look at the pattern and notice that whenever you have the same up and down index—in this case, a σ appearing twice like this— you add all those terms. And since you also know what dimension you’re working in, why not leave out the summation sign altogether, and let the repeated indices tell you that this is a sum:

::: {.displayeq}

$$x^{\mu'}=A_{\sigma}^{\mu'}x^{\sigma}.$$

:::

Today this notation is called the Einstein summation convention.

You can see where I’m going with this: when you add more variables— so that you’re working with an *n*-dimensional space (Riemann’s manifold!)—you can use the *same* symbolic equation, except that now your indices μ′ and σ will run from 1 to *n*, and your sum implicitly has not two terms but *n* of them. That’s *n* equations (one for each value of μ′), each one a sum of *n* terms (one term for each value of σ), all encapsulated in just one small equation. It’s brilliantly economical!

<!--p262-->
I’ve chosen μ′ and σ for the index labels here, but they are meant to represent general indices, so there’s nothing specific about the letters μ and σ themselves—just as the letter *x* for the unknown in school algebra is an arbitrary choice (as was my choice of $A_{\sigma}^{\mu'}$ for the transformation matrix components). So don’t focus on the specific letters here, but rather on the patterns of the indices. As we’ll see, it’s this economical symbolism that makes the equations of physics so beautifully elegant when written in tensor form.

## INVARIANCE AND TENSORS

Now we’re getting to what all this has to do with invariance. The components of a vector ***a*** are measured from the coordinate axes, so they transform in the same way, $a^{\mu'}=A_{\sigma}^{\mu'}a^{\sigma}$. For example, for the rotation in figure 9.1, the components will transform just like the coordinates in the equations above, so we have—using Ricci’s upstairs indices for the (contravariant) vectors ***a*** and ***b***—

::: {.displayeq}

*a*^**1′**^ = *a*^**1**^ cos θ + *a*^**2**^ sin θ, *a*^**2′**^ = −*a*^**1**^ sin θ + *a*^**2**^ cos θ,

:::

and similarly for *b*^**1′**^ and *b*^**2′**^. When you multiply these pairs of components to form the scalar product in the rotated frame, you find that

::: {.displayeq}

*a*^**1′**^*b*^**1′**^ + *a*^**2′**^*b*^**2′**^ = *a*^**1**^*b*^**1**^ + *a*^**2**^*b*^**2**^.

:::

You get the same number—the same scalar product—in both frames, which is what it means to be invariant. So this is an algebraic version of the geometric argument in figure 9.1.

But what about the scalar product as we write it in undergrad notation, *a*~1~*b*~1~ + *a*~2~*b*~2~?

In Ricci’s notation this would be the scalar product of covariant or row vectors (or one-forms). As we’ll see later, it turns out that in the usual Euclidean space and Cartesian coordinate system, there’s no need to distinguish between upstairs and downstairs indices on vector components. But first we need to see more about what the downstairs indices mean for tensors.

<!--p263-->
The matrix of components $A_{\sigma}^{\mu'}$ for transformations of coordinates and (contravariant) vectors shows how to write the new coordinates or vector components in terms of the old ones. So, to write your original coordinates in terms of the new ones, the transformation goes the other way. We saw this for the Lorentz transformations in figure 9.3, but you can see how to do it for *any* coordinate transformation by going back to writing general transformation equations as ***X′*** = *A**X***. Then matrix algebra tells you that to transform the other way, you’ll have

::: {.displayeq}

***X′*** = *A**X*** ⟹ *A***^−1^*X′*** = ***X***.

:::

For example, the inverse of the rotation matrix $\left(\begin{matrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{matrix}\right)$ is $\left(\begin{matrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{matrix}\right)$, since *AA*^**−1**^ = *I*. This suggests that the *first column* in the original matrix becomes the *first row* in the inverse, and similarly for the second row. In other words, the columns of the original matrix—the contravariant vectors, with their upstairs indices—become rows, or covariant vectors with downstairs indices, in the inverse matrix. Which means that all you have to do to represent the components of the inverse matrix is to interchange the indices on the original one: $A_{\sigma}^{\mu'}\to A_{\mu'}^{\sigma}$. This is why Ricci wrote covariant vectors (one-forms or dual vectors) with a downstairs index: the transformation rule for their components is $a_{\mu'}=A_{\mu'}^{\sigma}a_{\sigma}$. Using this rule, you can prove that *a*~1~*b*~1~ + *a*~2~*b*~2~ is invariant, just as *a*^**1**^*b*^**1**^ + *a*^**2**^*b*^**2**^ is invariant.

Generalising vectors to tensors, Ricci said that if all the indices on the components of a tensor, of any rank, are upstairs, it is called “contravariant”; it will transform just like contravariant vector components, but with the appropriate number of transformation matrices $A_{\mu'}^{\sigma}$ (as you can see in the endnote[^ch11n19]). If all the indices are downstairs, Ricci called it a “covariant” tensor. If some indices are up and some down, it’s called “mixed.” For example, we saw that the components of the tensor product of a column vector by a row vector were *u*^**1**^*v*~1~, *u*^**1**^*v*~2~, *u*^**2**^*v*~1~, *u*^**2**^*v*~2~, and so on, so they are the components of a mixed tensor.

<!--p264-->
This is why Ricci said that vectors are tensors: their components—like higher-order tensor components—transform in a *specific way* under a change of coordinates. And scalars are tensors because they are just numbers or numerical expressions that don’t depend on the coordinates at all—so they are automatically invariant under coordinate transformations. ( Just to dot i’s, not all numbers are invariants or scalars—for instance, frequency depends on the relative motion of the observer, as exemplified in the Doppler effect that we’ll see in the next chapter. And if the Unruh effect is finally detected, it may even turn out that temperature is not exactly the coordinateindependent scalar I said it was in chap. 7 and fig. 11.1—although you’d have to be traveling close to the speed of light to detect one degree of temperature change.[^ch11n20])

## A MODERN VIEW

Index notation isn’t all about coordinate transformations, though, as we’ll see in the next section. So here I want to outline a modern view of tensors. Coordinate transformations are still at the heart of it, but rather than *defining* tensors through the way their *components* transform under these coordinate changes, modern mathematicians define “whole tensors” as *linear operators* that yield invariants.

We saw in chapter 6 that $\frac{d}{dx}$ is an operator and so is its vector extension nabla, $\nabla=\frac{\partial}{\partial x}\boldsymbol{i}+\frac{\partial}{\partial y}\boldsymbol{j}+\frac{\partial}{\partial z}\boldsymbol{k}.$. You have to “insert” a function into the operator $\frac{d}{dx}$ to get its derivative, while inserting a function *f* into nabla gives you “grad *f*,” a vector whose components are partial derivatives of the function. But a tensor is more like the divergence operator, ∇∙, which operates on a vector to give a scalar. And scalars, as we just saw, are always invariant. For example, in Maxwell’s equations, ∇∙ operates on the electric and magnetic field vectors, giving a scalar:

::: {.displayeq}

∇ ∙ ***E*** = 4πρ ∇ ∙ ***B*** = 0.

:::

<!--p265-->
Similarly, multiplying a row vector (a covariant vector or one-form or dual vector) by a column vector (a contravariant vector) gives a scalar— the scalar product in Euclidean space. So, you can think of a one-form as something that *operates on* a vector to give a scalar, an invariant. This definition gets right to the heart of what tensors are all about: not component and coordinate transformations per se but *invariance* under those transformations.

Going up an order (or rank), you can think of a matrix as a mixed second-order tensor that operates on a vector *and* a one-form to give a scalar. More specifically, it operates on a (column) vector to give another (column) vector—like the rotation matrix *A* in the transformation equation ***X′*** = *A**X***, where *A* “operated on” $X=\left(\begin{matrix} x \\ y \end{matrix}\right)$ to give a new vector, $\left(\begin{matrix} x' \\ y' \end{matrix}\right)$; then, as we just saw, when you operate on this new vector with a row vector (one-form), you get the scalar product. The higher the order of the tensor, the more vectors and/or one-forms it must operate on to give a scalar.

This conception of tensors as operators is fundamental in quantum theory, for example, while pure mathematicians take the idea into the more abstract territory of multilinear mappings. So there’s much more to say about the notion of linear operators—and about “vector spaces,” too, and other subtleties such as the difference between vectors and one-forms, and the significance of transforming “basis” vectors and one-forms rather than vector and tensor components—but that’s beyond my scope here. Still, if you’ve stayed with me so far, I hope this section and the previous one have given you a feeling for the way mathematicians develop their ideas—how they sort out the rules that their mathematical constructs have to obey, and how they interpret these rules and constructs in terms of important ideas such as invariance. These interpretations evolve as mathematicians build on their forerunners’ insights. This is a key theme of this book, where we’ve already seen this kind of mathematical development, from cuneiform tables and computational algorithms to symbolic algebra, vectors, and matrices, and from calculus to vector analysis. Later in this chapter we’ll take the final step to tensor calculus.

## THE AMAZING COMPUTATIONAL POWER OF TENSOR SYMBOLISM

<!--p266-->
The position of the indices on tensor components plays a vital role in tensor equations and computations. For example, we’ve seen that in Euclidean space, multiplying a row (covariant) vector ***v*** by a column (contravariant) vector ***u*** gives their scalar product. Using Ricci’s index notation and Einstein’s summation convention we have a beautifully economical representation of this:

::: {.displayeq}

*v*~1~*u*^**1**^ + *v*~2~*u*^**2**^ ≡ *v*~μ~*u*^**μ**^.

:::

There’s nothing special about my choice of the letter μ here—again, I could have chosen any letter, because what matters is that both indices are the same (so this is a sum).[^ch11n21] The amazing thing about this representation is this: the fact that each pair of up and down indices is the same *actually tells us* that this scalar product is invariant under appropriate coordinate transformations. You can *prove* it’s invariant, simply by inserting the transformation equations, as you can see in the next endnote. But once you understand how to do that, the index notation saves you the bother.[^ch11n22]

It really is remarkable the way tensor notation makes things easier. Nonetheless, you might be grumbling that so far, we’ve had three different types of scalar product, with upstairs indices, downstairs indices, and now mixed indices. That’s simply because in tensor analysis there are two types of vector, but I’ll show shortly how it all comes together in one general expression. For now, I want to focus on the remarkable way the mixed form of the scalar product shows invariance *through its very symbolism*. This carries over for higher-order tensors, too, so whenever you see an expression where each downstairs index is matched by the same upstairs one—such as *T*~μν~*h*^**μν**^ (ν is pronounced “nu”)—you know it is invariant. It’s quite extraordinary, really—and this is just one example of why Ricci’s index notation is such a brilliant innovation. He was right to say it is worth the struggle of initiation.

Tensor expressions such as *v*~μ~*u*^**μ**^ and *T*~μν~*h*^**μν**^ are examples of the tensor operation called “contraction”—because when you set a pair of upstairs and downstairs indices equal, you’re reducing, or contracting, the rank of your tensor. For instance, *v*~μ~*u*^**λ**^ (where λ is pronounced “lambda”) is a general component of a mixed rank 2 (two-index) tensor, but when you set λ = μ, you reduce the rank (or order) to 0, because *v*~μ~*u*^**μ**^ is a scalar (the scalar product).

<!--p267-->
You don’t have to contract all the indices unless you want to find the invariants. For instance, *T*~μν~*h*^**λσ**^ is a general component of a rank 4 (4-index) tensor, but if you set λ = μ you get a two-index tensor, with components *T*~μν~*h*^**μσ**^. It’s a 2-index tensor because you’re summing on the repeated index μ, leaving only the ν and σ indices free. It’s as if contracting the μ indices “cancels” them, rather like the way you “cancel” terms in the chain rule, $\frac{dy}{dx}=\frac{dy}{du}\frac{du}{dx}$, although in this case you’re summing terms rather than “deleting” them.

There’s an especially important contraction now called the “inner product” in tribute to Grassmann. As we saw earlier, Hamilton’s system, which morphed into our university-level vector analysis, was perfectly adapted for three-dimensional problems—remember those 3-D rotations that had set him on the path to discovering quaternions! Grassmann’s was more abstract, so although it was harder to apply, it was more readily adaptable to the *n*-dimensional spaces that Riemann created, and in which Ricci’s tensors operate. So, by the early twentieth century, Grassmann’s ideas had begun filtering into the mainstream, giving added conceptual substance to the vector and tensor analysis that had descended from Hamilton. Ricci was in the Hamiltonian tradition, and in his 1900 overview of his calculus he doesn’t use the term “inner” (*or* “outer”) product; by 1916, however— and to take just one example—in his overview of general relativity theory Einstein will use these Grassmannian terms.

So, what is the inner product? It comes from contracting a pair of indices on a mixed tensor formed from the outer product of two other tensors. For example, suppose you form the outer product of a covariant tensor ***T*** with components *T*~μν~ and a vector ***u*** with components *u*^**σ**^. You get a new mixed tensor whose components are *T*~μν~*u*^**σ**^. Now contract the indices by setting σ = μ, to give *T*~μν~*u*^**μ**^; this is the general component of the inner product of ***T*** and ***u***. (In component form, it is *T*~1ν~*u*^**1**^ + *T*~2ν~*u*^**2**^ + … , the number of terms depending on the dimension of the space.)

<!--p268-->
But look what happens if you take the *outer* product of this tensor with another (contravariant) vector, ***v***: you get a new tensor, with components *T*~μν~*u*^**μ**^*v*^**λ**^. (So inner products reduce or contract the rank, and outer products increase it.) If you now set λ = ν, you get yet another new tensor, with components *T*~μν~*u*^**μ**^*v*^**ν**^. This is the inner product of *T*~μν~*u*^**μ**^ and *v*^**λ**^. Like the scalar product *v*~μ~*u*^**μ**^, this tensor is a scalar (an invariant number or function), because each pair of indices is the same.

In fact, if ***T*** is a metric tensor—which from now on, and cribbing from Einstein, I’ll denote by ***g***, with components *g*~μν~—then this particular inner product is, in fact, just what we’ve been used to calling the scalar product of ***u*** and ***v***. For, as we’ve seen, the metric actually defines the scalar product. For example, the 2-D Euclidean metric

::: {.displayeq}

*ds*^**2**^ = *dx*^**2**^ + *dy*^**2**^ ≡ (*dx*^**1**^)^**2**^ + (*dx*^**2**^)^**2**^

:::

has components *g*~11~ = *g*~22~ = 1, with the other components zero; so, writing out the sums indicated by the repeated indices, the inner product in this case is:

::: {.displayeq}

*g*~μν~*u*^**μ**^*v*^**ν**^ = *g*~11~*u*^**1**^*v*^**1**^ + *g*~12~*u*^**1**^*v*^**2**^ + *g*~21~*u*^**2**^*v*^**1**^ + *g*~22~*u*^**2**^*v*^**2**^ = *u*^**1**^*v*^**1**^ + *u*^**2**^*v*^**2**^.

:::

This is, indeed, the usual vector analysis scalar product ***u*** ∙ ***v***, except with Ricci’s upstairs indices because here both vectors are contravariant.

## A PEEK AT SYMMETRY, WHY METRICS ARE TENSORS, AND SORTING OUT THE INDICES ON SCALAR PRODUCTS

We saw in chapter 4 that the scalar product is commutative (it’s only the vector product that isn’t). And we just saw that ***u*** ∙ ***v*** = *g*~μν~*u*^**μ**^*v*^**ν**^ (and by implication ***v*** ∙ ***u*** = *g*~νμ~*v*^**ν**^*u*^**μ**^). So, this commutativity, ***u*** ∙ ***v*** = ***v*** ∙ ***u***, means that we must have *g*~μν~ = *g*~νμ~. The indices on the metric tensor components are, therefore, *symmetric*, like a reflection in a mirror. This symmetry is invariant under linear coordinate transformations because the scalar product is, so it’s handy in computations. As we’ve seen, invariance in general is a mathematical “symmetry,” because when something is invariant, it stays the same—just like the shape of a reflected image or a rotated snowflake.

<!--p269-->
In chapter 9 we met the Euclidean and Minkowski metrics, where the coefficients of the differentials are constant, signifying that they define flat spaces. In chapter 10, we saw that Gauss proved information about the curvature of a surface is contained in the *coefficients* of the differentials in the general 2-D metric, and that Riemann generalised this to curved *n*-dimensional spaces. So, with arbitrary coordinates *x*^**μ**^, a metric in curved space can be expressed as

::: {.displayeq}

*ds*^**2**^ = *g*~μν~*dx*^**μ**^*dx*^**ν**^,

:::

where now the coefficients *g*~μν~ are not constants but functions of the coordinates.

From the repeated indices you can see straightaway that the “distance” or space-time interval measure, *ds*^**2**^, is invariant, and you can prove it by using the coordinate transformation equations.[^ch11n23] We’ve already seen examples of this general result: the Euclidean metric is invariant under transformations such as rotations, while the Minkowski metric is invariant under Lorentz transformations (fig. 9.3). But why is the metric a tensor? The clue is in the invariance; after all, representing invariance is the whole point of tensors.

To see this in more detail, we saw just before that *g*~μν~*u*^**μ**^*v*^**ν**^ is the scalar product of the vectors ***u*** and ***v***. This suggests that the metric ***g*** “operates on” these two vectors to produce a scalar—the invariant scalar product. Which means the metric is a tensor according to the modern definition I gave two sections back.

It’s also a tensor according to Ricci’s definition, because we know the transformation equations for the contravariant vector components *u*^**μ**^, *v*^**ν**^, so the transformation equation of *g*~μν~ must be that of a covariant rank 2 tensor if *g*~μν~*u*^**μ**^*v*^**ν**^ is to be an invariant scalar. The previous endnote illustrates the calculations that show this, but you can see already that the modern view is more elegant.

• • •

<!--p270-->
There’s one last thing I want to show you before I briefly outline Ricci’s crowning achievement, tensor derivatives. When I spoke earlier of the scalar product in the various forms *v*~1~*u*~1~ + *v*~2~*u*~2~, *v*~**1**~*u*^**1**^ + *v*~**2**~*u*^**2**^, and *v*~1~*u*^**1**^ + *v*~2~*u*^**2**^, I was assuming we were in 2-D Euclidean space, where the metric is *ds*^**2**^ = *dx*^**2**^ + *dy*^**2**^. More generally, we’ve just seen that in a space with a metric whose components are *g*~μν~, the scalar product of two (contravariant) vectors ***v*** and ***u*** is *g*~μν~*u*^**μ**^*v*^**ν**^. Now look what happens if I swap the positions of the indices and write *g* ^**μν**^*v*~μ~*u*~ν~. This suggests the scalar product of two covariant vectors. But what is *g* ^**μν**^? Ricci defined *g* ^**μν**^ so that it has a very special property: it “raises the index” of a covariant tensor. We saw a little earlier that *T*~μν~*h*^**μσ**^, with repeated (contracted) μ indices, is a two-index tensor, as if we’d “canceled” the μ’s when we summed them. So, Ricci defined the special contractions

::: {.displayeq}

$$g^{\mu v}g_{\mu\sigma}=g_{\sigma}^{v},\text{and}g^{\lambda\sigma}g_{\sigma}^{v}=g^{\lambda v}.$$

:::

(Actually, Ricci used *a^rs^* rather than *g* ^**μν**^, but otherwise I’m using his definitions.) In other words, *g* ^**μν**^ has taken *g*~μσ~ to $g_{\sigma}^{v}$. And *g*^**μν**^*g*^**λσ**^ has taken *g*~μσ~ to *g*^**λν**^. It works the other way, too: *g*~μν~ can lower the indices. (That’s because Ricci essentially defined the matrix representations of the metric components *g*~μν~ and *g* ^**μν**^ to be inverses of each other. But the key thing is that these *are* definitions.)

Ricci defined this as a general property, so that the metric tensor can raise or lower indices when it is contracted with *any* tensor. This is important in tensor equations such as Einstein’s, as we’ll see. But it also brings all those different forms of the scalar product together in a rather brilliant way. The contraction *g*~μν~*v*^**μ**^ lowers the index on the vector, giving *v*~ν~. This means that in general, *g*~μν~*v*^**μ**^*u*^**ν**^ = *v*~ν~*u*^**ν**^, just as I had earlier for the particular scalar product of the row and column vector! Similarly, *g* ^**μν**^*v*~μ~*u*~ν~ = *v*^**ν**^*u*~ν~.

But here’s the really interesting thing. In Euclidean space, using Cartesian coordinates, we know that the metric is *ds*^**2**^ = *dx*^**2**^ + *dy*^**2**^. I’m keeping to 2-D for simplicity, but of course you can add more dimensions and the result I’m heading to will be the same: namely, in this situation it doesn’t matter if you write your vectors’ indices with upstairs indices or downstairs ones. That’s because (in 2-D)

::: {.displayeq}

*v*~ν~ = *g*~μν~*v*^**μ**^ = *g*~1ν~*v*^**1**^ + *g*~2ν~*v*^**2**^,

:::

<!--p271-->
but the only nonzero components of the Euclidean metric are *g*~11~ = 1 = *g*~22~, so, you have

::: {.displayeq}

*v*~1~ = *g*~11~*v*^**1**^ + *g*~21~*v*^**2**^ = 1 × *v*^**1**^ + 0 × *v*^**2**^ = *v*^**1**^,

:::

and similarly, *v*~2~ = *g*~12~*v*^**1**^ + *g*~22~*v*^**2**^ = *v*^**2**^. In other words, in Euclidean space with the usual Cartesian coordinates, there’s *no difference* between components of a vector and a one-form (that is, between Ricci’s contravariant and covariant vectors). That’s why, in ordinary vector analysis, there’s no need to worry about this distinction in terminology or in the position of indices.

## TENSOR CALCULUS, VERY BRIEFLY

The biggest question for Ricci was, what happens if you differentiate a tensor? More specifically, is the derivative a tensor? If it’s not, then tensors are not much use in physics, where physical phenomena are widely modeled by differential equations—as in Newton’s laws of motion and Maxwell’s equations of electromagnetism, for example. As we saw in chapter 9, the equations of physics must also keep their form invariant, even when you change from one reference frame to another. Otherwise, different observers would deduce different laws of physics, and we’d never be able to agree on the nature of physical reality.

<!--p272-->
Form-invariant equations are called “covariant,” and Ricci called his invariant derivative a “covariant derivative.” It’s not the same as an ordinary or partial derivative, because it turns out that the partial derivative of a vector component *u*^**μ**^ with respect to one of the coordinates in that frame, say *x*^**λ**^, doesn’t, in general, transform like a tensor. Ricci found the right covariant form of the derivative by using an invariant expression discovered by Christoffel. It amounts to adding to the partial derivative a term involving the Christoffel symbols I mentioned in chapter 10. Ricci followed Christoffel and denoted these symbols with curly brackets, but today, following Einstein and others, they’re usually denoted by $\Gamma_{\sigma\lambda}^{\mu}$. (The symbol Γ is the upper-case Greek letter gamma; the indices fit in with the relevant transformation equations, although today they are interpreted as the coefficients of the derivatives of basis vectors. For instance, in Cartesian coordinates, the basis vectors are ***i, j, k***. They are constant, so their derivatives are zero, and hence so are the Christoffel symbols in this case. So, in Euclidean space, you only need partial derivatives!)

Taking the partial derivative of a vector or tensor component gives it a second index—to show the variable with which the component is being differentiated. Ricci represented the partial derivative of a vector simply by adding another index, but today, the new index is indicated with a comma to show it’s a derivative. So, the partial derivative of *u*^**μ**^ is represented as

::: {.displayeq}

$$\frac{\partial u^{\mu}}{\partial x^{\lambda}}\equiv u^{\mu}_{,\lambda}.$$

:::

A semicolon is often used to designate the *covariant* derivative:

::: {.displayeq}

$$u^{\mu}_{;\lambda}=u^{\mu}_{,\lambda}+\Gamma^{\mu}_{\sigma\lambda}u^{\sigma}.$$

:::

I’ve shown this equation just to give you a visual, so the details are not important—except to say that there’s a natural extension to covariant derivatives of any tensor, not just vectors. The key thing is that it’s a tensor— so its value is invariant under the relevant coordinate transformations. In other words, you get the same result when you transform to new coordinates and take the covariant derivative of the transformed component *u*^**μ′**^ with respect to *x*^**λ′**^.

In Cartesian coordinates, the difference between partial and covariant derivatives disappears in flat spaces and space-times. This is another example of the way distinctions that are important in curved spaces disappear in flat space: in the Euclidean vector analysis we learn at school, there’s no need to talk about covariant derivatives, just as there’s no need to worry about the position of the indices on vectors.

## NOBODY CARED!

<!--p273-->
People had been studying invariance and differential geometry for years when Ricci brought it all together in tensor analysis—his “absolute differential calculus.” He drew on some of these earlier researchers—chiefly Gauss, Riemann, and Christoffel, but also others such as Sophus Lie, whose work on groups and invariance is still important, and the renowned differential geometer, Eugenio Beltrami, who’d been Ricci’s professor when he was a student at Bologna.

When Ricci entered some of his papers on tensors for Italy’s Royal Mathematics Prize in the late 1880s, Beltrami was a judge. Speaking on behalf of the judging committee, he admired Ricci’s mathematical virtuosity, but he wondered if the effort that had gone into creating this new calculus would ever be repaid by sufficiently fruitful applications—applications that could not be made using existing methods.[^ch11n24] He rather seemed to doubt it—just as William Thomson and Arthur Cayley could see no benefit in whole-vector analysis over separate component calculations. (The vector wars were going on in Britain at the very same time as Beltrami’s pronouncement about tensors in Italy.) But just as Maxwell had argued that the importance of whole vectors in physics was the physical insight they offered, so Ricci would later write that when it came to understanding curved *n*-dimensional surfaces and spaces, his calculus and its notation “contribute not only to the elegance, but also to the agility and clarity of the demonstrations and conclusions.”[^ch11n25]

Back in the 1880s, though, it must have seemed to Ricci—who still hadn’t got his promotion to professor—that for all the promise of his brilliant student years, he would forever go unrecognised and unfulfilled.

<!--stats: p=117 fig=1 eq=33 note=0-->
