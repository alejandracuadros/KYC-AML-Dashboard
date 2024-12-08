USE regulatory_compliance;

INSERT INTO pep_individuals (pep_id, full_name, job_title, country, class, date_of_birth)
VALUES
(1, 'John Doe', 'Minister of Finance', 'USA', 'Government', '1970-05-15'),
(2, 'Jane Smith', 'Supreme Court Judge', 'UK', 'Judiciary', '1965-11-02'),
(3, 'Carlos Gomez', 'Brigadier General', 'Mexico', 'Military', '1975-08-19'),
(4, 'Aisha Khan', 'Mayor of Capital City', 'Pakistan', 'Government', '1980-03-27'),
(5, 'Li Wei', 'Defense Secretary', 'China', 'Government', '1968-06-12'),
(6, 'Anna Petrova', 'Ambassador to the UN', 'Russia', 'Government', '1972-09-09'),
(7, 'Mark Jensen', 'High Court Judge', 'Canada', 'Judiciary', '1960-12-22'),
(8, 'Ahmed Suleiman', 'General of Armed Forces', 'Nigeria', 'Military', '1978-03-15'),
(9, 'Isabel Fernandez', 'Minister of Education', 'Spain', 'Government', '1982-11-20'),
(10, 'Hassan Youssef', 'Chief Justice', 'Egypt', 'Judiciary', '1964-01-07'),
(11, 'Marie Dubois', 'Minister of Health', 'France', 'Government', '1973-06-18'),
(12, 'Kenji Tanaka', 'Defense General', 'Japan', 'Military', '1969-02-28'),
(13, 'Fatima Abdullah', 'Governor', 'UAE', 'Government', '1976-08-04'),
(14, 'Stefan Novak', 'Minister of Defense', 'Poland', 'Government', '1971-05-09'),
(15, 'Olivia Green', 'Deputy Minister of Trade', 'Australia', 'Government', '1985-04-14');

INSERT INTO pep_and_organization_association (pep_id, organization_name, relationship_type, country)
VALUES
(1, 'Global Finance Inc.', 'Ownership', 'USA'),
(1, 'North American Holdings', 'Partnership', 'Canada'),
(2, 'UK Judicial Affairs Association', 'Membership', 'UK'),
(3, 'Military Logistics Co.', 'Ownership', 'Mexico'),
(4, 'Urban Development Partners', 'Partnership', 'Pakistan'),
(5, 'Asian Defense Technologies', 'Ownership', 'China'),
(6, 'Diplomatic Ventures Ltd.', 'Partnership', 'Russia'),
(7, 'Canadian Legal Council', 'Membership', 'Canada'),
(8, 'Nigerian Security Corporation', 'Ownership', 'Nigeria'),
(9, 'Educational Outreach LLC', 'Partnership', 'Spain'),
(10, 'Egyptian Judiciary Network', 'Membership', 'Egypt'),
(11, 'French Health Council', 'Partnership', 'France'),
(12, 'Defense Technologies Japan', 'Ownership', 'Japan'),
(13, 'Gulf Trade Network', 'Partnership', 'UAE'),
(14, 'Eastern European Defense Group', 'Partnership', 'Poland'),
(15, 'Pacific Trade Alliance', 'Ownership', 'Australia');

