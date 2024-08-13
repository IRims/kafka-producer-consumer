const { kafka } = require("./client");

async function init() {
    const admin = kafka.admin();
    try {
        console.log("Admin connecting...");
        await admin.connect(); // Ensure connection is awaited
        console.log("Admin Connection Success...");

        console.log("Creating Topic [rider-updates]");
        const result = await admin.createTopics({
            topics: [
                {
                    topic: "rider-updates",
                    numPartitions: 2,
                },
            ],
        });

        if (result) {
            console.log("Topic Created Successfully [rider-updates]");
        } else {
            console.log("Topic [rider-updates] already exists or wasn't created.");
        }

    } catch (error) {
        console.error("An error occurred:", error);
    } finally {
        console.log("Disconnecting Admin...");
        await admin.disconnect();
        console.log("Admin Disconnected.");
    }
}

init();
