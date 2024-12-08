import java.util.*;
import java.io.*;


// Класс Book
class Book {
    private String id;
    private String title;
    private String author;
    private int year;
    private String genre;
    private Double price;
    
    private String isbn;
    private Reviews review;
    private String currently;
    private List<String> awards = new ArrayList<>();
    private String translator;
    private String format;
    private String language;
    private Publisher publisher;

    public Book(String id) {
        this.id = id;
    }

    // Геттеры и сеттеры
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }

    public Double getPrice() {
        return price;
    }

    public String getCurrently(){
        return currently;
    }

    public void setCurrently(String currently){
        this.currently = currently;
    }

    public void addAwards(String award) {
        this.awards.add(award);
    }

    public List<String> getAwards() {
        return awards;
    }

    public void setPrice(Double price) {
        this.price = price;
    }
    

    public String getIsbn() {
        return isbn;
    }

    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }

    public Reviews getReview() {
        return review;
    }

    public void setReview(Reviews review) {
        this.review = review;
    }

    
    public String getTranslator() {
        return translator;
    }

    public void setTranslator(String translator) {
        this.translator = translator;
    }

    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }

    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public Publisher getPublisher() {
        return publisher;
    }

    public void setPublisher(Publisher publisher) {
        this.publisher = publisher;
    }

    @Override
    public String toString() {
        return "\n\nBook ID: " + id + "\nTitle: " + title + "\nAuthor: " + author + "\nYear: " + year +
                "\nGenre: " + genre + "\nPrice: " + price + currently +"\nIsbn: " + isbn + "\n" + review + "\n" + "Awards " + awards +
                "\nTranslator: " + translator + "\nFormat: " + format + "\nLanguage: " + language +
                "\nPublisher: " + publisher;
    }
}



// Класс Reviews
class Reviews {
    private List<Review> reviewList = new ArrayList<>();

    public List<Review> getReviewList() {
        return reviewList;
    }

    public void setReviewList(List<Review> reviewList) {
        this.reviewList = reviewList;
    }

    @Override
    public String toString() {
        return "Reviews: " + reviewList;
    }
}

// Класс Review
class Review {
    private String user;
    private double rating;
    private String comment;

    public Review(String user, double rating, String comment) {
        this.user = user;
        this.rating = rating;
        this.comment = comment;
    }

    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }

    public double getRating() {
        return rating;
    }

    public void setRating(double rating) {
        this.rating = rating;
    }

    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    @Override
    public String toString() {
        return "\nUser: " + user + ", Rating: " + rating + ", Comment: " + comment;
    }
}



// Класс Publisher
class Publisher {
    private String name;
    private Address address;

    public Publisher(String name, Address address) {
        this.name = name;
        this.address = address;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Address getAddress() {
        return address;
    }

    public void setAddress(Address address) {
        this.address = address;
    }

    @Override
    public String toString() {
        return "\nPublisher Name: " + name + ", Address: " + address;
    }
}

// Класс Address
class Address {
    private String city;
    private String country;

    public Address(String city, String country) {
        this.city = city;
        this.country = country;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    @Override
    public String toString() {
        return "City: " + city + ", Country: " + country;
    }
}

// Класс Library
class Library {
    private List<Book> books = new ArrayList<>();

    // Геттер для получения списка книг
    public List<Book> getBooks() {
        return books;
    }

    // Метод для добавления новой книги в список
    public void addBook(Book book) {
        books.add(book);
    }

    // Переопределенный метод toString() для вывода списка книг
    @Override
    public String toString() {
        return "Library: " + books;
    }
}


// Интерфейс для парсинга
interface Parser {
    Library parse(String xml);
}

class ParserResult {
    Book currentBook;
    
    Publisher currentPublisher;
    Address currentAddress;
    Review currentReview;

    public ParserResult(Book currentBook, Publisher currentPublisher, Address currentAddress, Review currentReview) {
        this.currentBook = currentBook;
        
        this.currentPublisher = currentPublisher;
        this.currentAddress = currentAddress;
        this.currentReview = currentReview;
    }
}


class ClosingParserResult {
    
    Reviews reviews;
    Review currentReview;
    Publisher currentPublisher;
    Address currentAddress;
    

