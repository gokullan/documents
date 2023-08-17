Machine Learning

-   Prototype in Octave first before migrating to other languages

-   Definitions

    -   1:
    -   2:

-   Supervised learning

    -   "right answers" given
    -   Regression -- predict continuous valued output (eg: price)
    -   Classification -- discrete valued output (eg: malignant or
        benign)
    -   How to handle infinite number of features? Support Vector
        Machine

-   Unsupervised learning

    -   Given dataset (no labels or no idea about effect of variables in
        the data), is it possible to find some structure in the data?

    -   No feedback

    -   Clustering

        -   "Data lives in clusters"
        -   Eg: Google news stories -- looks at thousands of news
            stories across the web and groups them into related clusters
        -   Other eg: Computer clustering (data centres), Social network
            analysis, maket segmentation, astronomical data

    -   Cocktail party algorithm

        -   Mixed audio -\> Cocktail Party Algorithm -\> ("Mixture of 2
            audio sounds", Output_1, Output_2 \... )
        -   one line of code in Octave (using svd -- singular value
            decomposition)

Linear Regression

-   Notations

    -   m: \# of training examples
    -   x: input variables (features)
    -   y: output variables (target)
    -   (x^(i)^, y^(i)^): i^th^ training example
    -   hypothesis function (mapping from x to y):
        ![](media/image1.svg){width="1.22323in" height="0.17795in"}
        (![](media/image2.svg){width="0.21575in" height="0.1878in"} :
        parameters)
    -   

-   Cost function ![](media/image3.svg){width="0.71417in"
    height="0.20787in"}

    -   ![](media/image4.svg){width="1.54252in" height="0.3122in"} (find
        the parameters that minimize
        J)![](media/image5.svg){width="2.74961in" height="0.53228in"}
        (squared error function)

(![](media/image6.svg){width="0.09685in" height="0.39331in"} is chosen
for mathematical convenience -- see gradient descent)

-   -   ![](media/image7.svg){width="0.45512in" height="0.20787in"} vs.
        ![](media/image8.svg){width="0.71417in" height="0.20787in"}

        -   For every pair ![](media/image9.svg){width="0.58701in"
            height="0.20787in"}, there exists a corresponding line
            (hypothesis ![](media/image10.svg){width="0.45512in"
            height="0.20787in"}) in the x-y plane.

-   Gradient descent

    -   To solve a general minimization problem -

![](media/image11.svg){width="2.47795in" height="0.3122in"}

-   -   Algorithm

Repeat until convergence {

![](media/image12.svg){width="1.85433in" height="0.45433in"} for i=0 and
i=1 SIMULTANEOUSLY}

![](media/image13.svg){width="0.11693in" height="0.0878in"} is the
learning rate ("how big do you want your steps to be as you move down
the hill (update the parameters) " - see pdf)

-   -   Intuition of the derivative term
    -   Effects of increasing or decreasing
        ![](media/image14.svg){width="0.11693in" height="0.0878in"}
    -   With ![](media/image14.svg){width="0.11693in" height="0.0878in"}
        fixed, as ![](media/image15.svg){width="0.15315in"
        height="0.18071in"} approaches a local minimum, the gradient
        descent automatically reduces the step size (since the
        derivative term will automatically get smaller) .

-   ![](media/image16.svg){width="3.79213in" height="0.59528in"}

![](media/image17.svg){width="3.11142in" height="0.58071in"}

![](media/image18.svg){width="2.88031in" height="0.53228in"}

![](media/image19.svg){width="2.03504in" height="0.53228in"}

-   ![](media/image20.svg){width="3.79213in" height="0.59528in"}

![](media/image21.svg){width="3.09409in" height="0.54606in"}

![](media/image22.svg){width="2.39252in" height="0.54606in"}

-   Cost function is always convex (bowl-shaped) for linear regression,
    (i.e.), there is only 1 minima
-   Batch gradient descent -- looks at all examples in the training set
    at every step

Linear Algebra

-   Matrix

    -   rectangular array of numbers
    -   ![](media/image23.svg){width="0.48779in" height="0.15039in"}
        refers to the set of all mxn matrices whose elements belong to
        the set of real numbers

-   Vector

    -   nx1 matrix (row matrix)
    -   Also called 'n-dimensional vector';
        ![](media/image24.svg){width="0.22874in" height="0.13937in"}

Linear Regression with Multiple variables

-   n: \# of features
-   ![](media/image25.svg){width="0.28504in" height="0.19882in"}:
    features of ith training example
    (![](media/image26.svg){width="1.72323in" height="0.23346in"})
-   ![](media/image27.svg){width="0.28504in" height="0.29882in"}: jth
    feature of ith training example
-   ![](media/image28.svg){width="3.16693in" height="0.20787in"}

Let ![](media/image29.svg){width="0.79409in" height="1.29252in"}, where
![](media/image30.svg){width="0.55157in" height="0.1752in"};
![](media/image31.svg){width="0.76063in" height="1.05984in"}

Both vectors are 0-indexed and ![](media/image32.svg){width="0.96299in"
height="0.22165in"}

Thus ![](media/image33.svg){width="1.03976in" height="0.22047in"}

-   Gradient descent for multiple variables

-   Feature scaling

    -   Easier for gradient descent to find it s way to the global
        minimum if all features take on a common range of values

("θ will descend quickly on small ranges and slowly on large ranges")

-   -   Usually we the following range is preferred:
        ![](media/image34.svg){width="1.03504in" height="0.1748in"}

Note: Anything close to this is also accepted

-   -   Mean Normalization: ![](media/image35.svg){width="4.03701in"
        height="0.50157in"}

-   Influence of learning rate ![](media/image14.svg){width="0.11693in"
    height="0.0878in"}

    -   If ![](media/image14.svg){width="0.11693in" height="0.0878in"}
        is sufficiently small, ![](media/image36.svg){width="0.35315in"
        height="0.19252in"} always decreases after every iteration of
        gradient descent
    -   If ![](media/image14.svg){width="0.11693in" height="0.0878in"}
        is large, then it may "overshoot and diverge, therby increasing
        ![](media/image37.svg){width="0.35315in" height="0.19252in"}
        after every iteration".
    -   Plot ![](media/image37.svg){width="0.35315in"
        height="0.19252in"} vs. #iterations to declare convergence as
        well as to find a suitable learning rate.

-   Features and Polynomial Regression

    -   It is not required to only use the features provided. New
        features could also be defined using the existing ones.

        -   Eg: Assume x1 = frontage and x2 = depth; one could define a
            new feature, area (=frontage x depth), that would be better
            suited for predicting prices. (Insight into problem is
            helpful in this case)

    -   Assume you want to fit a quadratic or cubic polynomial to your
        data. Higher order (order \> 1) terms can each be treated as
        feature and so the same linear regression model can be used for
        this purpose also.

        -   Note that feature scaling is very important when trying to
            fit higher order polynomials to data.

-   Normal Equation method

    -   Explicitly finding the minimum of
        ![](media/image37.svg){width="0.35315in" height="0.19252in"} (by
        setting the derivatives to 0)
    -   No need of feature scaling
    -   ![](media/image38.svg){width="2.27598in" height="0.24055in"},

where ![](media/image39.svg){width="2.90984in" height="1.18425in"}

-   -   Gradient descent vs. Normal equation

![](media/image40.png){width="6.19291in" height="1.60984in"}

-   -   \<\>

Vectorization

![](media/image41.png){width="6.69291in" height="2.13976in"}

Logistic Regression

-   Does feature scaling affect ![](media/image10.svg){width="0.45512in"
    height="0.20787in"} ?
-   Linear regression is not suitable for classification problems
-   0 -- negative class; 1 -- positive class (for binary classification)
-   For a given feature of a training example,
    ![](media/image25.svg){width="0.28504in" height="0.19882in"}, the
    corresponding ![](media/image42.svg){width="0.26142in"
    height="0.22047in"} is called the label of that training example.
-   For logistic regression, we want
    ![](media/image43.svg){width="1.15512in" height="0.19252in"}.

-   Hypthesis representation

    -   For linear regression, we had,
        ![](media/image33.svg){width="1.03976in" height="0.22047in"}
    -   For logistic regression,
        ![](media/image44.svg){width="1.27874in" height="0.22047in"},
        where ![](media/image45.svg){width="1.26417in"
        height="0.40866in"} is called the sigmoid or logistic function
    -   Here ![](media/image10.svg){width="0.45512in"
        height="0.20787in"} gives the probability that the output y=1
        (positive class), given features
        ![](media/image46.svg){width="0.10118in" height="0.0878in"} and
        parameters ![](media/image47.svg){width="0.0878in"
        height="0.1378in"}. Thus,
        ![](media/image48.svg){width="1.80118in" height="0.20787in"}
    -   Also, note that for binary classification:

![](media/image49.svg){width="2.74882in" height="0.19252in"}

-   Decision Boundary

    -   Let us assume that,

![](media/image50.svg){width="2.62953in" height="0.59528in"}

-   -   From ![](media/image51.svg){width="0.34331in"
        height="0.20787in"}, it can be seen that for
        ![](media/image52.svg){width="0.97047in" height="0.20787in"},
        ![](media/image53.svg){width="0.44528in" height="0.15433in"},
        (i.e.), ![](media/image54.svg){width="0.67598in"
        height="0.19882in"} (this is the decision boundary)
    -   The region obtained from the previous inequality is the region
        where y=1, in a plane where (assuming we have 3 features, where
        x0 is always 1) x1 and x2 represent the x and y-axis
        respectively.
    -   Note that the decision boundary is a property of the hypothesis
        and the parameters of the hypothesis, not the dataset.

![](media/image55.png){width="6.27087in" height="2.57283in"}

Neural Networks

-   Motivation

    -   To come up with a non-linear hypothesis with large number of
        features\* is computationally intensive to do using logistic
        regression
    -   \*say the input is a 100x100 image (10^4^ pixels); then,
        including quadratic terms in our hypothesis, we would have
        (10^4^ x 10^4^)/2 features (0.5 x 10^8^ = 5 x 10^7\ ^= 50
        million)

-   Neurons

    -   Dendrites = input wires
    -   Cell body = processing centre
    -   Axon = output wire
    -   

-   Model representation

    -   Layer 1 -- input layer ("dendrites")
    -   Final layer -- output layer
    -   Middle layers -- hidden layers
    -   Activation function -- ![](media/image51.svg){width="0.34331in"
        height="0.20787in"} (sigmoid function)
    -   Weights -- parameters ![](media/image47.svg){width="0.0878in"
        height="0.1378in"}
    -   The value of a node ![](media/image56.svg){width="0.07165in"
        height="0.14528in"} in a given layer
        ![](media/image57.svg){width="0.07874in" height="0.16693in"} is
        denoted as ![](media/image58.svg){width="0.16142in"
        height="0.23701in"} and is given by

![](media/image59.svg){width="3.46063in" height="0.2752in"}, where

![](media/image60.svg){width="3.02047in" height="0.94409in"} represents
the parameters required to map layer
![](media/image61.svg){width="0.07874in" height="0.16693in"} to layer
![](media/image62.svg){width="0.41063in" height="0.1685in"} and
![](media/image63.svg){width="0.15039in" height="0.14252in"} denoted the
number of nodes in layer ![](media/image61.svg){width="0.07874in"
height="0.16693in"}.

-   -   It can be seen that the dimension of
        ![](media/image64.svg){width="0.15591in" height="0.17126in"} is
        ![](media/image65.svg){width="1.10512in" height="0.19961in"} (+1
        is due to the bias)

![](media/image66.png){width="6.69291in" height="2.30354in"}

![](media/image67.png){width="6.69291in" height="3.7626in"}

-   Overfitting

    -   Hypothesis has high variance -- we don't know much about the
        problem to restrict ourselves to some bias; so we have a large
        hypothesis space
    -   This happens when the number of features is large (?)

VC Dimension

-   <https://datascience.stackexchange.com/questions/32557/what-is-the-exact-definition-of-vc-dimension>

Bias-Variance Tradeoff

-   Bias -- The inability of a ML algorithm to capture the true
    underlying relationship between the features and the output (eg:
    using straight lines (linear regression) to fit a quadratic
    relationship)
-   Variance -- The difference in fits between datasets (low variability
    =\> consistent predictions across different datasets; predictions
    may be good, but not great, if the model has high bias)

![](media/image68.png){width="6.69291in" height="3.40709in"}

![](media/image69.png){width="6.69291in" height="3.43819in"}

Decision Trees

-   Gini Impurity --
    <https://towardsdatascience.com/gini-impurity-measure-dbd3878ead33>

-   Entropy

    -   <https://stats.stackexchange.com/questions/95261/why-am-i-getting-information-entropy-greater-than-1>

    -   Information Gain vs. KL-Divergence

        -   <https://stats.stackexchange.com/questions/103175/information-gain-is-kl-divergence>
        -   <https://stats.stackexchange.com/questions/13389/information-gain-mutual-information-and-related-measures>

    -   <https://towardsdatascience.com/entropy-and-information-gain-in-decision-trees-c7db67a3a293>

    -   

-   Algorithm

Support Vector Machines

-   Source:
    <https://shuzhanfan.github.io/2018/05/understanding-mathematics-behind-support-vector-machines/>

-   Pre-requisites:

    -   Equation of a plane
    -   What do positive and negative values output by the LHS of the
        standard equation of a plane (for a given point) mean?
    -   Shortest distance from a point to a plane --
        <https://math.stackexchange.com/questions/1210545/distance-from-a-point-to-a-hyperplane>

-   It is a supervised learning algorithm that (for classification
    problems) aims to find the hyperplane (boundary) that has the widest
    "margin" of separation from the data points, (i.e.), all points
    above the margin are points from the positive class and those below
    are from the negative class

-   Margin referes to the shortest "distance" between all the data
    points and the hyperplane. (distance refers to the perpendicular (or
    shortest) distance measure)

-   In order to obtain such a hyperplane, the distance from all points
    to the plane must be \>= the margin distance. (By definition of a
    margin, there cannot be any point that has lesser distance (than the
    margin distance) from the hyperplane)
-   Thus, the following constraint should be satisfied by the required
    hyperplane --

![](media/image70.png "texmaths"){width="1.52126in" height="0.45669in"},
where M is the margin length

-   The above constraint is only for those hyperplanes that give correct
    classification. But how do we know if a hyperplane classifies the
    data points correctly or not? We can incorporate this information
    into the above constraint as well. Before that, let's define y~i~,
    (the label for the sample x~i~) to be 1 for the positive class and
    -1 for the negative class.

-   Now our constraint becomes
    ![](media/image71.png "texmaths"){width="1.47756in"
    height="0.45669in"}

    -   The LHS will be negative when the point is incorrectly
        classified by the hyperplane

-   Since we are looking to maximize the margin, all those hyperplanes
    that gave an incorrect classification will be taken out of the
    picture since they output negative values in the LHS of the
    constraint.

-   To simplify things, let's take
    ![](media/image72.png "texmaths"){width="0.28976in"
    height="0.19252in"} to the RHS and set
    ![](media/image73.png "texmaths"){width="0.90512in"
    height="0.19252in"}. Thus we have our final constraint
    ![](media/image74.png "texmaths"){width="1.32874in"
    height="0.19252in"}

-   Next, we determine the length of the margin (more specifically, we
    will find the length of the maximum width separating the 2 classes =
    2 x margin_length) graphically and use the above constraint in the
    expression that we obtain.

Boosting

-   <https://towardsdatascience.com/boosting-algorithms-explained-d38f56ef3f30>
-   <https://www.mygreatlearning.com/blog/adaboost-algorithm/>

Backpropagation

-   Matrix Calculus --
    <https://math.stackexchange.com/questions/1621948/derivative-of-a-vector-with-respect-to-a-matrix>

CNN

-   <https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53>

-   Application of Computer Vision

    -   Image classification
    -   Object detection (drawing a bounding box around the required
        object + finding out it's position)
    -   Neural style transfer ("re-paint" an image according to a given
        style)

-    Why CNN and not normal neural networks?

    -   Say, we need to detect features of a 1000 x 1000 color image,
        (i.e.), 10^6\ ^x 3 pixels
    -   If the 2^nd^ layer in the NN has 1000 nodes, then the total
        number of weights required will be 1000 x \[(10^6^ x 3)+1\] \~ 3
        billion weights and thus it is not feasible to train it due to
        the heavy computational and memory requirements

-   Edge detection

    -   The filter matrix used for convolution with the image is usually
        3x3 with fixed coefficients.
    -   These weights can be learned using backpropagation (instead of
        being fixed), to get an image in which the edges are detected
        the best.
    -   Convolution of an n x n image with an f x f filter (f is almost
        always odd) results in a matrix of dimension (n-f+1) x (n-f+1)
        (**"valid convolution"**)

-   Padding

    -   To prevent shrinking of image size at successive layers
    -   To prevent loss of information in the "corner" pixels
    -   If the amount of padding is p, then the size of the resultant
        matrix (after convolution) is (n+2p-f+1) x (n+2p-f+1)
    -   If (n+2p-f+1) = n (i.e.), the size of the resultant matrix is
        the same as that of the image, then p = (f-1)/2 (**"same
        convolution"**)

-   Strided convolutions

    -   Stride = 2 =\> shift the filter matrix by 2 positions for every
        set of convolution
    -   Dimension of resulting matrix using strides =
        ![](media/image75.svg){width="1.47165in" height="0.48031in"}

-   Cross-correlation vs. convolution

    -   Convolution involves flipping the filter matrix both
        horizontally and vertically and then computing the product-sum

        -   take the horizontal mirror-image
            (![](media/image76.svg){width="1.25709in"
            height="0.20394in"}), then the vertical mirror-image

(![](media/image77.svg){width="1.24488in" height="0.20394in"})

-   -   If no filp is involved, the operation is technically called
        "cross-correlation"
    -   Convolution follows the associative property: (A\*B)\*C =
        A\*(B\*C), but this is not of much importance in computer
        vision.
    -   In CV, when we refer to "convolution", it actually means
        cross-correlation

-   Convolution over volume

    -   The dimension of an RGB image is represented as: height x width
        x 3, where 3 refers to the number of channels (sometimes called
        depth)
    -   To convolve over sunch an image, the filter should also have the
        same number of channels, (i.e.) f~1~ x f~2~ x 3 (f~1~ -- height,
        f~2~ - width of filter matrix)
    -   Each channel is convolved with its corresponding filter channel
        and the output for a given location (or pixel) is the sum of the
        outputs of all channels for that location.
    -   The output is will be of dimension (n-f+1) x (n-f+1) x n~c~',
        where n~c~' is the number of filters being used, (i.e.),
        different filters can be applied to the image and their
        corresponding outputs will be stacked in the final output.

![](media/image78.png){width="6.69291in" height="3.03268in"}

![](media/image79.png){width="6.69291in" height="4.03464in"}

-   One layer of a CNN

![](media/image80.png){width="6.44291in" height="3.60551in"}

-   Why convolution?

    -   Parameter sharing

        -   The same filter is used to detect a particular feature for
            all pixel positions

    -   Sparcity of connections

        -   The output of a particular pixel depends only on its
            neighbours and not on other pixels

    -   Translation invariance

        -   A "cat" image shifted by a few pixels would also be labelled
            correctly

-   Note

    -   Typically, as we move across the different layers (from left to
        right), the height and width decrease, while the number of
        channels increase.

-   Popular CNNs

    -   LeNet

        -   \~60K parameters
        -   used sigmoid/tanh activation (instead of ReLu)
        -   non-linearity after pooling
        -   involved computing convolution differently for a filter with
            n~c~ channels to reduce computational cost

![](media/image81.png){width="6.69291in" height="3.77087in"}

-   -   AlexNet

        -   \~60M parameters
        -   involves Local Response Normalization
        -   parallel GPU execution

![](media/image82.png){width="6.69291in" height="3.7252in"}

-   -   VGG-16 (VGG-19)

        -   \~138M parameters

        -   noted for simplicity

            -   fixed convolution and pooling parameters
            -   number of filters doubles for every set of convolution

![](media/image83.png){width="6.69291in" height="3.78268in"}

-   ResNets

    -   Difficult to train very deep NNs due to vanishing/exploding
        gradient problems

Feature Extraction ?

Support Vector Machines

-   Cost function of Logistic Regression vs. SVM

![](media/image84.png){width="6.69291in" height="2.34646in"}

-   \<\>

RNN

-   Mitesh Khapra Deep Learning series (NPTEL) --
    <https://youtube.com/playlist?list=PLyqSpQzTE6M9gCgajvQbc68Hk_JKGBAYT>
-   LSTM -- <http://colah.github.io/posts/2015-08-Understanding-LSTMs/>
-   GRU --
    <https://towardsdatascience.com/understanding-gru-networks-2ef37df6c9be>

Generative Modeling

-   In discriminate modeling, we do classification, (i.e.), we finding
    P(C/X) directly by learning the mapping. Here X is the input
    feature, C is the class label

-   In generative modeling, we want to do classification (or some other
    task) by finding out P(X/C) first. (How likely is it that X *comes
    from* class C as opposed to how likely is it that X *belongs to*
    class C)

    -   If we want to do classification, we can apply Bayes Theorem and
        find out P(C/X)

-   How to find P(X/C)?

    -   Assume X as the white blood cell count and C as the class label
        for cancer (C=0 indicates no cancer)
    -   We also assume that P(X/C) is normally distributed, (i.e.), we
        are performing Gaussian Generative modeling
    -   Thus, we need to generate 2 distributions -- P(X/C=0) and
        P(X/C=1)
    -   For each distribution, we need 2 parameters -- the mean and
        standard deviation
    -   There is a way to estimated these parameters (MLE -- Maximum
        Likelihood Estimation) for each distribution by using the
        training samples of the respective classes (refer slides for the
        derivation and formula) and we end up with the required
        distributions

Autoencoder

Techniques to prevent Overfitting in CNNs

Validation Set

-   This is used after training and before testing
-   It is used to check if the model has overfit the training data. (If
    training accuracy is high and validation accuracy is much lower,
    then overfitting has happened)
-   In case of overfitting (see graph below), suitables changes are made
    to the training process and the model is run on the validation test
    set again.
-   This process repeats until the model generalizes well, i.e, until
    validation accuracy is high and not much lesser than training
    accuracy.

![](media/image85.png){width="4.75in" height="3.9689in"}

1.  Image Augmentation

-   -   Apply transformations such as rotation, zoom, flip, etc., to
        training images and add the transformed images to the training
        samples as well so that the model can generalize well on images
        it has not seen before.

1.  Dropout

-   -   Randomly "turn off" some neurons in the network during training

1.  Early stopping

Reading Materials --
<https://hackernoon.com/memorizing-is-not-learning-6-tricks-to-prevent-overfitting-in-machine-learning-820b091dc42>

Expectation Maximization --
<https://www.kaggle.com/code/charel/learn-by-example-expectation-maximization/notebook>

Overfitting-handling techniques

-   Holdout dataset (cross-validation)
-   Regularization
-   Data Augmentation

Transfer Learning

-   **Side-track**: Explanation-based neural network learning --
    multi-task learning -- better performance

-   Basic idea -- Taking a pre-trained neural network and tweak it to
    fit the new scenario, (i.e.), a neural network that has been trained
    on a large dataset can apply its knowledge to a dataset it has never
    seen before

-   Training

    -   Only the weights pertaining to the output layer of the
        pre-trained model must be changed. Other variables of the
        pre-trained model should be frozen (non-trainable).
    -   If we do not freeze the variables of the pre-trained model, the
        whole point of transfer learning is lost since our objective is
        to use the weights of the pre-trained model for our own training
        task.
    -   As an additional benefit, the training time is reduced
        significantly.

-   Tensorflow Hub -- Repository of pre-trained models

-   Sample Code

![](media/image86.png){width="6.69291in" height="3.64252in"}

-   

ML Implementation notes

-   [Jupyter Notebook Tricks](https://www.kaggle.com/code/tientd95/jupyter-notebook-tricks)

-   **Markdown**

    -   <https://www.markdownguide.org/cheat-sheet/>

    -   <https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/>

    -   ESC to enter command mode

        -   dd to delete a cell
        -   y to convert to python cell
        -   m to convert to markdown cell

    -   Enclose in \$ \<equation\> \$ to enter equations

    -   [Adding Emojis](https://stackoverflow.com/questions/50197537/jupyter-notebook-does-not-support-smileys-in-markdown-cells)
        -   Copy-paste from [Link 1](https://emojikeyboard.org/) or [Link 2](https://www.webpagefx.com/tools/emoji-cheat-sheet/)
        -   Use unicode (decimal form): &#2400;


## Matplotlib (`matplotlib.pyplot`)
> `import matplotlib.pyplot as plt`

-   ```python
    plt.figure(num, figsize=(width_inches, height_inches))
    plt.plot(x_values, y_values)
    plt.plot(x_values2, y_values2)
    # both of the above will appear in the same window
    plt.xlabel(<>)
    plt.ylabel(<>)
    plt.title(label=<>, fontsize=<>, color=<>)
    plt.show()
    ```

-  Adding legends
    ```
    plt.legend([<labels in the order in which they were plotted>])
    # OR
    plt.legend() # if label arguments are provided in plt.plot()
    ```

-   -   Other arguments for plt.plot()

        -   Use color, linestyle, marker arguments in plt.plot() (OR)
            Format string: '\[marker\]\[line\]\[color\]' (hex values can
            also be used for color)
        -   linewidth

-   -   plt.tight_layout() - to adjust padding
    -   plt.grid(True) -- to show grids on the plot

-   -   Style

        -   print(plt.style.available) -- to see the available
            (in-built) plot styles
        -   plt.style.use(\<style-name\>)
        -   plt.xkcd() \# in reference to xkcd comics

    -   plt.savefig('\<\>.png') \# to save a plot

    -   %inline ?

    -   color map ?

-   Using subplots

-   Histogram: `plt.hist(data, bins)`
    -   [Histogram plot from a list of strings](https://stackoverflow.com/questions/28418988/how-to-make-a-histogram-from-a-list-of-strings)

-   Bar graphs from dictionary
```py
D = {u'Label1':26, u'Label2': 17, u'Label3':30}
plt.bar(*zip(*D.items()))
plt.show()

```

-   Box-plot: `plt.boxplot(data)`


-   Categorical encoding --
    <https://towardsdatascience.com/categorical-encoding-using-label-encoding-and-one-hot-encoder-911ef77fb5bd>

-   Accessing drive files in Colab --
    <https://stackoverflow.com/questions/48376580/google-colab-how-to-read-data-from-my-google-drive>

    -   from google.colab import drive

drive.mount('/content/drive')
\# use '/content/drive/My Drive/filename'

### Seaborn
```python
import seaborn as sns
```
-   t-SNE plot
    ```python
    plt.figure(figsize=(16,10))
    sns.scatterplot(
        x="tsne-2d-one", y="tsne-2d-two",
        hue="y",
        palette=sns.color_palette("hls", 10),
        data=df_subset,
        legend="full",
        alpha=0.3
    )
    ```
    -   Here `y.shape=(len(y), 10)`
    -   The parameters `x`, `y` and `hue` refer to column name of the DataFrame `df_subset`
    -   [Reference](https://builtin.com/data-science/tsne-python)

##  Numpy and Pandas

[Tutorial](https://www.hackerearth.com/practice/machine-learning/data-manipulation-visualisation-r-python/tutorial-data-manipulation-numpy-pandas-python/tutorial/)

##   Numpy

-   Numpy slicing --
    <https://stackoverflow.com/questions/5347091/slicing-numpy-array-representing-nested-list>

    -   a = np.array(\[\[1,2,3\],\[4,5,6\],\[7,8,9\]\])

    -   a\[:, :1\] =\> \[\[1\],\[4\],\[7\]\]; a\[:, 0\] =\>
        array(\[1,4\])

        -   **Slicing syntax**: numpyArray**\[dim_1, dim_2, \... ,
            dim_n\]**, where dim_i can be of the form **start_index
            : end_index : step**
        -   **Note: **Only numpy arrays (not lists) can be sliced
            using commas as above
-   np.where
```py
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# say we want the indices of those elements
# where the 2nd column is divisible by 2
# and the 3rd column is divisible by 3
np.where(
    # note the brackets!
    (
        (a[:,1] % 2 == 0) &
        (a[:,2] % 3 == 0)
    )
)  # output [0, 2]
```
-   [Thoughts on appending to a Numpy array](https://stackoverflow.com/questions/568962/how-do-i-create-an-empty-array-and-then-append-to-it-in-numpy)

-   np.random.uniform(low, high, size)

-   np.random.normal(mean, sd, size)

-   np.random.randint(low, high, size) -- generates a random integer
    in the range \[low, high)

-   np.append()

-   np.stack() --->

-   np.hstack()

-   np.concatenate()

-   np.start() --->

-   np.array vs. np.ndarray()

-   `np.swapaxes(arr, axis_1, axis_2)` - return a *view* is arr is an *ndarray* (for NumPy >= 1.10)
    -   Changes made to the view will affect the original array

-   np.ndarray.item()

-   np.cumsum() --->

-   np.matmul()

-   <https://stackoverflow.com/questions/24439137/efficient-way-for-appending-numpy-array>

-   Saving and loading numpy arrays
```py
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
np.save("myarray.npy", a)
a_copy = np.load("myarray.npy")
```

## Pandas

-   Creating a dataframe

    -   data = \[\[item1a, item1b\], \[item2a, item2b\], \...\]
    -   df = pd.DataFrame(data, columns = \['col1', 'col2'\])

-   To access column names: df.columns

-   Each row in a DataFrame is a **Series** (?)

-   Count the different attributes of a column:
    a\["col_label"\].**value_counts()**

-   Accessing particular row(s)/ columns(s)

    -   <https://stackoverflow.com/questions/31593201/how-are-iloc-and-loc-different>
    -   <https://stackoverflow.com/questions/45983801/pandas-iloc-vs-direct-slicing>
    -   a.loc\[index_label,:\] (OR) a.iloc\[:, col_name\]
    -   a.iloc\[index, :\] (OR) a.iloc\[:, col_index\] (use .iloc,
        .iloc to access values)

-   Changing index

    -   <https://stackoverflow.com/questions/19851005/rename-pandas-dataframe-index>

-   Adding a row
```py
df.loc[len(df)] = [v1, v2, v3, ...]
```

-   Adding a column

-   Deleting a row

-   Deleting a column

-   Get datatype of a column

    -   a.drop(\['col_name1', 'col_name2', \...\])

-   Iterate over rows

    -   for index, row in df.iterrows(): \<\>
    -   <https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas>

-   -   Sorting

        -   df.sort_values(by=\['col1', 'col2', ...\], ascending=True)

-   -   Grouping

        -   Grouped = Df.groupby(by='col')

        -   Access a particular group

            -   grouped.get_group(group_name)

                -   Group names are available in grouped.groups

        -   Iteration

> For name, group in grouped.\_\_iter\_\_():

> pass

-   -   -   \<\>

    -   Index

        -   Replace current index with default 0-based indexing

            ?-   Df.reset_index(drop=True)

                -   drop=False retains the old index as a column in the
                    dataframe

-   -   List non-numeric columns

        -   num_cols = df.\_get_numeric_data().columns

> list(set(df.columns) -- set(num_cols))

-   -   Handling datetime values

        -   Time difference between 2 columns

            -   ***pd.Timedelta(t1 -- t2).total_seconds() / 3600***,
                where ***t1*** and ***t2*** are Datetime objects
            -   <https://stackoverflow.com/questions/22923775/calculate-time-difference-between-two-pandas-columns-in-hours-and-minutes>

        -   Datetime index

            -   <https://towardsdatascience.com/tips-on-working-with-datetime-index-in-pandas-2bcedf956d70>

-   -   Handling null values

        -   NaN vs. NaT vs. None

            -   <https://dev.to/discdiver/the-weird-world-of-missing-values-in-pandas-3kph>

        -   Count all null values: ***df.isna().sum()*** (OR)
            ***df\['col_name'\].isna().sum()***

        -   Check for null values

            -   pd.isnull(df.iloc\[0\]\['col_name'\])
            -   <https://stackoverflow.com/questions/49435317/how-to-test-if-a-variable-is-pd-nat>

        -   Delete rows with null values: df.dropna(axis=0)

-   Normal Distributions

    -   **scipy.stats.norm**(mean, sd).pdf(data_point)

-   Loading images from a folder --
    <https://stackoverflow.com/questions/30230592/loading-all-images-using-imread-from-a-given-folder>
-   Matplotlib --
    <https://youtube.com/playlist?list=PL-osiE80TeTvipOqomVEeZ1HRrcEvtZB>\_
-   Automate data fetching (44)
-   Using hash to split train and test data (50)
-   Stratified sampling (51)
-   Data cleaning (61) (start from 267)

## Sklearn
-   Splitting into training and testing
    ```python
    from sklean.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.7, random_state=42
        )
    ```

-   Shuffling dataset
    ```python
    from sklearn.utils import shuffle
    X, y = shuffle(X, y)
    ```
    [Reference](https://stackoverflow.com/questions/35076223/how-to-randomly-shuffle-data-and-target-in-python)

-   Scikit Linear Regression
    -   [Ref. 1](https://www.kdnuggets.com/2019/03/beginners-guide-linear-regression-python-scikit-learn.html)
    -   [YouTube playlist](https://youtube.com/playlist?list=PL5-da3qGB5ID7YYAqireYEew2mWVvgmj6)

-   Feature scaling
        -   from sklearn.preprocessing import MinMaxScalar
        -   scalar = MinMaxScalar()
        -   X_scaled = scalar.fit_transform(X)
        -   [https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html)

-   [ValueError: Found array with dim 3. Estimator expected <= 2.](https://stackoverflow.com/questions/34972142/sklearn-logistic-regression-valueerror-found-array-with-dim-3-estimator-expec)

    ```python
    nsamples, nx, ny = train_dataset.shape
    d2_train_dataset = train_dataset.reshape((nsamples,nx*ny))
    ```

<https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/load_data/images.ipynb#scrollTo=oV9PtjdKKWyI>

**glob** -- to match files/folders that follow a specified pattern

-   glob patterns are not the same as regex; regex are more powerful
-   Source: <https://youtu.be/Vc5kGYty18k>
-   Explore more on \*/ and \*\*/

import glob

png_files = glob.**glob**("path/\*.png") \# return a list of filenames
that match this pattern

\# returns an iterator

\# used in cases where you do not want to/ cannot store the file names
in main memory

it = glob.**iglob**("path/\*.png")

\# recursive searching

\# \*\*/ is used to match zero or more subdirectories

glob.glob("path/**\*\*/**\*.png", **recursive=True**)

**os**

-   Refer \*\*/College/Machine_Learning/prerequisites_python/

-   mkdir() vs. makedirs(); rmdir() vs. removedirs()

-   os.listdir("\<dir_path\>") lists filenames in the directory

-   os.path

    -   .join
    -   .basename
    -   .dirname (get the parent-directory name)
    -   .split (combines output of .basename and .dirname)
    -   .exists
    -   .isdir
    -   .isfile
    -   .splitext -- to get filename without extension
        (\...splitext\[0\])

-   os.walk(directory)

    -   for root, dirs, files in os.walk(directory):

-   os.path.getsize("\<filename\>") -- to get file size

\# do something

**pathlib**

-   Reference -- <https://youtu.be/iqZ2V8qTYq8>
-   Cheat sheet at \*\*/College/Machine_Learning/prerequisites_python
-   pathlib.Path("\...").with_suffix('.txt') -- replaces existing suffix
    with the new suffix

datetime

generators and iterators

Pillow (import PIL)

-   PIL.Image.open("filepath/../sample.jpg")

## pickle

```python
import pickle

# save an object
fileObj = open('data.obj', 'wb')
pickle.dump(exampleObj,fileObj)
fileObj.close()

# load an object
fileObj = open('data.obj', 'rb')
exampleObj = pickle.load(fileObj)
fileObj.close()
```

**open-cv** (import cv2)

-   cv2.imread("filepath/../sample.jpg") \# reads in BGR format

    -   <https://stackoverflow.com/questions/54959387/rgb-image-display-in-matplotlib-plt-imshow-returns-a-blue-image>

        -   Read grayscale images: cv2.imread("file",
            cv2.IMREAD_GRAYSCALE)

-   cv2.resize(img, (width, height)) \# returns image

subprocess

-   run external script in Python

    -   result = subprocess.run(\['program.sh', 'arg1', 'arg2', ..,\],
        capture_output=True, text=True)

> print(result.stdout, result.stderr)

-   -   [*https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output*](https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output)
    -   os.system('command to run in cmd')

Create a custom data generator

-   <https://github.com/anujshah1003/custom_data_generator>

-   Use case: When you have --

    -   A csv file which maps the image filenames to their classes
    -   An image directory containing all images

-   Steps

    -   create_samples(csv_file)

        -   return a list of the form \[\[image_name1, label1\],
            \[image_name1, label1\], \... \[image_name_n, label_n\]\]

    -   data_generator(samples, image_dir)

        -   a generator function which takes samples (as described
            above) and 'yields' a generator

multiprocessing

-   <https://www.digitalocean.com/community/tutorials/python-multiprocessing-example>
-   <https://colab.research.google.com/github/pnavaro/python-notebooks/blob/master/notebooks/10-Multiprocessing.ipynb>

## `random`
-   To select `n` distinct random elements from a list
```py
import random
random.sample(myList, n)
```

Misc

-   use %timeit module to measure the time
-   <https://towardsdatascience.com/latest-winning-techniques-for-kaggle-image-classification-with-limited-data-5259e7736327>
-   <https://www.kaggle.com/code/vbookshelf/python-generators-to-reduce-ram-usage-part-2/notebook>
-   wandb API key: 6126efc3a7a9a191e68b2067a05f874ac618d6a1
-   <https://www.kaggle.com/code/akarshu121/document-image-classification-with-docformer/notebook>

Tensorflow

ML algorithm -- a function that can tune variables in order to correctly
map the inputs to their corresponding outputs

-   [Should you use `keras.engine`?](https://stackoverflow.com/questions/72909937/why-is-there-no-documentation-for-keras-engine)

-   Fashion MNIST training using vanilla neural network --
    <https://colab.research.google.com/github/tensorflow/examples/blob/master/courses/udacity_intro_to_tensorflow_for_deep_learning/l03c01_classifying_images_of_clothing.ipynb#scrollTo=-KtnHECKZni>\_

-   Fashion MNIST training using CNN --
    <https://colab.research.google.com/github/tensorflow/examples/blob/master/courses/udacity_intro_to_tensorflow_for_deep_learning/l04c01_image_classification_with_cnns.ipynb>

-   model.summary()

![](media/image87.png){width="6.69291in" height="2.35984in"}

-   Loading images --
    <https://www.tensorflow.org/tutorials/load_data/images>

-   tensorflow.data.Dataset.load()

    -   <https://www.tensorflow.org/datasets/api_docs/python/tfds/load>
    -   <https://stackoverflow.com/questions/58683675/how-to-manipulate-tfds-load-datasets-correctly-in-tensorflow-2-x>

-   When choose functional API over sequential API? (multiple inputs and
    outputs?)

-   Reading image dataset --
    <https://stackoverflow.com/questions/62654715/how-to-read-images-dataset-in-google-colab-for-deep-learning>

Image classification from scratch --
<https://keras.io/examples/vision/image_classification_from_scratch/>

Losses (tf.keras.losses)

-   SparseCategoricalCrossEntropy()

    -   <https://datascience.stackexchange.com/questions/73093/what-does-from-logits-true-do-in-sparsecategoricalcrossentropy-loss-function>

-   Linear activation

-   Softmax

-   Understanding losses --
    <https://gombru.github.io/2018/05/23/cross_entropy_loss/>

-   <https://levelup.gitconnected.com/killer-combo-softmax-and-cross-entropy-5907442f60ba>

Loading images

-   <https://www.tensorflow.org/tutorials/load_data/images>
-   tf.keras.utils.get_file(

)

-   \<\>

tf.data.Dataset

-   skip and take --
    <https://stackoverflow.com/questions/48213766/split-a-dataset-created-by-tensorflow-dataset-api-in-to-train-and-test>
-   <https://www.tensorflow.org/api_docs/python/tf/data/Dataset>

tf.keras.layers.Rescaling

Looping under model.fit()

-   <https://stackoverflow.com/questions/50448743/is-it-logical-to-loop-on-model-fit-in-keras>
-   <https://github.com/keras-team/keras/issues/2708>

Grayscale to RGB

-   <https://stackoverflow.com/questions/70876871/transfer-learning-mobilenet-with-dataset-that-contains-grayscale-images>
-   

Data Augmentation

-   <https://www.tensorflow.org/tutorials/images/data_augmentation>
-   <https://www.tensorflow.org/api_docs/python/tf/keras/layers/RandomZoom>

Creating dataset from Google Images/ Bing

-   <https://pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/>
-   <https://medium.com/analytics-vidhya/a-simple-way-to-collect-your-deep-learning-image-dataset-4ead47b6826c>
-   \<\>

-   <https://developers.google.com/machine-learning/crash-course/representation/feature-engineering>

Probability distributions

-   <https://stats.stackexchange.com/questions/214275/intuitive-difference-between-joint-probability-and-conditional-probability-in-th>
-   <https://math.stackexchange.com/questions/1566215/difference-between-joint-probability-distribution-and-conditional-probability-di>

Bias variance -- <http://scott.fortmann-roe.com/docs/BiasVariance.html>

RNN

-   <https://stackoverflow.com/questions/43408463/how-does-tensorflows-multirnncell-work>

    -   For advanced learning, see the blog post mentioned in the
        accepted answer

-   <https://machinelearningmastery.com/understanding-simple-recurrent-neural-networks-in-keras/>

-   SimpleRNN vs. SimpleRNNCell --
    <https://stackoverflow.com/questions/50608080/what-is-a-cell-class-in-keras/50608296>

-   get_weights() for LSTM --
    <https://stackoverflow.com/questions/68845790/gate-weights-order-for-lstm-layers-in-tensorflow>

-   Migrating from v1 to v2 --
    <https://github.com/tensorflow/tensorflow/issues/28216>

-   *x*~*i*~

Autoencoders

-   Terms -- Latent variable model, variational inference, Evidence
    Lower Bound (ELBO)
-   <https://youtu.be/c27SHdQr4lw>
-   <https://bjlkeng.github.io/posts/variational-autoencoders/>
-   <https://ermongroup.github.io/cs228-notes/learning/latent/>
-   <https://datascience.stackexchange.com/questions/63977/how-does-joint-probability-generate-new-data-in-generative-model>

Initializing weights --
<https://stats.stackexchange.com/questions/27112/danger-of-setting-all-initial-weights-to-zero-in-backpropagation>

Kaggle

-   Use double dollar (\$\$) for Math Equations
-   Hamming Loss -- <https://www.kaggle.com/competitions/mlp3/data> (see
    sampleSubmission.csv)
