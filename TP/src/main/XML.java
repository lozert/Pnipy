package src.main;

import java.util.*;

// Класс для Book
class Book {
    String id;
    String title;
    String author;
    int year;
    String genre;
    Price price;
    String format;
    Publisher publisher;
    List<Review> reviews = new ArrayList<>();
    String language;
    String translator;

    public Book(String id) {
        this.id = id;
    }

    @Override
    public String toString() {
        return "Book ID: " + id + "\nTitle: " + title + "\nAuthor: " + author + "\nYear: " + year + 
               "\nGenre: " + genre + "\nPrice: " + price + "\nFormat: " + format + 
               "\nPublisher: " + publisher + "\nReviews: " + reviews + "\nLanguage: " + language + 
               (translator != null ? "\nTranslator: " + translator : "");
    }
}

// Класс для Price
class Price {
    String currency;
    double value;

    public Price(String currency, double value) {
        this.currency = currency;
        this.value = value;
    }

    @Override
    public String toString() {
        return value + " " + currency;
    }
}

// Класс для Publisher
class Publisher {
    String name;
    Address address;

    @Override
    public String toString() {
        return "Publisher Name: " + name + ", Address: " + address;
    }
}

// Класс для Address
class Address {
    String city;
    String country;

    @Override
    public String toString() {
        return city + ", " + country;
    }
}

// Класс для Review
class Review {
    String user;
    int rating;
    String comment;

    @Override
    public String toString() {
        return "\nUser: " + user + ", Rating: " + rating + ", Comment: " + comment;
    }
}

// Класс для Library
class Library {
    List<Book> books = new ArrayList<>();

    @Override
    public String toString() {
        return "Library: " + books;
    }
}

public class XML {

    public static void main(String[] args) {
        String xml = "<library><book id='1'><title>Effective Java</title><author>Robert C. Martin</author>"
                   + "<year>2015</year><genre>Programming</genre><price currency='GBP'>32.67</price>"
                   + "<format>Audiobook</format><publisher><name>TechBooks Publishing</name>"
                   + "<address><city>London</city><country>USA</country></address></publisher>"
                   + "<reviews><review><user>dave</user><rating>5</rating><comment>Great book!</comment></review>"
                   + "<review><user>alice</user><rating>2</rating><comment>Very informative.</comment></review>"
                   + "<review><user>eve</user><rating>1</rating><comment>Not for me.</comment></review></reviews>"
                   + "<language>English</language></book></library>";

        Library library = parseXml(xml);
        System.out.println(library);
    }

    // Метод для парсинга XML
    public static Library parseXml(String xml) {
        Library library = new Library();
        Stack<String> stack = new Stack<>();
        String currentTag = null;
        Book currentBook = null;
        Review currentReview = null;
        Publisher currentPublisher = null;
        Address currentAddress = null;
        Price currentPrice = null;

        for (int i = 0; i < xml.length(); i++) {
            if (xml.charAt(i) == '<') {
                int closing = xml.indexOf('>', i);
                String tag = xml.substring(i + 1, closing);

                // Закрывающий тег
                if (tag.startsWith("/")) {
                    currentTag = stack.pop();
                    if (currentTag.equals("book")) {
                        library.books.add(currentBook);
                        currentBook = null;
                    } else if (currentTag.equals("review")) {
                        currentBook.reviews.add(currentReview);
                        currentReview = null;
                    } else if (currentTag.equals("publisher")) {
                        currentBook.publisher = currentPublisher;
                        currentPublisher = null;
                    } else if (currentTag.equals("address")) {
                        currentPublisher.address = currentAddress;
                        currentAddress = null;
                    } else if (currentTag.equals("price")) {
                        currentBook.price = currentPrice;
                        currentPrice = null;
                    }
                } else {
                    // Открывающий тег
                    stack.push(tag);
                    currentTag = tag.split(" ")[0];

                    if (currentTag.equals("book")) {
                        String id = tag.split("'")[1];
                        currentBook = new Book(id);
                    } else if (currentTag.equals("review")) {
                        currentReview = new Review();
                    } else if (currentTag.equals("publisher")) {
                        currentPublisher = new Publisher();
                    } else if (currentTag.equals("address")) {
                        currentAddress = new Address();
                    } else if (currentTag.equals("price")) {
                        String currency = tag.split("'")[1];
                        currentPrice = new Price(currency, 0.0);
                    }
                }
                i = closing;
            } else if (!stack.isEmpty()) {
                int closing = xml.indexOf('<', i);
                String content = xml.substring(i, closing).trim();

                if (!content.isEmpty()) {
                    switch (currentTag) {
                        case "title": currentBook.title = content; break;
                        case "author": currentBook.author = content; break;
                        case "year": currentBook.year = Integer.parseInt(content); break;
                        case "genre": currentBook.genre = content; break;
                        case "price": currentPrice.value = Double.parseDouble(content); break;
                        case "format": currentBook.format = content; break;
                        case "name": currentPublisher.name = content; break;
                        case "city": currentAddress.city = content; break;
                        case "country": currentAddress.country = content; break;
                        case "user": currentReview.user = content; break;
                        case "rating": currentReview.rating = Integer.parseInt(content); break;
                        case "comment": currentReview.comment = content; break;
                        case "language": currentBook.language = content; break;
                        case "translator": currentBook.translator = content; break;
                    }
                }
                i = closing - 1;
            }
        }
        return library;
    }
}
