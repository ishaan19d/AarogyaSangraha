// Define an array of health quotes
const healthQuotes = [
    { text: "Health is a state of complete harmony of the body, mind, and spirit.", author: "B.K.S. Iyengar" },
    { text: "The greatest wealth is health.", author: "Virgil" },
    { text: "To ensure good health: eat lightly, breathe deeply, live moderately, cultivate cheerfulness, and maintain an interest in life.", author: "William Londen" },
    { text: "The first wealth is health.", author: "Ralph Waldo Emerson" },
    { text: "Health is the crown on the well person's head that only the ill person can see.", author: "Robin Sharma" },
    { text: "The doctor of the future will no longer treat the human frame with drugs, but rather will cure and prevent disease with nutrition.", author: "Thomas Edison" },
    { text: "He who has health has hope, and he who has hope has everything.", author: "Arabian Proverb" },
    { text: "Take care of your body. It's the only place you have to live.", author: "Jim Rohn" },
    { text: "A healthy outside starts from the inside.", author: "Robert Urich" },
    { text: "Your body holds deep wisdom. Trust in it. Learn from it. Nourish it. Watch your life transform and be healthy.", author: "Bella Bleue" },
    { text: "A good laugh and a long sleep are the best cures in the doctor's book.", author: "Irish Proverb" },
    { text: "An ounce of prevention is worth a pound of cure.", author: "Benjamin Franklin" },
    { text: "The secret of health for both mind and body is not to mourn for the past, worry about the future, or anticipate troubles, but to live in the present moment wisely and earnestly.", author: "Buddha" },
    { text: "Walking is man's best medicine.", author: "Hippocrates" },
    { text: "Physical fitness is not only one of the most important keys to a healthy body, it is the basis of dynamic and creative intellectual activity.", author: "John F. Kennedy" },
    { text: "Health is not simply the absence of sickness.", author: "Hannah Green" },
    { text: "Your body is a temple, but only if you treat it as one.", author: "Astrid Alauda" },
    { text: "To keep the body in good health is a duty... otherwise we shall not be able to keep our mind strong and clear.", author: "Buddha" },
    { text: "In order to change we must be sick and tired of being sick and tired.", author: "Unknown" },
    { text: "The groundwork of all happiness is health.", author: "Leigh Hunt" }
];

// Function to get a random health quote
function getRandomHealthQuote() {
    const randomIndex = Math.floor(Math.random() * healthQuotes.length);
    const quote = healthQuotes[randomIndex];
    
    // Output the quote and author name
    console.log(quote.text);
    console.log(`- ${quote.author}`);

    // Display the quote on the webpage
    document.getElementById("quote").innerHTML = quote.text +"<br>- " + quote.author;
}

// Call getRandomHealthQuote() function when the page loads
window.onload = getRandomHealthQuote;
