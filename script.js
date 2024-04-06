const quotes = [
    "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
    "The way to get started is to quit talking and begin doing. - Walt Disney",
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
    "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "Tell me and I forget. Teach me and I remember. Involve me and I learn. - Benjamin Franklin",
    "The only way to do great work is to love what you do. - Steve Jobs",
  ];
  
  function getRandomQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    return quotes[randomIndex];
  }
  
  function displayQuote() {
    const quoteElement = document.getElementById("quote-text");
    quoteElement.textContent = getRandomQuote();
  }
  
  const newQuoteBtn = document.getElementById("new-quote-btn");
  newQuoteBtn.addEventListener("click", displayQuote);
  
  // Set initial text
  displayQuote();
  