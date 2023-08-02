# Centralized-Digital-Library-Server-Application

I have developed a two-layer distributed application using Python Socket Programming as part of my lab project. The application's structure includes a total of 13 servers, comprising of one central server, three language-specific servers, and nine genre-specific servers.

The first layer of the application is designed to manage language-specific requests, and it incorporates three servers catering to Telugu, Hindi, and English literature, respectively.

The second layer consists of nine servers of genre-specific, with each server connected to one of the language servers . These servers host books from three various genres: horror, detective, and technical.

To facilitate seamless operations and interaction, a central server mediates communication between the clients and the first layer of servers.

By employing multi-threading techniques, the application efficiently handles multiple clients simultaneously, enhancing system efficiency and responsiveness. This setup ensures an organized, manageable, and efficient distribution of digital library resources.

Overall, the application has been successfully organized and is capable of effectively managing and serving digital library resources.