INSERT INTO startups (startup_id, startup_name, country, date_of_incorporation, company_size, employees)
VALUES
(1, 'GreenTech Solutions', 'USA', '2012-05-14', 'Medium', 50),
(2, 'AgriFuture', 'India', '2015-03-20', 'Small', 15),
(3, 'FinTech Innovators', 'UK', '2011-07-01', 'Medium', 120),
(4, 'HealthFirst AI', 'Germany', '2013-09-25', 'Large', 300),
(5, 'EduLearn Platform', 'Australia', '2017-01-10', 'Small', 10),
(6, 'UrbanGro', 'Canada', '2014-11-08', 'Small', 25),
(7, 'CyberSecureX', 'Israel', '2016-06-15', 'Medium', 100),
(8, 'CleanWater Inc.', 'South Africa', '2013-03-12', 'Small', 40),
(9, 'NextGen Robotics', 'Japan', '2012-10-07', 'Large', 500),
(10, 'EcoFoods', 'Brazil', '2018-04-19', 'Small', 12),
(11, 'SpacePioneers', 'USA', '2011-02-28', 'Large', 600),
(12, 'Solar Innovators', 'Germany', '2019-05-30', 'Medium', 150),
(13, 'BioMed Solutions', 'India', '2014-07-22', 'Small', 35),
(14, 'SmartEdu', 'Singapore', '2016-08-05', 'Small', 18),
(15, 'GreenSpaces', 'UK', '2012-12-16', 'Large', 220),
(16, 'HealthAI Analytics', 'Canada', '2015-09-01', 'Large', 270),
(17, 'BlueOcean Ventures', 'Australia', '2013-01-25', 'Medium', 60),
(18, 'AI Nexus', 'USA', '2010-03-18', 'Large', 800),
(19, 'FarmTech Pro', 'Netherlands', '2017-10-03', 'Medium', 70),
(20, 'EcoRide', 'France', '2014-02-11', 'Small', 40),
(21, 'Wellness4All', 'India', '2018-06-27', 'Medium', 50),
(22, 'UrbanTech Design', 'South Korea', '2011-11-14', 'Medium', 140),
(23, 'RoboLogix', 'USA', '2016-04-05', 'Medium', 85),
(24, 'SolarHarvest', 'South Africa', '2010-09-29', 'Small', 45),
(25, 'SmartGrid Solutions', 'Germany', '2014-12-03', 'Large', 350),
(26, 'GreenFarm', 'India', '2019-02-17', 'Small', 20),
(27, 'CleanOcean Tech', 'Australia', '2015-07-09', 'Medium', 90),
(28, 'MediTech Innovations', 'UK', '2013-11-23', 'Medium', 60),
(29, 'SafeCity', 'USA', '2011-01-31', 'Medium', 120),
(30, 'EcoLiving Designs', 'France', '2018-10-15', 'Small', 25);

INSERT INTO startup_profile (startup_id, industry, last_year_revenue, current_projected_revenue, next_year_revenue, amount_raised)
VALUES
(1, 'Renewable Energy', 2.5, 3.0, 3.8, 7.5),
(2, 'Agriculture', 0.8, 1.0, 1.2, 2.4),
(3, 'Financial Technology', 4.7, 5.6, 7.1, 14.1),
(4, 'Healthcare', 7.3, 8.8, 11.0, 21.9),
(5, 'EdTech', 0.4, 0.5, 0.6, 1.2),
(6, 'Urban Farming', 1.2, 1.4, 1.8, 3.6),
(7, 'Cybersecurity', 3.9, 4.7, 5.9, 11.7),
(8, 'Water Purification', 2.8, 3.4, 4.2, 8.4),
(9, 'Robotics', 9.5, 11.4, 14.3, 28.5),
(10, 'FoodTech', 0.6, 0.7, 0.9, 1.8),
(11, 'Aerospace', 15.0, 18.0, 22.5, 45.0),
(12, 'Renewable Energy', 4.3, 5.2, 6.5, 12.9),
(13, 'Biotechnology', 1.9, 2.3, 2.9, 5.7),
(14, 'EdTech', 0.7, 0.8, 1.1, 2.1),
(15, 'Urban Planning', 5.1, 6.1, 7.7, 15.3),
(16, 'Healthcare', 8.7, 10.4, 13.1, 26.1),
(17, 'Marine Technology', 2.4, 2.9, 3.6, 7.2),
(18, 'Artificial Intelligence', 20.0, 24.0, 30.0, 60.0),
(19, 'Agriculture', 3.1, 3.7, 4.7, 9.3),
(20, 'Transportation', 1.5, 1.8, 2.3, 4.5),
(21, 'Healthcare', 1.3, 1.6, 2.0, 3.9),
(22, 'Urban Planning', 6.2, 7.4, 9.3, 18.6),
(23, 'Robotics', 3.4, 4.1, 5.1, 10.2),
(24, 'Renewable Energy', 2.1, 2.5, 3.2, 6.3),
(25, 'Energy', 9.0, 10.8, 13.5, 27.0),
(26, 'Agriculture', 0.9, 1.1, 1.4, 2.7),
(27, 'Marine Technology', 4.0, 4.8, 6.0, 12.0),
(28, 'Biotechnology', 2.7, 3.2, 4.1, 8.1),
(29, 'Urban Safety', 5.8, 7.0, 8.7, 17.4),
(30, 'Interior Design', 1.0, 1.2, 1.5, 3.0);

