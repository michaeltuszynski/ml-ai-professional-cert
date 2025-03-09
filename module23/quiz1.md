# Module 23: Generative Models Quiz

## Question 1 (1 pt)
What is a common limitation of generative adversarial networks (GANs)?

**Options:**
1. They are designed to be faster than other generative models.
2. They require extensive computational resources and training time.
3. They are typically unstable during training and can suffer from mode collapse.
4. They are limited to generating images and cannot handle text or audio.

**Answer:** Option 3: They are typically unstable during training and can suffer from mode collapse.

GANs are fundamentally defined by their adversarial training process between generator and discriminator networks. This inherent competition often leads to training instability where the networks fail to converge properly. Mode collapse is a specific failure case where the generator produces limited varieties of outputs, failing to capture the full diversity of the training distribution.

---

## Question 2 (1 pt)
What is a key drawback of variational autoencoders (VAEs)?

**Options:**
1. VAEs often produce blurry or less detailed images compared with other models.
2. VAEs are incapable of handling high-dimensional data.
3. VAEs are less stable during training compared with GANs.
4. VAEs require multiple neural networks to be trained simultaneously.

**Answer:** Option 1: VAEs often produce blurry or less detailed images compared with other models.

VAEs are defined by their probabilistic latent variable model that encodes inputs into a distribution in latent space. This probabilistic encoding, while allowing for controlled generation and interpolation, tends to produce outputs that average over possible solutions, resulting in blurrier or less detailed images compared to models like GANs that directly optimize for visual fidelity.

---

## Question 3 (1 pt)
What is a major challenge associated with diffusion models?

**Options:**
1. Diffusion models require a very large number of training steps to generate high-quality images
2. Diffusion models rely on adversarial training to improve performance.
3. Diffusion models are prone to generating unrealistic images due to limited training data.
4. Diffusion models are less effective at generating images than GANs.

**Answer:** Option 1: Diffusion models require a very large number of training steps to generate high-quality images.

Diffusion models are defined by their iterative process of gradually adding and then removing noise. This fundamental design requires many sequential denoising steps during inference, making the generation process computationally intensive and time-consuming compared to single-pass generation in other models like GANs or VAEs.

---

## Question 4 (1 pt)
What limitation is commonly associated with training deep generative models in general?

**Options:**
1. Deep generative models are limited to specific domains.
2. Deep generative models are unable to produce diverse outputs.
3. Deep generative models generally require large amounts of data and computational resources.
4. Deep generative models are inherently biased toward generating only synthetic data.

**Answer:** Option 3: Deep generative models generally require large amounts of data and computational resources.

Deep generative models are defined by their ability to learn complex data distributions. This fundamental capability requires substantial training data to accurately capture distribution characteristics and significant computational resources to optimize the large number of parameters needed to represent these distributions effectively.

---

## Answer Key

1. Option 3: They are typically unstable during training and can suffer from mode collapse. (Core challenge in GAN training dynamics)
2. Option 1: VAEs often produce blurry or less detailed images compared with other models. (Result of probabilistic encoding)
3. Option 1: Diffusion models require a very large number of training steps to generate high-quality images. (Due to iterative denoising process)
4. Option 3: Deep generative models generally require large amounts of data and computational resources. (Necessary for learning complex distributions)
