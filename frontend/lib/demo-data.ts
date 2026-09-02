export const DEMO_CONVERSATIONS = [
  {
    id: "1",
    customer: "John Doe",
    subject: "Issue with billing",
    status: "open",
    last_message_at: new Date().toISOString(),
    unread_count: 2,
    ai_handled: false,
  },
  {
    id: "2",
    customer: "Jane Smith",
    subject: "Feature request",
    status: "resolved",
    last_message_at: new Date().toISOString(),
    unread_count: 0,
    ai_handled: true,
  },
];

export const DEMO_CUST_STATS = {
  total_conversations: 1284,
  open_conversations: 32,
  ai_replies: 847,
  customers: 923,
};