INSERT INTO founders_details (passport_id, full_name, date_of_birth, nationality, birth_place, residence_place, gender, phone_number, email, startup_id, role_in_startup)
VALUES
('US987654321', 'Emily Carter', '1985-07-22', 'American', 'New York', 'San Francisco', 'Female', '+1-202-555-0101', 'emily.carter@greentech.com', 1, 'Founder'),
('IN543210987', 'Rahul Mehta', '1990-10-15', 'Indian', 'Mumbai', 'Bangalore', 'Male', '+91-9876543210', 'rahul.mehta@agrifuture.in', 2, 'Founder'),
('UK123456789', 'Sophia Turner', '1982-03-05', 'British', 'London', 'Manchester', 'Female', '+44-20-79460001', 'sophia.turner@fintechuk.co.uk', 3, 'Founder'),
('DE987123654', 'Hans Müller', '1978-12-01', 'German', 'Berlin', 'Munich', 'Male', '+49-30-12345678', 'hans.muller@healthfirst.de', 4, 'Founder'),
('AU654321987', 'Michael Brown', '1995-09-11', 'Australian', 'Sydney', 'Melbourne', 'Male', '+61-2-98765432', 'michael.brown@edulearn.com', 5, 'Founder'),
('CA543219876', 'Lisa Adams', '1988-06-14', 'Canadian', 'Toronto', 'Vancouver', 'Female', '+1-416-555-0199', 'lisa.adams@urbangro.ca', 6, 'Founder'),
('IL123654789', 'David Levy', '1980-08-22', 'Israeli', 'Tel Aviv', 'Jerusalem', 'Male', '+972-3-1234567', 'david.levy@cybersecurex.co.il', 7, 'Founder'),
('ZA321987654', 'Thabo Nkosi', '1985-11-30', 'South African', 'Cape Town', 'Johannesburg', 'Male', '+27-21-1234567', 'thabo.nkosi@cleanwater.co.za', 8, 'Founder'),
('JP654987321', 'Takumi Ito', '1979-04-18', 'Japanese', 'Tokyo', 'Osaka', 'Male', '+81-3-12345678', 'takumi.ito@nextgenrobotics.jp', 9, 'Founder'),
('BR321654987', 'Ana Oliveira', '1987-05-07', 'Brazilian', 'São Paulo', 'Rio de Janeiro', 'Female', '+55-11-912345678', 'ana.oliveira@ecofoods.com.br', 10, 'Founder'),
('US654123987', 'Alex Johnson', '1984-02-19', 'American', 'New York', 'San Francisco', 'Male', '+1-202-555-0102', 'alex.johnson@spacepioneers.com', 11, 'Founder'),
('DE987654321', 'Clara Schmidt', '1983-03-14', 'German', 'Berlin', 'Munich', 'Female', '+49-30-12345679', 'clara.schmidt@solarinnovators.de', 12, 'Founder'),
('IN876543210', 'Vikram Patel', '1989-09-29', 'Indian', 'Mumbai', 'Bangalore', 'Male', '+91-9876543211', 'vikram.patel@biomedsolutions.in', 13, 'Founder'),
('SG654987123', 'Grace Tan', '1991-04-08', 'Singaporean', 'Singapore', 'Singapore', 'Female', '+65-61234567', 'grace.tan@smartedu.sg', 14, 'Founder'),
('UK321654987', 'Emma Davis', '1976-07-16', 'British', 'London', 'Manchester', 'Female', '+44-20-79460002', 'emma.davis@greenspaces.co.uk', 15, 'Founder'),
('CA987654123', 'James Martin', '1980-10-01', 'Canadian', 'Toronto', 'Vancouver', 'Male', '+1-416-555-0200', 'james.martin@healthai.ca', 16, 'Founder'),
('AU123456987', 'Sophia Williams', '1986-06-20', 'Australian', 'Sydney', 'Melbourne', 'Female', '+61-2-98765433', 'sophia.williams@blueocean.com.au', 17, 'Founder'),
('US876543219', 'Robert Thompson', '1983-12-25', 'American', 'New York', 'San Francisco', 'Male', '+1-202-555-0103', 'robert.thompson@ainexus.com', 18, 'Founder'),
('NL987321654', 'Lucas van Dijk', '1977-01-17', 'Dutch', 'Amsterdam', 'Rotterdam', 'Male', '+31-20-1234567', 'lucas.vandijk@farmtechpro.nl', 19, 'Founder'),
('FR321987654', 'Chloe Moreau', '1989-08-03', 'French', 'Paris', 'Lyon', 'Female', '+33-1-12345678', 'chloe.moreau@ecoride.fr', 20, 'Founder'),
('IN654987321', 'Anjali Sharma', '1992-11-11', 'Indian', 'Mumbai', 'Bangalore', 'Female', '+91-9876543212', 'anjali.sharma@wellness4all.in', 21, 'Founder'),
('KR321654987', 'Min Jae Park', '1985-05-30', 'South Korean', 'Seoul', 'Busan', 'Male', '+82-2-12345678', 'min.park@urbantech.kr', 22, 'Founder'),
('US654987123', 'Karen White', '1987-09-07', 'American', 'New York', 'San Francisco', 'Female', '+1-202-555-0104', 'karen.white@robologix.com', 23, 'Founder'),
('ZA987654321', 'Sizwe Mkhize', '1990-04-04', 'South African', 'Cape Town', 'Johannesburg', 'Male', '+27-21-1234568', 'sizwe.mkhize@solarharvest.co.za', 24, 'Founder'),
('DE543216789', 'Lukas Weber', '1981-06-15', 'German', 'Berlin', 'Munich', 'Male', '+49-30-12345680', 'lukas.weber@smartgrid.de', 25, 'Founder'),
('IN321987654', 'Pooja Nair', '1993-07-23', 'Indian', 'Mumbai', 'Bangalore', 'Female', '+91-9876543213', 'pooja.nair@greenfarm.in', 26, 'Founder'),
('AU876543210', 'Jack Brown', '1980-02-13', 'Australian', 'Sydney', 'Melbourne', 'Male', '+61-2-98765434', 'jack.brown@cleanocean.au', 27, 'Founder'),
('UK654123987', 'Oliver Taylor', '1994-03-22', 'British', 'London', 'Manchester', 'Male', '+44-20-79460003', 'oliver.taylor@meditech.co.uk', 28, 'Founder'),
('US543216789', 'Laura Wilson', '1988-12-11', 'American', 'New York', 'San Francisco', 'Female', '+1-202-555-0105', 'laura.wilson@safecity.com', 29, 'Founder'),
('FR654987321', 'Sophie Laurent', '1993-12-08', 'French', 'Paris', 'Lyon', 'Female', '+33-1-12345679', 'sophie.laurent@ecoliving.fr', 30, 'Founder');

