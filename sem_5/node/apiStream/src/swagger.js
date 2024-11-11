import swaggerJsDoc from "swagger-jsdoc";
import swaggerUi from "swagger-ui-express";

const swaggerOptions = {
    swaggerDefinition: {
        openapi: "3.0.0",
        info: {
            title: "API Documentation",
            version: "1.0.0",
            description: "Documentation de l'API apiStream",
        },
        components: {
            schemas: {
                User: {  // Ajoutez ici le schéma "User" pour éviter les erreurs de résolution
                    type: "object",
                    properties: {
                        id: { type: "string", description: "ID unique de l'utilisateur" },
                        name: { type: "string", description: "Nom de l'utilisateur" },
                        email: { type: "string", description: "Email de l'utilisateur" }
                    }
                },
                Video: {  // Conservez le schéma Video si vous l'utilisez aussi
                    type: "object",
                    properties: {
                        id: { type: "string", description: "ID unique de la vidéo" },
                        title: { type: "string", description: "Titre de la vidéo" },
                        description: { type: "string", description: "Description de la vidéo" },
                        url: { type: "string", description: "URL de la vidéo" }
                    }
                }
            }
        },
        servers: [
            {
                url: "http://localhost:3000",
            },
        ],
    },
    apis: ["./src/routes/*.js"], // Chemin vers les fichiers de routes où les annotations Swagger seront définies
};

const specs = swaggerJsDoc(swaggerOptions);

export { swaggerUi, specs };
