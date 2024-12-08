import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;


class Library {

    private List<Book> books = new ArrayList<>();

    public void addBook(Book book) {
        books.add(book);
    }
    static class Book {

        private String bookId;
        private String bookTitle;
        private String bookAuthor;
        private String publicationYear;
        private String bookGenre;
        private String bookPrice;
        private String bookLanguage;
        private List<Review> reviewList;

        public List<Review> getReviews() {
            return reviewList;
        }

        public void addReviewUser(String userName) {
            if (this.reviewList == null) {
                this.reviewList = new ArrayList<>();
            }
            Review newReview = new Review();
            newReview.setUser(userName);
            this.reviewList.add(newReview);
        }

        public void addReviewRating(String rating) {
            if (this.reviewList != null && !this.reviewList.isEmpty()) {
                this.reviewList.get(this.reviewList.size() - 1).setRating(rating);
            }
        }

        public void addReviewComment(String comment) {
            if (this.reviewList != null && !this.reviewList.isEmpty()) {
                this.reviewList.get(this.reviewList.size() - 1).setComment(comment);
            }
        }

        private List<String> awards;

        public String getBookId() {
            return bookId;
        }

        public void setAwards(List<String> awards) {
            this.awards = awards;
        }

        public List<String> getAwards() {
            return awards;
        }

        public void setBookId(String id) {
            this.bookId = id;
        }

        public String getBookTitle() {
            return bookTitle;
        }

        public void setBookTitle(String title) {
            this.bookTitle = title;
        }

        public String getBookAuthor() {
            return bookAuthor;
        }

        public void setBookAuthor(String author) {
            this.bookAuthor = author;
        }

        public String getPublicationYear() {
            return publicationYear;
        }

        public void setPublicationYear(String year) {
            this.publicationYear = year;
        }

        public String getBookGenre() {
            return bookGenre;
        }

        public void setBookGenre(String genre) {
            this.bookGenre = genre;
        }

        public String getBookPrice() {
            return bookPrice;
        }

        public void setBookPrice(String price) {
            this.bookPrice = price;
        }

        public String getBookLanguage() {
            return bookLanguage;
        }

        public void setBookLanguage(String language) {
            this.bookLanguage = language;
        }

        @Override
        public String toString() {
            return "Book ID: " + bookId + '\n' +
                    "\tTitle: " + bookTitle + '\n' +
                    "\tAuthor: " + bookAuthor + '\n' +
                    "\tYear: " + publicationYear + '\n' +
                    "\tGenre: " + bookGenre + '\n' +
                    "\tPrice: " + bookPrice + '\n' +
                    "\tLanguage: " + bookLanguage + '\n' +
                    "\tAwards: " + awards + '\n' +
                    "\tReviews: " + reviewList + '\n';
        }
    }

    static class Review {

        private String user;
        private String rating;
        private String comment;

        public String getUser() {
            return user;
        }

        public void setUser(String user) {
            this.user = user;
        }

        public String getRating() {
            return rating;
        }

        public void setRating(String rating) {
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
            return "User: " + user + '\n' + "Rating: " + rating + '\n' + "Comment: " + comment + '\n';
        }
    }
}

public class Main {

    public static String Parse(String filePath) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(filePath));
        String line;
        Library.Book currentBook = new Library.Book();

        while ((line = reader.readLine()) != null) {
            if (line.contains("<book id=")) {
                currentBook.setBookId(line.replaceAll("<book id=\"", "").replaceAll("\">", ""));
            } else if (line.contains("<title>")) {
                currentBook.setBookTitle(line.replaceAll("<title>", "").replaceAll("</title>", ""));
            } else if (line.contains("<author>")) {
                currentBook.setBookAuthor(line.replaceAll("<author>", "").replaceAll("</author>", ""));
            } else if (line.contains("<year>")) {
                currentBook.setPublicationYear(line.replaceAll("<year>", "").replaceAll("</year>", ""));
            } else if (line.contains("<genre>")) {
                currentBook.setBookGenre(line.replaceAll("<genre>", "").replaceAll("</genre>", ""));
            } else if (line.contains("<price currency=")) {
                currentBook.setBookPrice(line.replaceAll("<price currency=\"[^\"]*\">", "").replaceAll("</price>", ""));
            } else if (line.contains("<language>")) {
                currentBook.setBookLanguage(line.replaceAll("<language>", "").replaceAll("</language>", ""));
            } else if (line.contains("<user>")) {
                currentBook.addReviewUser(line.replaceAll("<user>", "").replaceAll("</user>", ""));
            } else if (line.contains("<rating>")) {
                currentBook.addReviewRating(line.replaceAll("<rating>", "").replaceAll("</rating>", ""));
            } else if (line.contains("<comment>")) {
                currentBook.addReviewComment(line.replaceAll("<comment>", "").replaceAll("</comment>", ""));
            } else if (line.contains("<award>")) {
                currentBook.setAwards(Collections.singletonList(line.replaceAll("<award>", "").replaceAll("</award>", "")));
            } else if (line.contains("</book>")) {
                System.out.println(currentBook);
            }
        }
        reader.close();
        return "Processing Complete";
    }

    public static void main(String[] args) throws IOException {
        String filename = args[0];
        System.out.println(Parse( filename));
    }
}