INSERT INTO investors (startup_id, investor_name, passport_id) VALUES
(1, 'John Peterson', 'USINV000001'),
(2, 'Aarav Choudhury', 'ININV000002'),
(3, 'James Smith', 'UKINV000003'),
(4, 'Markus Wagner', 'DEINV000004'),
(5, 'Emily Johnson', 'AUINV000005'),
(6, 'Sophie McDonald', 'CAINV000006'),
(7, 'David Cohen', 'ILINV000007'),
(8, 'Thabo Maseko', 'ZAINV000008'),
(9, 'Kenji Yamamoto', 'JPINV000009'),
(10, 'Ana Rodrigues', 'BRINV000010'),
(11, 'Robert Miller', 'USINV000011'),
(12, 'Klaus Schmidt', 'DEINV000012'),
(13, 'Priya Gupta', 'ININV000013'),
(14, 'Li Wei Tan', 'SGINV000014'),
(15, 'Oliver Brown', 'UKINV000015'),
(16, 'Daniel Thompson', 'CAINV000016'),
(17, 'Charlotte Davis', 'AUINV000017'),
(18, 'Karen Johnson', 'USINV000018'),
(19, 'Maarten de Vries', 'NLINV000019'),
(20, 'Claire Dubois', 'FRINV000020'),
(21, 'Rohit Agarwal', 'ININV000021'),
(22, 'Min-su Park', 'KRINV000022'),
(23, 'Laura Robinson', 'USINV000023'),
(24, 'Sipho Ndlovu', 'ZAINV000024'),
(25, 'Eva Becker', 'DEINV000025'),
(26, 'Ravi Sharma', 'ININV000026'),
(27, 'Benjamin Clarke', 'AUINV000027'),
(28, 'Charlotte White', 'UKINV000028'),
(29, 'Jason Lee', 'USINV000029'),
(30, 'Amelie Moreau', 'FRINV000030');