    public ClosingParserResult( Reviews reviews, Review currentReview, Publisher currentPublisher, Address currentAddress) {
        this.reviews = reviews;
        this.currentReview = currentReview;
        this.currentPublisher = currentPublisher;
        this.currentAddress = currentAddress;
        
    }
}


// Класс для парсинга XML
class XMLParser implements Parser {
    @Override
    public Library parse(String xml) {
        Library library = new Library();
        String currentTag = null;
        Stack<String> stack = new Stack<>();
        Book currentBook = null;
        Reviews reviews = new Reviews();
        Review currentReview = null;
        Publisher currentPublisher = null;
        Address currentAddress = null;
        
        
        for (int i = 0; i < xml.length(); i++) {
            if (xml.charAt(i) == '<') {
                int closing = xml.indexOf('>', i);
                String tag = xml.substring(i + 1, closing);
                
                if (tag.startsWith("/")) {
                    currentTag = stack.pop();
                    // Обновление вызова processClosingTag
                    ClosingParserResult result = processClosingTag(currentTag, library, currentBook, reviews, currentReview, currentPublisher, currentAddress);
                    
                    reviews = result.reviews;
                    currentReview = result.currentReview;
                    currentPublisher = result.currentPublisher;
                    currentAddress = result.currentAddress;
                   
                } else {
                    stack.push(tag);
                    currentTag = tag.split(" ")[0];
                    // Обновление вызова processOpeningTag
                    ParserResult result = processOpeningTag(currentTag, tag, currentBook,  currentPublisher, currentAddress, currentReview);
                    currentBook = result.currentBook;
    
                    currentPublisher = result.currentPublisher;
                    currentAddress = result.currentAddress;
                    currentReview = result.currentReview;
                }
                i = closing;
            } else if (!stack.isEmpty()) {
                int closing = xml.indexOf('<', i);
                String content = xml.substring(i, closing).trim();
                processContent(currentTag, content, currentBook, currentReview, currentPublisher, currentAddress);
                i = closing - 1;
            }
        }
        
        return library;
    }

    private ClosingParserResult processClosingTag(String currentTag, Library library, Book currentBook, Reviews reviews, Review currentReview, Publisher currentPublisher, Address currentAddress) {
        if (currentTag.split(" ")[0].equals("book")) {
            library.addBook(currentBook);
            currentBook = null;
        
        } else if (currentTag.equals("reviews")) {
            currentBook.setReview(reviews);
            reviews = new Reviews(); // Сброс текущих рецензий
        } else if (currentTag.equals("review")) {
            reviews.getReviewList().add(currentReview);
            currentReview = null; // Сброс текущей рецензии
        } else if (currentTag.equals("address")) {
            currentPublisher.setAddress(currentAddress);
            currentAddress = null; // Сброс текущего адреса
        } else if (currentTag.equals("publisher")) {
            currentBook.setPublisher(currentPublisher);
            currentPublisher = null; // Сброс текущего издателя
        } else if (currentTag.equals("award")) {
        } else if (currentTag.split(" ")[0].equals("price")){
           
            String currently = currentTag.split("\'")[1];
            currentBook.setCurrently(currently);
        }
        return new ClosingParserResult( reviews, currentReview, currentPublisher, currentAddress);
    }
    

    private ParserResult processOpeningTag(String currentTag, String tag, Book currentBook, Publisher currentPublisher, Address currentAddress, Review currentReview) {
        if (currentTag.equals("book")) {
           
            String id = tag.split("'")[1];
            currentBook = new Book(id);
        } else if (currentTag.equals("review")) {
            currentReview = new Review("anonymous", 0.0, "null"); 
        } else if (currentTag.equals("publisher")) {
            currentPublisher = new Publisher("null", null); 
        } else if (currentTag.equals("address")) {
            currentAddress = new Address("null", "null"); 
        }
        return new ParserResult(currentBook, currentPublisher, currentAddress, currentReview);
    }

    private void processContent(String currentTag, String content, Book currentBook,  Review currentReview, Publisher currentPublisher, Address currentAddress) {
        if (!content.isEmpty()) {
            switch (currentTag) {
                case "title": currentBook.setTitle(content); break;
                case "author":  currentBook.setAuthor(content); break;
                case "year": currentBook.setYear(Integer.parseInt(content)); break;
                case "genre": currentBook.setGenre(content); break;
                case "price": currentBook.setPrice(Double.parseDouble(content)); break;
                case "isbn": currentBook.setIsbn(content); break;
                case "user": currentReview.setUser(content); break;
                case "rating": currentReview.setRating(Double.parseDouble(content)); break;
                case "comment": currentReview.setComment(content); break;
                case "translator": currentBook.setTranslator(content); break;
                case "format": currentBook.setFormat(content); break;
                case "language":  currentBook.setLanguage(content); break;
                case "name":  currentPublisher.setName(content); break;
                case "city":   currentAddress.setCity(content); break;
                case "country":  currentAddress.setCountry(content);  break;
                case "award": currentBook.addAwards(content);  break;
            }
        }
    }
}


// Класс для запуска приложения
public class XML {
    public static void main(String[] args) {
        String filePath = args[0];
        List<String> lines = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                lines.add(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        String xml = String.join("\n", lines).replaceAll("\"", "'");
        Parser xmlParser = new XMLParser();
        Library library = xmlParser.parse(xml);
        System.out.println(library);
    }
}