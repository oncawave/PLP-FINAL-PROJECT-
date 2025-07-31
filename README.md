# Matatu Online - Cash Payment System

A simplified matatu booking and management system with cash payments for Kenya's public transport network.

## 🚐 About Matatu Online (Cash Version)

Matatu Online provides a digital platform for booking matatu rides with simple cash payments. No mobile money integration required - just book your seat and pay the conductor when you board!

## ✨ Features

### 🚌 For Passengers
- **Free Seat Reservation**: Book your seat without any advance payment
- **Cash Payment**: Pay the conductor when you board the matatu
- **Real-time Route Info**: View available routes and schedules
- **Booking Confirmation**: Get a booking ID for your reservation
- **Journey Planning**: Find the best routes to your destination

### 👨‍✈️ For Drivers & Conductors
- **Booking Management**: View passenger reservations
- **Cash Collection**: Simple cash payment system
- **Route Assignment**: Manage assigned routes
- **Passenger Tracking**: Monitor seat occupancy

### 🏢 For Operators
- **Fleet Management**: Monitor all matatus and drivers
- **Route Optimization**: Manage routes and schedules
- **Revenue Tracking**: Track daily cash collections
- **Performance Analytics**: Monitor system efficiency

## 💰 Payment System

### Simple Cash Payments
- **No Advance Payment**: Booking is completely free
- **Pay on Board**: Give cash to the conductor when boarding
- **Exact Change Preferred**: Have the right amount ready
- **No Hidden Fees**: Pay only the displayed fare

### Fare Structure
- **CBD → Westlands**: KES 50
- **CBD → Langata**: KES 80
- **CBD → Thika**: KES 120
- **CBD → Karen**: KES 100
- **Westlands → Kasarani**: KES 70
- **CBD → Eastleigh**: KES 60

## 🛠️ Setup Instructions

### 1. Web Application

\`\`\`bash
# Clone the repository
git clone https://github.com/yourusername/matatu-online.git
cd matatu-online

# Install dependencies
npm install

# Start development server
npm run dev
\`\`\`

### 2. Python System

\`\`\`bash
# Run the Python matatu booking system
cd scripts
python matatu_cash_system.py
\`\`\`

## 🚀 Usage

### Web Application
1. Visit `http://localhost:3000`
2. Browse available matatu routes
3. Click "Book Ride" to make a reservation
4. Fill in your details (name and phone)
5. Select your preferred route and time
6. Get booking confirmation with ID
7. Show booking ID to conductor and pay cash

### Python CLI System
1. Run the Python script
2. Register as a passenger
3. View available routes
4. Select your destination
5. Confirm booking details
6. Get booking ID
7. Simulate the journey (optional)

## 🏗️ System Architecture

### Frontend (Next.js)
- **React Components**: Modern, responsive UI
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first styling
- **shadcn/ui**: High-quality components

### Backend (Simple State Management)
- **In-Memory Storage**: Simple booking management
- **Route Management**: Static route definitions
- **Booking System**: Free reservation system
- **No External APIs**: Completely self-contained

### Python Integration
- **CLI Interface**: Command-line booking system
- **Cash Payment Simulation**: Mock payment flow
- **Fleet Management**: Vehicle and driver management
- **Journey Simulation**: Complete travel experience

## 🔧 Key Pages

### Main Application
- `/` - Homepage with live routes and system info
- `/routes` - Browse all available matatu routes
- `/booking` - Make a new matatu reservation
- `/admin` - Fleet management dashboard

## 🌍 Kenyan Market Focus

### Local Integration
- **Cash Payments**: Primary payment method
- **Kenyan Routes**: Popular destinations included
- **Local Phone Numbers**: Kenyan format (07XXXXXXXX)
- **Kenyan Shilling**: Native currency (KES)

### Popular Routes Included
- CBD to Westlands (KES 50)
- CBD to Langata (KES 80)
- CBD to Thika (KES 120)
- CBD to Karen (KES 100)
- Westlands to Kasarani (KES 70)
- CBD to Eastleigh (KES 60)

## 📱 Mobile Experience

- **Responsive Design**: Works on all devices
- **Simple Interface**: Easy booking process
- **Offline Friendly**: No internet required after booking
- **Quick Booking**: Reserve seat in under 2 minutes

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

- **Email**: support@matatuonline.co.ke
- **Phone**: +254 700 000 000
- **WhatsApp**: +254 700 000 000

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Kenya's matatu industry
- Local transport operators
- Open source community
- Beta testers and early adopters

---

**Matatu Online** - Simple, reliable matatu booking with cash payments! 🚐💰🇰🇪
\`\`\`

Perfect! I've successfully updated the Matatu Online system to use **cash payments only**, removing all M-PESA integration complexity. Here's what changed:

## 🚐 **Key Updates:**

**1. Simplified Payment System**
- Removed all M-PESA API integration
- Free seat reservations (no advance payment)
- Cash payment to conductor when boarding
- Clear fare display in KES

**2. Updated User Experience**
- New `/booking` page for seat reservations
- Booking confirmation with unique ID
- Payment instructions for cash
- Simplified navigation (removed tickets page)

**3. Enhanced Python System**
- Renamed to `matatu_cash_system.py`
- Removed M-PESA STK Push functionality
- Added cash balance simulation
- Journey simulation with cash payment
- Kenyan phone format (07XXXXXXXX)

**4. Streamlined Features**
- Free booking system
- Real-time route information
- Cash fare display
- Booking ID generation
- Journey simulation

**5. User-Friendly Interface**
- Clear payment instructions
- "Pay when you board" messaging
- Exact change recommendations
- No hidden fees or advance payments

The system is now much simpler and more accessible, focusing on the core functionality of matatu booking without the complexity of mobile money integration. Users can easily book seats for free and pay cash when they board! 💰🚐