INSERT INTO board_members (startup_id, member_name, passport_id)
VALUES
(1, 'John Smith', 'US100000001'),
(1, 'Maria Johnson', 'US100000002'),

(2, 'Arjun Singh', 'IN200000001'),
(2, 'Priya Chakraborty', 'IN200000002'),

(3, 'James Brown', 'UK300000001'),
(3, 'Olivia Wilson', 'UK300000002'),

(4, 'Lukas Becker', 'DE400000001'),
(4, 'Hannah Schneider', 'DE400000002'),

(5, 'Ethan Clark', 'AU500000001'),
(5, 'Sophie Miller', 'AU500000002'),

(6, 'Liam Anderson', 'CA600000001'),
(6, 'Ava Thompson', 'CA600000002'),

(7, 'Noam Cohen', 'IL700000001'),
(7, 'Miriam Levi', 'IL700000002'),

(8, 'Sibusiso Dlamini', 'ZA800000001'),
(8, 'Naledi Molefe', 'ZA800000002'),

(9, 'Hiroshi Yamamoto', 'JP900000001'),
(9, 'Yuki Tanaka', 'JP900000002'),

(10, 'Gabriel Silva', 'BR100000001'),
(10, 'Mariana Rocha', 'BR100000002'),

(11, 'Daniel Robinson', 'US110000001'),
(11, 'Laura Davis', 'US110000002'),

(12, 'Maximilian Braun', 'DE120000001'),
(12, 'Anna Fischer', 'DE120000002'),

(13, 'Rohan Gupta', 'IN130000001'),
(13, 'Kavita Sharma', 'IN130000002'),

(14, 'Wei Ting', 'SG140000001'),
(14, 'Aisha Lim', 'SG140000002'),

(15, 'Thomas Davies', 'UK150000001'),
(15, 'Emily Harris', 'UK150000002'),

(16, 'William Martin', 'CA160000001'),
(16, 'Olivia Kim', 'CA160000002'),

(17, 'Benjamin White', 'AU170000001'),
(17, 'Grace Jones', 'AU170000002'),

(18, 'Michael Clark', 'US180000001'),
(18, 'Victoria Perez', 'US180000002'),

(19, 'Daan Jansen', 'NL190000001'),
(19, 'Sanne Bakker', 'NL190000002'),

(20, 'Antoine Dupont', 'FR200000001'),
(20, 'Camille Leroy', 'FR200000002'),

(21, 'Vishal Desai', 'IN210000001'),
(21, 'Nisha Verma', 'IN210000002'),

(22, 'Kim Min-Soo', 'KR220000001'),
(22, 'Park Ji-Young', 'KR220000002'),

(23, 'Christopher Lee', 'US230000001'),
(23, 'Julia Jackson', 'US230000002'),

(24, 'Mpumi Ndlovu', 'ZA240000001'),
(24, 'Zanele Khumalo', 'ZA240000002'),

(25, 'Johann Meyer', 'DE250000001'),
(25, 'Katrin Vogel', 'DE250000002'),

(26, 'Amit Bose', 'IN260000001'),
(26, 'Sarita Kulkarni', 'IN260000002'),

(27, 'Oliver Wood', 'AU270000001'),
(27, 'Chloe Parker', 'AU270000002'),

(28, 'Charlie Walker', 'UK280000001'),
(28, 'Megan Evans', 'UK280000002'),

(29, 'Jessica Robinson', 'US290000001'),
(29, 'David Anderson', 'US290000002'),

(30, 'Julien Morel', 'FR300000001'),
(30, 'Elodie Caron', 'FR300000002');

INSERT INTO sustainability (startup_id, goals, impact, social_contribution)
VALUES
(1, 'Reduce carbon emissions in solar panel production by 20%', 'Lower environmental footprint and cleaner energy supply', 'Empowering local communities with affordable green technology'),
(2, 'Improve crop yields through sustainable irrigation', 'Healthier soil and increased food security', 'Supporting small-scale farmers with eco-friendly solutions'),
(3, 'Enhance financial inclusion with eco-focused fintech products', 'Reduced inequality and resource-efficient capital flows', 'Offering low-interest microloans for green projects'),
(4, 'Develop AI-based diagnostics to minimize waste in healthcare', 'More efficient healthcare delivery and reduced resource usage', 'Improving patient outcomes in underserved regions'),
(5, 'Expand digital learning tools that lower paper consumption', 'Reduced deforestation and improved education quality', 'Providing affordable online courses for underprivileged students'),
(6, 'Implement vertical farming to reduce land and water usage', 'Increased urban food production with minimal footprints', 'Partnering with local communities to ensure fresh produce access'),
(7, 'Integrate cyber solutions that protect clean-tech IP', 'Safeguarding green innovations and investments', 'Educating small organizations on digital security best practices'),
(8, 'Create water purification systems with recyclable materials', 'Cleaner drinking water and reduced plastic waste', 'Donating filtration systems to rural communities'),
(9, 'Optimize robotics manufacturing for energy efficiency', 'Lower energy consumption and reduced production costs', 'Mentoring STEM students in sustainable robotics design'),
(10, 'Promote foodtech solutions that minimize packaging waste', 'Less landfill waste and improved nutrition access', 'Collaborating with local NGOs to provide healthy meals'),
(11, 'Advance aerospace research focusing on reusable components', 'Decreased space debris and lower resource depletion', 'Offering scholarships in environmental engineering fields'),
(12, 'Increase solar panel efficiency to reduce resource usage', 'More renewable energy and lower carbon footprint', 'Training local technicians in solar maintenance and repair'),
(13, 'Accelerate biotech research for eco-friendly healthcare', 'Reduced chemical runoff and safer pharmaceuticals', 'Donating a portion of profits to health initiatives in low-income areas'),
(14, 'Expand EdTech that reduces paper-based materials', 'Lower environmental impact of education materials', 'Offering free e-learning tools in disadvantaged schools'),
(15, 'Improve urban planning solutions to preserve green spaces', 'Healthier city environments and biodiversity conservation', 'Working with municipalities to create community gardens'),
(16, 'Use AI to optimize hospital resource management', 'Lower medical waste and efficient healthcare delivery', 'Providing free health workshops for local communities'),
(17, 'Enhance marine tech to clean and protect ocean ecosystems', 'Reduced ocean pollution and healthier marine life', 'Supporting coastal communities with clean-up initiatives'),
(18, 'Develop AI models that lower energy use in data centers', 'Less power consumption and minimized carbon footprint', 'Sponsoring energy-saving competitions in schools'),
(19, 'Increase agricultural output with minimal fertilizer', 'Reduced chemical runoff and sustainable food supply', 'Training farmers in organic methods and fair trade practices'),
(20, 'Optimize transportation routes to cut fuel consumption', 'Lower air pollution and improved logistics efficiency', 'Offering subsidized transport for low-income communities'),
(21, 'Enhance healthcare accessibility with lower resource use', 'Better patient outcomes with reduced waste', 'Donating medical supplies to community clinics'),
(22, 'Improve urban planning with efficient public transportation', 'Less congestion, reduced emissions, healthier lifestyles', 'Collaborating on affordable transit passes for low-income citizens'),
(23, 'Advance robotics to streamline recycling processes', 'Increased recycling rates and reduced landfill use', 'Educating youth about responsible waste management'),
(24, 'Increase renewable energy output in water treatment', 'Lower dependence on fossil fuels and cleaner drinking water', 'Donating clean water solutions to drought-affected areas'),
(25, 'Develop smart grid tech to optimize electricity distribution', 'Reduced energy loss and lower carbon emissions', 'Providing free workshops on energy conservation'),
(26, 'Enhance sustainable agriculture techniques at scale', 'Less pesticide use and healthier ecosystems', 'Supporting local cooperatives with eco-friendly seeds'),
(27, 'Improve marine tech to restore coral reefs', 'Healthier marine ecosystems and biodiversity restoration', 'Partnering with NGOs on coastal restoration projects'),
(28, 'Advance biotech solutions to lower environmental impact', 'Reduced chemical use and sustainable drug production', 'Funding research scholarships in environmental biotech'),
(29, 'Design urban safety measures that run on green energy', 'Safer communities with minimal ecological footprint', 'Offering training for community-led environmental surveillance'),
(30, 'Use eco-friendly materials in interior design products', 'Less chemical pollution and sustainable home solutions', 'Donating furniture to low-income housing programs');


