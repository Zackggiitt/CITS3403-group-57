// Exercise Data
const WORKOUT_PLAN_API_URL = '/api/workout_plan';

const exercises = {
    chest: [
        {
            name: "Bench Press",
            image: "https://images.pexels.com/photos/3837757/pexels-photo-3837757.jpeg",
            video: "https://www.youtube.com/embed/rT7DgCr-3pg",
            instructions: "1. Lie on bench with feet flat\n2. Grip bar slightly wider than shoulders\n3. Lower bar to mid-chest\n4. Press up until arms are straight",
            muscles: "Pectoralis Major, Triceps, Anterior Deltoids",
            calories: 10
        },
        {
            name: "Dumbbell Bench Press",
            image: "https://images.pexels.com/photos/7289233/pexels-photo-7289233.jpeg",
            video: "https://www.youtube.com/embed/VmB1G1K7v94",
            instructions: "1. Lie on bench with dumbbells at chest\n2. Press dumbbells up until arms straight\n3. Lower with control\n4. Keep wrists straight",
            muscles: "Pectoralis Major, Triceps, Anterior Deltoids",
            calories: 8
        },
        {
            name: "Incline Bench Press",
            image: "https://images.pexels.com/photos/18060077/pexels-photo-18060077/free-photo-of-muscular-man-lifting-dumbbells-on-a-weight-bench.jpeg",
            video: "https://www.youtube.com/embed/8iPEnn-ltC8",
            instructions: "1. Set bench to 30-45 degree angle\n2. Grip bar slightly wider than shoulders\n3. Lower bar to upper chest\n4. Press up until arms straight",
            muscles: "Upper Pectoralis, Anterior Deltoids",
            calories: 9
        },
        {
            name: "Decline Bench Press",
            image: "https://images.pexels.com/photos/209717/pexels-photo-209717.jpeg",
            video: "https://www.youtube.com/embed/LfyQBUKR8SE",
            instructions: "1. Set bench to 15-30 degree decline\n2. Grip bar slightly wider than shoulders\n3. Lower bar to lower chest\n4. Press up until arms straight",
            muscles: "Lower Pectoralis, Triceps",
            calories: 9
        },
        {
            name: "Dumbbell Flyes",
            image: "https://images.pexels.com/photos/11433059/pexels-photo-11433059.jpeg",
            video: "https://www.youtube.com/embed/eozdVDA78K0",
            instructions: "1. Lie on bench with dumbbells above chest\n2. Lower arms in arc motion\n3. Keep slight bend in elbows\n4. Return to start position",
            muscles: "Pectoralis Major, Anterior Deltoids",
            calories: 7
        },
        {
            name: "Chest Press Machine",
            image: "https://images.pexels.com/photos/6539839/pexels-photo-6539839.jpeg",
            video: "https://www.youtube.com/watch?v=sqNwDkUU_Ps",
            instructions: "1. Adjust seat height\n2. Grip handles at chest level\n3. Press handles forward\n4. Control return to start",
            muscles: "Pectoralis Major, Triceps",
            calories: 8
        },
        {
            name: "Pec Deck / Chest Fly Machine",
            image: "https://images.pexels.com/photos/18060022/pexels-photo-18060022/free-photo-of-muscular-man-exercising-on-the-peck-deck-machine-at-the-gym.jpeg",
            video: "https://www.youtube.com/watch?v=Z57CtFmRMxA",
            instructions: "1. Adjust seat height\n2. Place forearms on pads\n3. Bring arms together\n4. Control return to start",
            muscles: "Pectoralis Major, Anterior Deltoids",
            calories: 7
        },
        {
            name: "Dips for Chest",
            image: "https://images.pexels.com/photos/4803712/pexels-photo-4803712.jpeg",
            video: "https://www.youtube.com/embed/2z8JmcrW-As",
            instructions: "1. Support body on parallel bars\n2. Lean forward slightly\n3. Lower body until shoulders below elbows\n4. Push back up",
            muscles: "Lower Pectoralis, Triceps, Anterior Deltoids",
            calories: 9
        },
        {
            name: "Push-ups",
            image: "https://images.pexels.com/photos/176782/pexels-photo-176782.jpeg",
            video: "https://www.youtube.com/embed/IODxDxX7oi4",
            instructions: "1. Start in plank position\n2. Lower body until chest nearly touches ground\n3. Push back up to start\n4. Keep core engaged",
            muscles: "Pectoralis Major, Triceps, Core",
            calories: 6
        },
        {
            name: "Incline Push-ups",
            image: "https://images.pexels.com/photos/4803927/pexels-photo-4803927.jpeg",
            video: "https://www.youtube.com/watch?v=cfns5VDVVvk",
            instructions: "1. Place hands on elevated surface\n2. Keep body straight\n3. Lower chest to surface\n4. Push back up",
            muscles: "Upper Pectoralis, Triceps, Core",
            calories: 5
        }
    ],
    back: [
        {
            name: "Pull-ups",
            image: "https://images.pexels.com/photos/791764/pexels-photo-791764.jpeg",
            video: "https://www.youtube.com/embed/eGo4IYlbE5g",
            instructions: "1. Hang from bar with overhand grip\n2. Pull body up until chin clears bar\n3. Lower with control\n4. Keep core engaged",
            muscles: "Latissimus Dorsi, Biceps, Trapezius",
            calories: 10
        },
        {
            name: "Lat Pulldown",
            image: "https://images.pexels.com/photos/3838697/pexels-photo-3838697.jpeg",
            video: "https://www.youtube.com/watch?v=SALxEARiMkw",
            instructions: "1. Sit with thighs under pads\n2. Pull bar to upper chest\n3. Control return to start\n4. Keep chest up",
            muscles: "Latissimus Dorsi, Biceps, Trapezius",
            calories: 7
        },
        {
            name: "Barbell Row",
            image: "https://images.pexels.com/photos/3025027/pexels-photo-3025027.png",
            video: "https://www.youtube.com/watch?v=FWJR5Ve8bnQ",
            instructions: "1. Bend at hips with back straight\n2. Pull barbell to lower chest\n3. Lower with control\n4. Keep core engaged",
            muscles: "Latissimus Dorsi, Rhomboids, Trapezius",
            calories: 9
        },
        {
            name: "Dumbbell Row",
            image: "https://images.pexels.com/photos/13106577/pexels-photo-13106577.jpeg",
            video: "https://www.youtube.com/embed/roCP6wCXPqo",
            instructions: "1. Place hand and knee on bench\n2. Pull dumbbell to hip\n3. Lower with control\n4. Keep back straight",
            muscles: "Latissimus Dorsi, Rhomboids, Trapezius",
            calories: 8
        },
        {
            name: "Seated Cable Row",
            image: "https://images.pexels.com/photos/6551053/pexels-photo-6551053.jpeg",
            video: "https://www.youtube.com/embed/GZbfZ033f74",
            instructions: "1. Sit with feet on platform\n2. Pull handle to abdomen\n3. Squeeze shoulder blades\n4. Control return",
            muscles: "Latissimus Dorsi, Rhomboids, Trapezius",
            calories: 7
        },
        {
            name: "T-Bar/Landmine Row",
            image: "https://images.pexels.com/photos/209717/pexels-photo-209717.jpeg",
            video: "https://www.youtube.com/watch?v=hYo72r8Ivso",
            instructions: "1. Stand over T-bar\n2. Pull weight to chest\n3. Lower with control\n4. Keep back straight",
            muscles: "Latissimus Dorsi, Rhomboids, Trapezius",
            calories: 9
        },
        {
            name: "Deadlift",
            image: "https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg",
            video: "https://www.youtube.com/embed/1ZXobu7JvvE",
            instructions: "1. Stand with feet hip-width\n2. Bend at hips and knees\n3. Lift bar by extending hips\n4. Lower with control",
            muscles: "Hamstrings, Glutes, Lower Back",
            calories: 15
        },
        {
            name: "Reverse Flyes",
            image: "https://images.pexels.com/photos/209717/pexels-photo-209717.jpeg",
            video: "https://www.youtube.com/embed/eaTpDgG2Lug",
            instructions: "1. Bend at hips with dumbbells\n2. Raise arms to sides\n3. Squeeze shoulder blades\n4. Lower with control",
            muscles: "Rear Deltoids, Trapezius, Rhomboids",
            calories: 6
        },
        {
            name: "Superman",
            image: "https://images.pexels.com/photos/209717/pexels-photo-209717.jpeg",
            video: "https://www.youtube.com/embed/cc6UVRS7PW4",
            instructions: "1. Lie face down\n2. Lift arms and legs\n3. Hold position\n4. Lower with control",
            muscles: "Lower Back, Glutes, Hamstrings",
            calories: 4
        },
        {
            name: "Face Pull",
            image: "https://images.pexels.com/photos/6740311/pexels-photo-6740311.jpeg",
            video: "https://www.youtube.com/embed/rep-qVOkqgk",
            instructions: "1. Use rope attachment on cable\n2. Pull towards face\n3. Squeeze shoulder blades\n4. Control return",
            muscles: "Rear Deltoids, Trapezius, Rhomboids",
            calories: 5
        }
    ],
    shoulders: [
        {
            name: "Lateral Raises",
            image: "https://images.pexels.com/photos/5327460/pexels-photo-5327460.jpeg",
            video: "https://www.youtube.com/watch?v=OuG1smZTsQQ",
            instructions: "1. Hold dumbbells at sides\n2. Raise arms to shoulder height\n3. Lower with control\n4. Keep slight bend in elbows",
            muscles: "Lateral Deltoids, Trapezius",
            calories: 6
        },
        {
            name: "Front Raises",
            image: "https://media.istockphoto.com/id/1354524863/photo/portrait-of-fit-muscular-sport-man-doing-front-shoulder-exercise-with-resistance-band-on.jpg?s=1024x1024&w=is&k=20&c=pB7RFrSQenY-k1s5tiWtkcLQLlYoNnGPK4nK31_f97M=",
            video: "https://www.youtube.com/embed/-t7fuZ0KhDA",
            instructions: "1. Hold dumbbells in front\n2. Raise arms to shoulder height\n3. Lower with control\n4. Keep slight bend in elbows",
            muscles: "Anterior Deltoids, Upper Chest",
            calories: 6
        },
        {
            name: "Dumbbell Shoulder Press",
            image: "https://images.pexels.com/photos/7289236/pexels-photo-7289236.jpeg",
            video: "https://www.youtube.com/embed/qEwKCR5JCog",
            instructions: "1. Hold dumbbells at shoulders\n2. Press overhead until arms straight\n3. Lower with control\n4. Keep core tight",
            muscles: "Deltoids, Triceps, Upper Chest",
            calories: 8
        },
        {
            name: "Barbell Overhead Press",
            image: "https://images.pexels.com/photos/17944268/pexels-photo-17944268/free-photo-of-man-lifting-weights.jpeg",
            video: "https://www.youtube.com/embed/2yjwXTZQDDI",
            instructions: "1. Hold barbell at shoulder level\n2. Press overhead until arms straight\n3. Lower with control\n4. Keep core tight",
            muscles: "Deltoids, Triceps, Upper Chest",
            calories: 9
        },
        {
            name: "Arnold Press",
            image: "https://images.pexels.com/photos/6922175/pexels-photo-6922175.jpeg",
            video: "https://www.youtube.com/watch?v=6Z15_WdXmVw",
            instructions: "1. Start with palms facing you\n2. Rotate arms as you press\n3. Lower with rotation\n4. Keep core tight",
            muscles: "Deltoids, Triceps, Upper Chest",
            calories: 8
        },
        {
            name: "Dumbbell Shrugs",
            image: "https://media.istockphoto.com/id/1222441366/photo/filipino-man-working-out-at-home.jpg?s=1024x1024&w=is&k=20&c=-6Q7f-17k8b7sCV5Z7t92HDBujdtRq-36VZgdONGfB8=",
            video: "https://www.youtube.com/embed/cJRVVxmytaM",
            instructions: "1. Hold dumbbells at sides\n2. Raise shoulders to ears\n3. Hold at top\n4. Lower with control",
            muscles: "Trapezius, Upper Back",
            calories: 5
        },
        {
            name: "Upright Row",
            image: "https://media.istockphoto.com/id/179115981/photo/man-illustrating-how-to-do-a-dumbbell-upright-row-exercise.jpg?s=1024x1024&w=is&k=20&c=HH1AM0LaWM26ebxU0Oikt3Y5n81Yq0uGQRt2LYoEQLo=",
            video: "https://www.youtube.com/embed/amCU-ziHITM",
            instructions: "1. Hold barbell with narrow grip\n2. Pull bar to chin\n3. Keep elbows high\n4. Lower with control",
            muscles: "Deltoids, Trapezius, Biceps",
            calories: 7
        },
        {
            name: "Reverse Flyes",
            image: "https://images.pexels.com/photos/209717/pexels-photo-209717.jpeg",
            video: "https://www.youtube.com/embed/eaTpDgG2Lug",
            instructions: "1. Bend at hips with dumbbells\n2. Raise arms to sides\n3. Squeeze shoulder blades\n4. Lower with control",
            muscles: "Rear Deltoids, Trapezius, Rhomboids",
            calories: 6
        }
    ],
    arms: {
        biceps: [
            {
                name: "Bicep Curls",
                image: "https://images.pexels.com/photos/6922180/pexels-photo-6922180.jpeg",
                video: "https://www.youtube.com/embed/ykJmrZ5v0Oo",
                instructions: [
                    "Stand with feet shoulder-width apart",
                    "Hold dumbbells at your sides, palms facing forward",
                    "Keep your upper arms stationary",
                    "Curl the weights up towards your shoulders",
                    "Slowly lower the weights back down",
                    "Maintain control throughout the movement"
                ],
                muscles: ["Biceps Brachii", "Brachialis"],
                calories: 3.5
            },
            {
                name: "Barbell Curl",
                image: "https://images.pexels.com/photos/5327467/pexels-photo-5327467.jpeg",
                video: "https://www.youtube.com/embed/kwG2ipFRgfo",
                instructions: "1. Hold barbell with underhand grip\n2. Curl bar to shoulders\n3. Lower with control\n4. Keep elbows close to body",
                muscles: "Biceps Brachii, Brachialis",
                calories: 6
            },
            {
                name: "Seated Alternating Curl",
                image: "https://images.pexels.com/photos/6550874/pexels-photo-6550874.jpeg",
                video: "https://www.youtube.com/embed/soxrZlIl35U",
                instructions: "1. Sit on bench with dumbbells\n2. Alternate curling each arm\n3. Keep back straight\n4. Control movement",
                muscles: "Biceps Brachii, Brachialis",
                calories: 5
            },
            {
                name: "Preacher Curl",
                image: "https://media.istockphoto.com/id/513435166/photo/young-man-in-a-preacher-bench-at-the-gym.jpg?s=1024x1024&w=is&k=20&c=BDaDNpye4IBVhvby4HUH19hLBmqp6KvE7T5uq5jdgoE=",
                video: "https://www.youtube.com/embed/fIWP-FRFNU0",
                instructions: "1. Rest arms on preacher bench\n2. Curl weight up\n3. Lower with control\n4. Keep back straight",
                muscles: "Biceps Brachii, Brachialis",
                calories: 6
            },
            {
                name: "Close-grip Lat Pulldown for Biceps",
                image: "https://images.pexels.com/photos/6922157/pexels-photo-6922157.jpeg",
                video: "https://www.youtube.com/watch?v=IjoFCmLX7z0",
                instructions: "1. Use close grip attachment\n2. Pull bar to chest\n3. Focus on biceps\n4. Control return",
                muscles: "Biceps Brachii, Brachialis",
                calories: 7
            }
        ],
        triceps: [
            {
                name: "Close-grip Bench Press",
                image: "https://images.pexels.com/photos/7289233/pexels-photo-7289233.jpeg",
                video: "https://www.youtube.com/watch?v=FiQUzPtS90E",
                instructions: [
                    "Lie on bench with narrow grip on barbell",
                    "Grip should be shoulder-width or slightly closer",
                    "Lower bar to lower chest",
                    "Keep elbows close to body throughout",
                    "Press bar back up to starting position",
                    "Maintain controlled movement"
                ],
                muscles: "Triceps Brachii, Pectoralis Major",
                calories: 4
            },
            {
                name: "Tricep Pushdown",
                image: "https://images.pexels.com/photos/6243176/pexels-photo-6243176.jpeg",
                video: "https://www.youtube.com/embed/2-LAMcpzODU",
                instructions: [
                    "Stand facing a cable machine with high pulley",
                    "Grab the rope or bar attachment",
                    "Keep elbows close to your sides",
                    "Push the weight down until arms are fully extended",
                    "Slowly return to starting position",
                    "Maintain control throughout"
                ],
                muscles: "Triceps Brachii",
                calories: 3
            },
            {
                name: "Skull Crushers",
                image: "https://images.pexels.com/photos/209717/pexels-photo-209717.jpeg",
                video: "https://www.youtube.com/embed/d_KZxkY_0cM",
                instructions: [
                    "Lie on a bench with dumbbells or barbell",
                    "Hold weights above chest with arms extended",
                    "Lower weights toward your forehead",
                    "Keep elbows pointing toward ceiling",
                    "Extend arms back up to starting position",
                    "Maintain controlled movement throughout"
                ],
                muscles: "Triceps Brachii",
                calories: 3.5
            },
            {
                name: "One-arm Dumbbell Overhead Extension",
                image: "https://media.istockphoto.com/id/182879154/photo/skull-crusher-dumbbell-weight-training-male.jpg?s=1024x1024&w=is&k=20&c=Gm6Oetv1lOvjUq7NIvTJo-4Mhp1I43aPlu9XI13O9oo=",
                video: "https://www.youtube.com/watch?v=YM8iX9BJWjA",
                instructions: "1. Hold dumbbell overhead\n2. Lower behind head\n3. Extend arm\n4. Keep elbow stationary",
                muscles: "Triceps",
                calories: 5
            },
            {
                name: "Dips",
                image: "https://images.pexels.com/photos/8520040/pexels-photo-8520040.jpeg",
                video: "https://www.youtube.com/embed/2z8JmcrW-As",
                instructions: "1. Support body on parallel bars\n2. Lower body by bending elbows\n3. Push back up\n4. Keep elbows close",
                muscles: "Triceps, Chest, Shoulders",
                calories: 7
            }
        ]
    },
    legs: [
        {
            name: "Squats",
            image: "https://images.pexels.com/photos/8032778/pexels-photo-8032778.jpeg",
            video: "https://www.youtube.com/embed/aclHkVaku9U",
            instructions: "1. Stand with feet shoulder-width\n2. Lower body by bending knees\n3. Keep chest up and back straight\n4. Push through heels to stand",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 12
        },
        {
            name: "Barbell Back Squat",
            image: "https://images.pexels.com/photos/371049/pexels-photo-371049.jpeg",
            video: "https://www.youtube.com/embed/SW_C1A-rejs",
            instructions: "1. Place bar on upper back\n2. Lower body until thighs parallel\n3. Keep chest up\n4. Push through heels",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 15
        },
        {
            name: "Dumbbell Squat",
            image: "https://media.istockphoto.com/id/941210268/photo/close-up-view-of-focussed-hardworking-active-fitness-strong-muscular-bearded-bodybuilder-man.jpg?s=1024x1024&w=is&k=20&c=MquC132EFZk7U6zjl2WxE1RWb3DiLELWhc8H3nOw0OU=",
            video: "https://www.youtube.com/watch?v=v_c67Omje48",
            instructions: "1. Hold dumbbells at sides\n2. Lower body until thighs parallel\n3. Keep chest up\n4. Push through heels",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 10
        },
        {
            name: "Bulgarian Split Squat",
            image: "https://images.pexels.com/photos/209717/pexels-photo-209717.jpeg",
            video: "https://www.youtube.com/embed/2C-uNgKwPLE",
            instructions: "1. Place back foot on bench\n2. Lower body until front thigh parallel\n3. Keep chest up\n4. Push through front heel",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 8
        },
        {
            name: "Leg Press",
            image: "https://images.pexels.com/photos/136404/pexels-photo-136404.jpeg",
            video: "https://www.youtube.com/embed/IZxyjW7MPJQ",
            instructions: "1. Adjust seat position\n2. Place feet on platform\n3. Lower weight until knees at 90 degrees\n4. Push through heels",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 12
        },
        {
            name: "Lunges",
            image: "https://images.pexels.com/photos/6740294/pexels-photo-6740294.jpeg",
            video: "https://www.youtube.com/embed/QOVaHwm-Q6U",
            instructions: "1. Step forward with one leg\n2. Lower body until back knee nearly touches ground\n3. Push back to start\n4. Keep torso upright",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 8
        },
        {
            name: "Walking Lunges",
            image: "https://images.pexels.com/photos/5067743/pexels-photo-5067743.jpeg",
            video: "https://www.youtube.com/embed/L8fvypPrzzs",
            instructions: "1. Step forward into lunge\n2. Push through front heel\n3. Bring back leg forward\n4. Repeat with other leg",
            muscles: "Quadriceps, Glutes, Hamstrings",
            calories: 9
        },
        {
            name: "Leg Curl",
            image: "https://images.pexels.com/photos/209717/pexels-photo-209717.jpeg",
            video: "https://www.youtube.com/embed/1Tq3QdYUuHs",
            instructions: "1. Lie face down on machine\n2. Place ankles under pad\n3. Curl legs up\n4. Control return",
            muscles: "Hamstrings",
            calories: 6
        },
        {
            name: "Leg Extension",
            image: "https://images.pexels.com/photos/6539840/pexels-photo-6539840.jpeg",
            video: "https://www.youtube.com/embed/YyvSfVjQeL0",
            instructions: "1. Sit on machine\n2. Place ankles under pad\n3. Extend legs\n4. Control return",
            muscles: "Quadriceps",
            calories: 6
        },
        {
            name: "Romanian Deadlift",
            image: "https://media.istockphoto.com/id/1394041426/photo/woman-doing-deadlift-with-barbell.jpg?s=1024x1024&w=is&k=20&c=o8hlilCtbjyDiXqOV0ZAsWjAwHdsa7NU7BnD4wYoz2U=",
            video: "https://www.youtube.com/embed/JCXUYuzwNrM",
            instructions: "1. Hold barbell with overhand grip\n2. Hinge at hips\n3. Lower bar along legs\n4. Return to start",
            muscles: "Hamstrings, Glutes, Lower Back",
            calories: 10
        },
        {
            name: "Standing Calf Raise",
            image: "https://images.pexels.com/photos/13965339/pexels-photo-13965339.jpeg",
            video: "https://www.youtube.com/watch?v=zNcD6cq1jnM",
            instructions: "1. Stand on edge of platform\n2. Raise heels as high as possible\n3. Lower heels below platform\n4. Repeat",
            muscles: "Gastrocnemius, Soleus",
            calories: 5
        },
        {
            name: "Seated Calf Raise",
            image: "https://images.pexels.com/photos/209717/pexels-photo-209717.jpeg",
            video: "https://www.youtube.com/watch?v=2Q-HQ3mnePg",
            instructions: "1. Sit on machine\n2. Place balls of feet on platform\n3. Raise heels as high as possible\n4. Lower below platform",
            muscles: "Soleus",
            calories: 5
        }
    ],
    core: [
        {
            name: "Sit-ups",
            image: "https://images.pexels.com/photos/3076516/pexels-photo-3076516.jpeg",
            video: "https://www.youtube.com/embed/1fbU_MkV7NE",
            instructions: "1. Lie on back with knees bent\n2. Place hands behind head\n3. Curl torso up\n4. Lower with control",
            muscles: "Rectus Abdominis, Hip Flexors",
            calories: 5
        },
        {
            name: "Crunches",
            image: "https://media.istockphoto.com/id/919871194/photo/young-woman-doing-sit-ups-at-gym.jpg?s=1024x1024&w=is&k=20&c=hfkAhs2SFwJQuDYrKx0kw2FiuWo8vTFNrv-VreXiEUw=",
            video: "https://www.youtube.com/embed/Xyd_fa5zoEU",
            instructions: "1. Lie on back with legs up andknees bent\n2. Place hands behind head\n3. Lift shoulders off ground\n4. Lower with control",
            muscles: "Rectus Abdominis",
            calories: 4
        },
        {
            name: "Russian Twists",
            image: "https://images.pexels.com/photos/6455815/pexels-photo-6455815.jpeg",
            video: "https://www.youtube.com/embed/wkD8rjkodUI",
            instructions: "1. Sit with knees bent\n2. Lean back slightly\n3. Twist torso side to side\n4. Keep core engaged",
            muscles: "Obliques, Rectus Abdominis",
            calories: 5
        },
        {
            name: "Plank",
            image: "https://images.pexels.com/photos/3768901/pexels-photo-3768901.jpeg",
            video: "https://www.youtube.com/embed/pSHjTRCQxIw",
            instructions: "1. Start in push-up position\n2. Support body on forearms\n3. Keep body straight\n4. Hold position",
            muscles: "Rectus Abdominis, Transverse Abdominis, Obliques",
            calories: 4
        },
        {
            name: "Side Plank",
            image: "https://images.pexels.com/photos/4775188/pexels-photo-4775188.jpeg",
            video: "https://www.youtube.com/embed/K2VljzCC16g",
            instructions: "1. Lie on side\n2. Support body on forearm\n3. Lift hips off ground\n4. Hold position",
            muscles: "Obliques, Transverse Abdominis",
            calories: 4
        },
        {
            name: "Hanging Leg Raises",
            image: "https://images.pexels.com/photos/25315917/pexels-photo-25315917/free-photo-of-studio-portrait-of-a-man-doing-leg-raises-on-two-wooden-boxes.jpeg",
            video: "https://www.youtube.com/watch?v=RuIdJSVTKO4",
            instructions: "1. Hang from bar\n2. Raise legs to 90 degrees\n3. Lower with control\n4. Keep core engaged",
            muscles: "Lower Abs, Hip Flexors",
            calories: 6
        },
        {
            name: "Reverse Crunch",
            image: "https://images.pexels.com/photos/209717/pexels-photo-209717.jpeg",
            video: "https://www.youtube.com/watch?v=XY8KzdDcMFg",
            instructions: "1. Lie on back with legs up\n2. Lift hips off ground\n3. Lower with control\n4. Keep core engaged",
            muscles: "Lower Abs, Hip Flexors",
            calories: 5
        },
        {
            name: "Mountain Climbers",
            image: "https://media.istockphoto.com/id/1311464336/photo/sportsman-practicing-mountain-climbing-exercise.webp?s=2048x2048&w=is&k=20&c=TRuXt86jaN-TaWA00DsylM6LPwWPlBoZVaYlGdyGQlg=",
            video: "https://www.youtube.com/embed/cnyTQDSE884",
            instructions: "1. Start in push-up position\n2. Bring knee to chest\n3. Alternate legs\n4. Keep core tight",
            muscles: "Rectus Abdominis, Hip Flexors",
            calories: 7
        },
        {
            name: "Bicycle Crunches",
            image: "https://images.pexels.com/photos/8038625/pexels-photo-8038625.jpeg",
            video: "https://www.youtube.com/embed/9FGilxCbdz8",
            instructions: "1. Lie on back with hands behind head\n2. Bring opposite elbow to knee\n3. Alternate sides\n4. Keep core engaged",
            muscles: "Rectus Abdominis, Obliques",
            calories: 6
        },
        {
            name: "Leg Raises",
            image: "https://media.istockphoto.com/id/1213375538/photo/fit-slim-young-woman-in-tight-sportswear-black-pants-and-top-lying-on-mat-keeping-straight.jpg?s=1024x1024&w=is&k=20&c=GSLAacSvaXtXYo6jAsel1kBQKCNsjUf78lnLAyC6QR8=",
            video: "https://www.youtube.com/embed/l4kQd9eWclE",
            instructions: "1. Lie on back with legs straight\n2. Raise legs to 90 degrees\n3. Lower with control\n4. Keep lower back pressed to floor",
            muscles: "Lower Abs, Hip Flexors",
            calories: 6
        }
    ],
    arms: [
        {
            name: "Hammer Curls",
            image: "https://images.pexels.com/photos/5327463/pexels-photo-5327463.jpeg",
            video: "https://www.youtube.com/embed/TwD-YGVP4Bk",
            instructions: [
                "Stand with feet shoulder-width apart",
                "Hold dumbbells at your sides, palms facing each other",
                "Keep your upper arms stationary",
                "Curl the weights up towards your shoulders",
                "Maintain neutral grip throughout",
                "Lower weights back down with control"
            ],
            muscles: ["Biceps Brachii", "Brachialis", "Brachioradialis"],
            calories: 3.5
        },
        {
            name: "Preacher Curl",
            image: "https://media.istockphoto.com/id/513435166/photo/young-man-in-a-preacher-bench-at-the-gym.jpg?s=1024x1024&w=is&k=20&c=BDaDNpye4IBVhvby4HUH19hLBmqp6KvE7T5uq5jdgoE=",
            video: "https://www.youtube.com/embed/fIWP-FRFNU0",
            instructions: "1. Rest arms on preacher bench\n2. Curl weight up\n3. Lower with control\n4. Keep back straight",
            muscles: "Biceps Brachii, Brachialis",
            calories: 6
        },
        {
            name: "Concentration Curls",
            image: "https://images.pexels.com/photos/5837271/pexels-photo-5837271.jpeg",
            video: "https://www.youtube.com/embed/Jvj2wV0vOYU",
            instructions: "1. Sit with elbow on inner thigh\n2. Curl weight up\n3. Squeeze at top\n4. Lower with control",
            muscles: "Biceps Brachii",
            calories: 5
        },
        {
            name: "Zottman Curls",
            image: "https://images.pexels.com/photos/209717/pexels-photo-209717.jpeg",
            video: "https://www.youtube.com/embed/ZrpRBgswtHs",
            instructions: [
                "Stand with dumbbells at your sides",
                "Perform regular bicep curl",
                "At the top, rotate wrists 180 degrees",
                "Lower weights with reverse grip",
                "Rotate back to starting position",
                "Keep core engaged throughout"
            ],
            muscles: ["Biceps Brachii", "Brachialis", "Forearm Flexors"],
            calories: 3.5
        },
        {
            name: "Rope Tricep Extension",
            image: "https://images.pexels.com/photos/10551496/pexels-photo-10551496.jpeg",
            video: "https://www.youtube.com/embed/kiuVA0gs3EI",
            instructions: [
                "Face away from cable machine",
                "Hold rope attachment overhead",
                "Keep upper arms stationary",
                "Extend forearms forward",
                "Slowly return to starting position",
                "Maintain tension throughout movement"
            ],
            muscles: ["Triceps Brachii"],
            calories: 3
        }
    ]
};

// Initialize the page
document.addEventListener('DOMContentLoaded', function () {
    // loadExercises();
    initializeCalorieChart();
    setupEventListeners();
    initializeCalorieCalculator();
    
    // Load real workout plan data
    loadWorkoutPlan().catch(error => {
        console.error("Error loading workout plan:", error);
    });

    // Load saved workout data
    loadSavedWorkout().catch(error => {
        console.error("Error loading saved workout:", error);
    });
});

// Load exercises into the grid
function loadExercises(category = 'all') {
    const container = document.getElementById('exercises-container');
    container.innerHTML = '';

    let exercisesToShow = [];
    if (category === 'all') {
        Object.values(exercises).forEach(categoryExercises => {
            exercisesToShow = exercisesToShow.concat(categoryExercises);
        });
    } else {
        exercisesToShow = exercises[category] || [];
    }

    exercisesToShow.forEach(exercise => {
        const card = createExerciseCard(exercise);
        container.appendChild(card);
    });
}

// Create exercise card element
function createExerciseCard(exercise) {
    const card = document.createElement('div');
    card.className = 'exercise-card';

    // Create the card content
    card.innerHTML = `
        <div class="exercise-image-container">
            <img src="${exercise.image}" alt="${exercise.name}" class="exercise-image">
            <div class="exercise-overlay">
                <button class="view-details-btn">View Details</button>
            </div>
        </div>
        <div class="exercise-card-content">
            <h3>${exercise.name}</h3>
            <p class="exercise-muscles">${Array.isArray(exercise.muscles) ? exercise.muscles.join(', ') : exercise.muscles}</p>
            <p class="exercise-calories">${exercise.calories} calories/set</p>
        </div>
    `;

    // Add click event to the entire card
    card.addEventListener('click', function () {
        showExerciseModal(exercise);
    });

    return card;
}

// Initialize calorie chart
function initializeCalorieChart() {
    const ctx = document.getElementById('calorieChart');
    if (!ctx) {
        console.error('Chart canvas element not found');
        return;
    }
    
    // Ensure Chart.js library is loaded
    if (typeof Chart === 'undefined') {
        console.error('Chart.js library is not loaded, chart cannot be initialized');
        return;
    }
    
    // If a chart instance already exists, destroy it first
    if (window.calorieChart instanceof Chart) {
        window.calorieChart.destroy();
        console.log('Destroyed existing chart instance');
    }
    
    // Initialize empty data
    const initialData = [0, 0, 0, 0, 0, 0, 0];
    
    try {
    const chart = new Chart(ctx, {
        type: 'bar',
        data: {
                labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            datasets: [{
                label: 'Calories Burned',
                    data: initialData,
                    backgroundColor: 'rgba(76, 175, 80, 0.8)',
                borderColor: 'rgba(76, 175, 80, 1)',
                    borderWidth: 2,
                    borderRadius: 8,
                    barThickness: 70,
                    maxBarThickness: 90
            }]
        },
        options: {
            responsive: true,
                maintainAspectRatio: false,
                layout: {
                    padding: {
                        top: 30,
                        right: 40,
                        bottom: 30, 
                        left: 30
                    }
                },
            scales: {
                y: {
                        beginAtZero: true,
                        suggestedMax: 300,
                        grid: {
                            color: 'rgba(200, 200, 200, 0.2)'
                        },
                        ticks: {
                            stepSize: 50,
                            font: {
                                size: 16,
                                weight: 'bold'
                            },
                            padding: 15,
                            callback: function(value) {
                                return value + ' cal';
                            }
                        },
                        title: {
                            display: true,
                            text: 'Calories',
                            font: {
                                size: 20,
                                weight: 'bold'
                            },
                            padding: {
                                top: 15,
                                bottom: 15
                            }
                        }
                    },
                    x: {
                        grid: {
                            display: false
                        },
                        ticks: {
                            font: {
                                size: 16,
                                weight: 'bold'
                            },
                            color: '#333',
                            padding: 20
                        }
                    }
                },
                plugins: {
                    legend: {
                        position: 'top',
                        labels: {
                            font: {
                                size: 18,
                                weight: 'bold'
                            },
                            padding: 25,
                            color: '#333'
                        }
                    },
                    tooltip: {
                        backgroundColor: 'rgba(0, 0, 0, 0.8)',
                        titleFont: {
                            size: 18,
                            weight: 'bold'
                        },
                        bodyFont: {
                            size: 16
                        },
                        padding: 18,
                        callbacks: {
                            label: function(context) {
                                return context.formattedValue + ' calories';
                            }
                        }
                    }
                },
                animation: {
                    duration: 1000,
                    easing: 'easeOutQuart'
            }
        }
    });
        
        // Save chart instance to global variable
    window.calorieChart = chart;
        
        console.log('Chart initialized successfully', chart);
        return chart;
    } catch (error) {
        console.error('Error initializing chart:', error);
        return null;
    }
}

// Calorie Calculator Functions
function initializeCalorieCalculator() {
    const calculatorForm = document.getElementById('calorie-calculator-form');
    if (calculatorForm) {
        calculatorForm.addEventListener('submit', function (e) {
            e.preventDefault();
            calculateCalories();
        });
    }
}

function calculateCalories() {
    const weight = parseFloat(document.getElementById('weight').value);
    const duration = parseFloat(document.getElementById('duration').value);
    const intensity = document.getElementById('intensity').value;

    if (isNaN(weight) || isNaN(duration)) {
        showAlert('Please enter valid weight and duration');
        return;
    }

    let caloriesPerMinute;
    switch (intensity) {
        case 'low':
            caloriesPerMinute = 3.5;
            break;
        case 'moderate':
            caloriesPerMinute = 7;
            break;
        case 'high':
            caloriesPerMinute = 10;
            break;
        default:
            caloriesPerMinute = 5;
    }

    const caloriesBurned = Math.round(caloriesPerMinute * duration * (weight / 70));
    document.getElementById('calories-result').textContent = caloriesBurned;
    document.getElementById('calories-result-container').style.display = 'block';
}

// Setup event listeners
function setupEventListeners() {
    // Category filter
    document.getElementById('category-filter').addEventListener('change', function (e) {
        loadExercises(e.target.value);
    });

    // Search filter
    document.getElementById('exercise-search').addEventListener('input', function (e) {
        const searchTerm = e.target.value.toLowerCase();
        const cards = document.querySelectorAll('.exercise-card');
        cards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            card.style.display = title.includes(searchTerm) ? 'block' : 'none';
        });
    });

    // Improved document click listener to handle exercise details and add-to-workout
    document.removeEventListener('click', handleDocumentClick); // Remove old listener if exists
    document.addEventListener('click', handleDocumentClick); // Add the new handler function

    // Close modal listener remains the same
    const closeModalButton = document.querySelector('.close-modal');
    if(closeModalButton) {
        closeModalButton.addEventListener('click', function () {
            const modal = document.getElementById('exercise-modal');
            if(modal) modal.style.display = 'none';
        });
    }

    // Calorie Calculator listener remains the same
    const calculatorForm = document.getElementById('calorie-calculator-form');
    if (calculatorForm) {
        calculatorForm.addEventListener('submit', function (e) {
            e.preventDefault();
            calculateCalories();
        });
    }
}

// Define the handler function separately for clarity
async function handleDocumentClick(e) {
    console.log("[handleDocumentClick] Click detected on:", e.target);

    // --- Handle clicks on Day Selection Buttons inside the Exercise Modal ---
    const dayButton = e.target.closest('.day-selection-container .day-button');
    if (dayButton) {
        console.log("[handleDocumentClick] Day button clicked:", dayButton.dataset.day);
        const day = dayButton.dataset.day;
        const exerciseJson = dayButton.closest('.modal-content').dataset.currentExercise; // Get data from modal content

        if (!exerciseJson) {
            console.error("[handleDocumentClick] Could not find exercise data on modal.");
            return;
        }

        try {
            const exerciseData = JSON.parse(exerciseJson);
            console.log("[handleDocumentClick] Parsed exercise data:", exerciseData);

            // Show the Sets/Reps prompt instead of directly adding
            showSetsRepsPrompt(exerciseData, day);

            // Close the main exercise modal after clicking a day button
            const exerciseModal = document.getElementById('exercise-modal');
            if (exerciseModal) {
                exerciseModal.style.display = 'none';
            }

        } catch (error) {
            console.error("[handleDocumentClick] Error parsing exercise data or adding to workout:", error);
            alert("Error processing exercise selection."); // User feedback
        }
        return; // Stop further processing if it was a day button click
    }

    // --- Handle clicks on Category Cards ---
    const categoryCard = e.target.closest('.category-card');
    if (categoryCard) {
        const category = categoryCard.dataset.category;
        console.log("[handleDocumentClick] Category card clicked:", category);
        if (category) {
            loadExercises(category);
        }
        return; // Stop further processing
    }

    // --- Handle clicks on Exercise Cards (to open modal) ---
    const exerciseCard = e.target.closest('.exercise-card');
    if (exerciseCard) {
        const exerciseJson = exerciseCard.dataset.exercise;
        console.log("[handleDocumentClick] Exercise card clicked. Data:", exerciseJson);
        if (exerciseJson) {
            try {
                const exerciseData = JSON.parse(exerciseJson);
                 openExerciseModal(exerciseData); // Pass parsed data
            } catch (error) {
                console.error("[handleDocumentClick] Error parsing exercise data from card:", error);
            }
        }
        return; // Stop further processing
    }

     // --- Handle clicks on Remove Exercise Button ---
    const removeButton = e.target.closest('.remove-exercise-btn');
    if (removeButton) {
        console.log("[handleDocumentClick] Remove button clicked.");
        const exerciseElement = removeButton.closest('.workout-exercise');
        if (exerciseElement) {
            const daySlot = exerciseElement.closest('.workout-slot');
            const day = daySlot ? daySlot.dataset.day : null;
            console.log(`[handleDocumentClick] Attempting to remove exercise from day: ${day}`);

            if (day) {
                // IMPORTANT: Remove the element *before* saving
                // This ensures saveWorkoutPlan reads the state *without* the removed item.
                exerciseElement.remove();
                console.log("[handleDocumentClick] Exercise element removed from DOM.");

                // Now save the plan which reflects the removal
                try {
                    await saveWorkoutPlan();
                    console.log(`[handleDocumentClick] Plan saved successfully after removing exercise from ${day}.`);
                    // loadWorkoutPlan is called inside saveWorkoutPlan on success, so no need here.
                } catch (error) {
                     console.error("[handleDocumentClick] Error during saveWorkoutPlan after removing exercise:", error);
                     // Optional: Add the element back if save fails? Or rely on full reload.
                     alert("Failed to update the plan after removing the exercise. Please refresh.");
                 }
            } else {
                console.warn("[handleDocumentClick] Could not determine day for removed exercise. Element removed but plan not saved.");
                 // If we couldn't find the day, just remove visually without saving.
                 exerciseElement.remove();
            }
        } else {
            console.error("[handleDocumentClick] Could not find parent '.workout-exercise' element for the remove button.");
        }
        return; // Stop further processing
    }


    // --- Handle clicks on Modal Close Buttons ---
    if (e.target.matches('.close-modal') || e.target.matches('.close-prompt-btn')) {
        console.log("[handleDocumentClick] Close button clicked.");
        const modal = e.target.closest('.modal');
        if (modal) {
            modal.style.display = 'none';
        }
        return; // Stop further processing
    }

    // --- Handle clicks outside of Modals (to close them) ---
    if (e.target.matches('.modal')) {
        console.log("[handleDocumentClick] Click outside modal content detected.");
        e.target.style.display = 'none';
        return; // Stop further processing
    }

    console.log("[handleDocumentClick] Click did not match any specific handler.");
}

// Show exercise modal
function showExerciseModal(exercise) {
    const modal = document.getElementById('exercise-modal');
    if (!modal) {
        console.error("Critical Error: Cannot find modal element #exercise-modal");
        return;
    }
    modal.dataset.exerciseData = JSON.stringify(exercise);

    // --- Populate Modal Content ---
    document.getElementById('modal-exercise-name').textContent = exercise.name;
    const instructions = Array.isArray(exercise.instructions) ? exercise.instructions.join('\\n') : exercise.instructions;
    document.getElementById('modal-exercise-instructions').textContent = instructions;
    const muscles = Array.isArray(exercise.muscles) ? exercise.muscles.join(', ') : exercise.muscles;
    document.getElementById('modal-exercise-muscles').textContent = muscles;
    document.getElementById('modal-exercise-calories').textContent = `${exercise.calories} calories per set`;

    const videoIframe = document.getElementById('exercise-video');
    const imageContainer = modal.querySelector('.exercise-video');
    if (imageContainer) {
        imageContainer.innerHTML = ''; // Clear previous content
        if (exercise.video && exercise.video.trim() !== '') {
             let videoId;
             try {
                 if (exercise.video.includes('youtube.com/embed/')) {
                     videoId = exercise.video.split('/').pop().split('?')[0]; // Extract from embed URL
                 } else if (exercise.video.includes('youtube.com/watch?v=')) {
            const url = new URL(exercise.video);
                     videoId = url.searchParams.get('v'); // Extract from watch URL
    } else {
                     // Assume it's just the ID if not a standard YouTube URL
                     videoId = exercise.video;
                 }
                 if (videoId) {
                     const iframe = document.createElement('iframe');
                     iframe.src = `https://www.youtube.com/embed/${videoId}`;
                     iframe.className = 'modal-exercise-video'; // Reuse class for consistency
                     iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
                     iframe.allowFullscreen = true;
                     imageContainer.appendChild(iframe);
                 } else if (exercise.image) { // Fallback to image if video processing fails or no ID found
                     const modalImage = document.createElement('img');
                     modalImage.src = exercise.image;
                     modalImage.alt = exercise.name;
                     modalImage.className = 'modal-exercise-image'; // Use a different class if needed for styling
                     imageContainer.appendChild(modalImage);
                 }
            } catch (e) {
                 console.error("Error processing video URL, falling back to image:", e);
                 // Fallback to image if URL parsing fails
                 if (exercise.image) {
    const modalImage = document.createElement('img');
    modalImage.src = exercise.image;
    modalImage.alt = exercise.name;
    modalImage.className = 'modal-exercise-image';
    imageContainer.appendChild(modalImage);
                 }
             }
        } else if (exercise.image) { // If no video provided, use image
            const modalImage = document.createElement('img');
            modalImage.src = exercise.image;
            modalImage.alt = exercise.name;
            modalImage.className = 'modal-exercise-image';
            imageContainer.appendChild(modalImage);
        }
    } else {
        console.error("Cannot find .exercise-video container in modal");
    }

    // --- Generate Day Selection Buttons ---
    const dayContainer = modal.querySelector('.day-selection-container');
    if(dayContainer) {
        generateButtons(dayContainer); // Call function to generate day buttons
    } else {
        console.error("[showExerciseModal] Could not find .day-selection-container.");
    }

    // Show modal
    modal.style.display = 'block';
}

// Function to generate day selection buttons inside the main modal
function generateButtons(container) {
    container.innerHTML = '';
    const days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
    const modalElement = container.closest('#exercise-modal');
    if (!modalElement) {
        console.error("Could not find parent modal (#exercise-modal) for day container");
        return;
    }
    const storedExerciseData = modalElement.dataset.exerciseData;

    if (!storedExerciseData) {
        console.error("Could not find stored exercise data on modal when generating buttons.");
        return;
    }

    days.forEach(dayName => {
        const button = document.createElement('button');
        button.textContent = dayName;
        button.className = 'day-select-btn';
        const dayValue = dayName.toLowerCase();
        button.dataset.day = dayValue;

        button.addEventListener('click', () => {
            try {
                const exerciseToAdd = JSON.parse(storedExerciseData);
                // Close the main modal
                modalElement.style.display = 'none';
                // Show the prompt modal instead of directly adding
                showSetsRepsPrompt(exerciseToAdd, dayValue);
            } catch (e) {
                console.error("Error parsing stored exercise data on day button click:", e);
            }
        });
        container.appendChild(button);
    });
}

// New function to show the sets/reps prompt modal
let currentPromptHandler = null; // To store the event handler

function showSetsRepsPrompt(exercise, day) {
    const promptModal = document.getElementById('sets-reps-prompt');
    const exerciseNameEl = document.getElementById('prompt-exercise-name');
    const setsInput = document.getElementById('prompt-sets');
    const repsInput = document.getElementById('prompt-reps');
    const weightInput = document.getElementById('prompt-weight');
    const confirmBtn = document.getElementById('confirm-add-exercise-btn');
    const closeBtn = promptModal.querySelector('.close-prompt-btn');

    if (!promptModal || !exerciseNameEl || !setsInput || !repsInput || !weightInput || !confirmBtn || !closeBtn) {
        console.error("Could not find all required elements for the sets/reps prompt.");
        return;
    }

    // Set exercise name in the prompt title
    exerciseNameEl.textContent = `Enter Sets and Reps for ${exercise.name}`; 
    // Reset to default values
    setsInput.value = 3;
    repsInput.value = 10;
    weightInput.value = 5;

    // Remove previous listener if exists to prevent duplicates
    if (currentPromptHandler) {
        confirmBtn.removeEventListener('click', currentPromptHandler);
    }

    // Define the new handler for this specific exercise and day
    currentPromptHandler = () => {
        const sets = parseInt(setsInput.value, 10);
        const reps = parseInt(repsInput.value, 10);
        const weight = parseInt(weightInput.value, 10);

        if (isNaN(sets) || sets <= 0) {
            alert("Please enter a valid number for sets.");
            return;
        }
        if (isNaN(reps) || reps <= 0) {
            alert("Please enter a valid number for reps.");
            return;
        }
        if (isNaN(weight) || weight <= 0) {
            alert("Please enter a valid number for weight.");
            return;
        }

        addExerciseToDay(exercise, day, sets, reps, weight); // Add with entered sets/reps
        promptModal.style.display = 'none'; // Hide prompt after adding
    };

    // Add the new event listener to the confirm button
    confirmBtn.addEventListener('click', currentPromptHandler);

    // Add listener for the close button (simple hide)
     const closeHandler = () => {
        promptModal.style.display = 'none';
        closeBtn.removeEventListener('click', closeHandler); // Clean up listener
        // Also remove the confirm button listener if the prompt is closed without confirming
        if (currentPromptHandler) {
             confirmBtn.removeEventListener('click', currentPromptHandler);
             currentPromptHandler = null;
        }
    };
    closeBtn.addEventListener('click', closeHandler);

    // Show the prompt modal
    promptModal.style.display = 'block';
}

// Modified addExerciseToDay to include sets and reps
function addExerciseToDay(exercise, day, sets, reps, weight) {
    const lowerCaseDay = day.toLowerCase();
    const slot = document.querySelector(`.workout-slot[data-day="${lowerCaseDay}"]`);

            if (slot) {
        console.log(`[addExerciseToDay] Adding exercise to slot for ${lowerCaseDay}:`, exercise, `Sets: ${sets}, Reps: ${reps}, weight: ${weight}`);
                const exerciseElement = document.createElement('div');
                exerciseElement.className = 'workout-exercise';
        const caloriesPerSet = Number(exercise.calories) || 0;
        const totalCalories = caloriesPerSet * sets;

        // Store sets, reps and BASE calories per set as data attributes
        exerciseElement.dataset.sets = sets;
        exerciseElement.dataset.reps = reps;
        exerciseElement.dataset.weight = weight;
        exerciseElement.dataset.caloriesPerSet = caloriesPerSet;

                exerciseElement.innerHTML = `
            <h4 class="exercise-name">${exercise.name}</h4>
            <p class="exercise-sets-reps">${sets} sets x ${reps} reps</p>
            <p class="exercise-weight">${weight}kg</p>
            <p class="exercise-calories-info">${totalCalories} calories (${caloriesPerSet}/set)</p> <!-- Display total and per set -->
            <button class="remove-exercise-btn">&times;</button>
        `;
        // Append element first
                slot.appendChild(exerciseElement);

        // --- Real-time Chart Update (Now using total calories) ---
        if (window.calorieChart) {
            const days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
            const dayIndex = days.indexOf(lowerCaseDay);
            if (dayIndex !== -1) {
                // Add the TOTAL calories for this exercise (sets * caloriesPerSet)
                const currentCalories = window.calorieChart.data.datasets[0].data[dayIndex] || 0;
                window.calorieChart.data.datasets[0].data[dayIndex] = currentCalories + totalCalories;
                window.calorieChart.update(); // Update chart immediately
                console.log(`[addExerciseToDay] Chart updated for day ${dayIndex}. Added ${totalCalories} calories. New total: ${currentCalories + totalCalories}`);
            }
        }
        // --- End Real-time Chart Update ---

        // Save after updating chart and adding to DOM
        saveWorkoutPlan();

    } else {
        console.error(`[addExerciseToDay] Could not find slot for day: ${lowerCaseDay}`);
        alert(`Error: Could not find the planner slot for ${day}.`);
    }
}

// Modified loadWorkoutPlan
async function loadWorkoutPlan() {
    try {
        const response = await fetch(WORKOUT_PLAN_API_URL);
        if (!response.ok) {
            if (response.status === 404) {
                console.log("[loadWorkoutPlan] No existing plan found on server (404). Initializing empty chart.");
                initializeCalorieChart();
                const slotsContainer = document.getElementById('workout-slots');
                if (slotsContainer) {
                    slotsContainer.querySelectorAll('.workout-slot .workout-exercise').forEach(el => el.remove());
                }
                return;
            }
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const planData = await response.json();

        const slotsContainer = document.getElementById('workout-slots');
        slotsContainer.querySelectorAll('.workout-slot .workout-exercise').forEach(el => el.remove());

        initializeCalorieChart(); // Re-initialize or clear the chart data

        const days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
        let chartData = Array(7).fill(0); // Initialize chart data array

        console.log("[loadWorkoutPlan] Fetched plan data:", planData);

        for (const day in planData) {
            const lowerCaseDay = day.toLowerCase();
            if (!days.includes(lowerCaseDay)) continue;

            const dayIndex = days.indexOf(lowerCaseDay);
            const slot = slotsContainer.querySelector(`.workout-slot[data-day="${lowerCaseDay}"]`);

            if (slot && Array.isArray(planData[day])) {
                let dayTotalCalories = 0;
                planData[day].forEach(exercise => {
                    // Backend now returns sets/reps reliably
                    const sets = parseInt(exercise.sets, 10) || 1; // Default to 1 set if parsing fails
                    const reps = parseInt(exercise.reps, 10) || 1; // Default to 1 rep
                    const weight = parseInt(exercise.weight, 10) || 5; // Default to 5kg
                    const caloriesPerSet = Number(exercise.calories) || 0;
                    const totalCalories = caloriesPerSet * sets;

                    const exerciseElement = document.createElement('div');
                    exerciseElement.className = 'workout-exercise';
                    exerciseElement.dataset.sets = sets;
                    exerciseElement.dataset.reps = reps;
                    exerciseElement.dataset.weight = weight;
                    exerciseElement.dataset.caloriesPerSet = caloriesPerSet;

                    exerciseElement.innerHTML = `
                        <h4 class="exercise-name">${exercise.name}</h4>
                        <p class="exercise-sets-reps">${sets} sets x ${reps} reps</p>
                        <p class="exercise-weight">${weight}kg</p>
                        <p class="exercise-calories-info">${totalCalories} calories (${caloriesPerSet}/set)</p>
                        <button class="remove-exercise-btn">&times;</button>
                    `;
                    slot.appendChild(exerciseElement);
                    // Add TOTAL calories for this exercise to the day's total for the chart
                    dayTotalCalories += totalCalories;
                });

                // Update chart data array for the corresponding day
                if (dayIndex !== -1) {
                    chartData[dayIndex] = dayTotalCalories;
                    console.log(`[loadWorkoutPlan] Calculated total calories for day ${dayIndex} (${day}): ${dayTotalCalories}`);
                }
            } else if (!Array.isArray(planData[day])) {
                console.warn(`[loadWorkoutPlan] Data for day '${day}' is not an array:`, planData[day]);
            } else {
                 console.warn(`[loadWorkoutPlan] Could not find slot DOM element for day: ${lowerCaseDay}`);
            }
        }

        // Update chart with the accumulated data
        if (window.calorieChart) {
             window.calorieChart.data.datasets[0].data = chartData;
            console.log(`[loadWorkoutPlan] Final chart data before update:`, JSON.stringify(chartData));
            window.calorieChart.update();
            console.log("[loadWorkoutPlan] Chart updated successfully after loading plan");
        } else {
            console.error("[loadWorkoutPlan] Chart instance does not exist after data population");
        }

    } catch (error) {
        console.error("Error loading workout plan:", error);
        if (!window.calorieChart) {
             initializeCalorieChart();
        }
    }
}

// Modified saveWorkoutPlan to ensure correct data is sent
async function saveWorkoutPlan() {
    console.log("[saveWorkoutPlan] Attempting to save workout plan...");
    const workoutPlan = {};
    const days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];

    days.forEach(day => {
        // Corrected selector: Find the .workout-slot within the .day-column div with id=day
        // Note: The HTML structure is actually <div class="day-column"> Monday <div class="workout-slot" data-day="monday">...</div> </div>
        // So we need to select based on the data-day attribute of the slot itself.
        const workoutSlotElement = document.querySelector(`.workout-slot[data-day="${day}"]`);


        if (!workoutSlotElement) {
            console.warn(`[saveWorkoutPlan] Workout slot element for day '${day}' not found.`);
            return; // Skip if the slot doesn't exist
        }
        const exercises = [];
        // Find exercises *within* the correct workout slot
        workoutSlotElement.querySelectorAll(`.workout-exercise`).forEach(exerciseElement => {
            const nameElement = exerciseElement.querySelector('.exercise-name'); // Selects <h4>

            // Read data directly from the dataset attributes of the exerciseElement
            const caloriesPerSet = exerciseElement.dataset.caloriesPerSet ? parseInt(exerciseElement.dataset.caloriesPerSet, 10) : 0;
            const sets = exerciseElement.dataset.sets ? parseInt(exerciseElement.dataset.sets, 10) : 0;
            const reps = exerciseElement.dataset.reps ? parseInt(exerciseElement.dataset.reps, 10) : 0;
            const weight = exerciseElement.dataset.weight ? parseInt(exerciseElement.dataset.weight, 10) : 5;


            if (nameElement && nameElement.textContent.trim()) {
                 const name = nameElement.textContent.trim();

                 // Basic validation for numeric values (already parsed or defaulted to 0)
                 if (Number.isNaN(caloriesPerSet) || Number.isNaN(sets) || Number.isNaN(reps) || Number.isNaN(weight)) {
                     console.warn(`[saveWorkoutPlan] Invalid numeric data found for ${name} on ${day}. Skipping.`);
                     return; // Skip this exercise if data is invalid
                 }

                 // Push data using the correct field names expected by backend ('calories' for calories_per_set)
                 exercises.push({
                     name: name,
                     calories: caloriesPerSet, // Map dataset.caloriesPerSet to 'calories' field for backend
                     sets: sets,
                     reps: reps,
                     weight: weight
                 });
                 console.log(`[saveWorkoutPlan] Extracted for ${day}: Name=${name}, CaloriesPerSet=${caloriesPerSet}, Sets=${sets}, Reps=${reps}, Weight=${weight}`);
             } else {
                console.warn(`[saveWorkoutPlan] Could not find name or data attributes on element:`, exerciseElement);
            }
        });
        if (exercises.length > 0) {
            workoutPlan[day] = exercises;
        }
    });

    console.log("[saveWorkoutPlan] Compiled workout plan data:", JSON.stringify(workoutPlan, null, 2));

    // Check if workoutPlan is empty before proceeding
    if (Object.keys(workoutPlan).length === 0) {
         console.log("[saveWorkoutPlan] No exercises found in any day slots. Sending request to clear plan.");
         // Allow sending an empty object if the intention is to clear the plan
    }


    // Get CSRF token from meta tag
    const csrfTokenMeta = document.querySelector('meta[name="csrf-token"]');
    const csrfToken = csrfTokenMeta ? csrfTokenMeta.getAttribute('content') : null;
    console.log("[saveWorkoutPlan] CSRF Token:", csrfToken); // Log the token

    if (!csrfToken) {
        console.error("[saveWorkoutPlan] CSRF token not found in meta tag!");
        alert("Error: CSRF token missing. Please refresh the page."); // Inform user
        return; // Stop if token is missing
    }

    try {
        const response = await fetch('/api/workout_plan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // Add CSRF token header
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(workoutPlan) // Send the potentially empty workoutPlan object
        });

        // Log raw response text for debugging non-JSON errors (like the HTML error page)
         const responseText = await response.text();
         console.log("[saveWorkoutPlan] Raw server response:", responseText);


        if (!response.ok) {
             // Try parsing as JSON, but fall back to text if it fails
            let errorData;
            try {
                errorData = JSON.parse(responseText); // Try parsing the text as JSON
            } catch (e) {
                 // If parsing failed, use the raw text in the details
                 errorData = { error: `Server returned non-JSON error (Status: ${response.status})`, details: responseText };
            }
             console.error('[saveWorkoutPlan] Server responded with error:', response.status, errorData);
             // Display a more user-friendly error if possible
             const errorMessage = errorData.error || `HTTP error! status: ${response.status}`;
             // Check if details exist and are not empty before appending
             const errorDetails = errorData.details && errorData.details.trim() ? `- ${errorData.details}` : '(No further details)';
             // Throw the error to be caught by the calling function or the catch block below
             throw new Error(`Error saving workout plan: ${errorMessage} ${errorDetails}`);
        }

         // If response is OK, parse the JSON response
        const result = JSON.parse(responseText);
         console.log('[saveWorkoutPlan] Workout plan saved successfully:', result);

         // Reload the plan ONLY if the save was successful
         await loadWorkoutPlan(); // Reload plan to reflect changes and update chart


    } catch (error) {
        // Log the error caught from the fetch operation or thrown due to !response.ok
        console.error('[saveWorkoutPlan] Error during fetch operation:', error);
        // Display error to user
        alert(`Failed to save workout plan: ${error.message}`); // Provide feedback to user
    }
} 

// Add save workout button event listener
const saveWorkoutBtn = document.getElementById('saveWorkoutBtn');
if (saveWorkoutBtn) {
    saveWorkoutBtn.addEventListener('click', handleSaveWorkoutClick);
}

// Add event listeners for the save confirmation modal
const saveConfirmationModal = document.getElementById('save-confirmation-modal');
if (saveConfirmationModal) {
    // Close modal when clicking the X
    saveConfirmationModal.querySelector('.close-modal').addEventListener('click', () => {
        saveConfirmationModal.style.display = 'none';
    });

    // Close modal when clicking outside
    window.addEventListener('click', (event) => {
        if (event.target === saveConfirmationModal) {
            saveConfirmationModal.style.display = 'none';
        }
    });

    // Handle cancel button
    document.getElementById('cancel-save-btn').addEventListener('click', () => {
        saveConfirmationModal.style.display = 'none';
    });

    // Handle confirm button
    document.getElementById('confirm-save-btn').addEventListener('click', () => {
        saveConfirmationModal.style.display = 'none';
        saveWorkout();
    });
}

function handleSaveWorkoutClick() {
    const saveConfirmationModal = document.getElementById('save-confirmation-modal');
    if (saveConfirmationModal) {
        saveConfirmationModal.style.display = 'block';
    }
}

async function saveWorkout() {
    try {
        // Get CSRF token
        const csrfTokenMeta = document.querySelector('meta[name="csrf-token"]');
        const csrfToken = csrfTokenMeta ? csrfTokenMeta.getAttribute('content') : null;

        if (!csrfToken) {
            console.error("[saveWorkout] CSRF token not found!");
            alert("Error: Security token missing. Please refresh the page.");
            return;
        }

        // Get week offset from the week-select dropdown
        const weekSelect = document.getElementById('week-select');
        const weekOffset = weekSelect ? parseInt(weekSelect.value, 10) : 0;

        // Show loading state
        const saveBtn = document.getElementById('saveWorkoutBtn');
        const originalText = saveBtn.innerHTML;
        saveBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Saving...';
        saveBtn.disabled = true;

        const response = await fetch('/api/save_workout', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({
                week_offset: weekOffset
            })
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || 'Failed to save workout');
        }

        // Show success message
        alert('Workout saved successfully!');
        
        // Reset button state
        saveBtn.innerHTML = originalText;
        saveBtn.disabled = false;

    } catch (error) {
        console.error('[saveWorkout] Error:', error);
        alert(error.message || 'Failed to save workout. Please try again.');
        
        // Reset button state
        const saveBtn = document.getElementById('saveWorkoutBtn');
        saveBtn.innerHTML = '<i class="fas fa-save"></i> Save This Week\'s Workout';
        saveBtn.disabled = false;
    }
}

async function loadSavedWorkout() {
    try {
        const response = await fetch("/api/saved_workout");
        if (!response.ok) {
            if (response.status === 404) {
                console.log("[loadWorkoutPlan] No existing plan found on server (404). Initializing empty chart.");
                const slotsContainer = document.getElementById('saved_workout');
                if (slotsContainer) {
                    slotsContainer.querySelectorAll('.workout-slot .workout-exercise').forEach(el => el.remove());
                }
                return;
            }
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const planData = await response.json();

        const slotsContainer = document.getElementById('saved_workout');
        slotsContainer.querySelectorAll('.workout-slot .workout-exercise').forEach(el => el.remove());

        const days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];

        console.log("[loadWorkoutPlan] Fetched plan data:", planData);

        for (const day in planData) {
            const lowerCaseDay = day.toLowerCase();
            if (!days.includes(lowerCaseDay)) continue;

            const dayIndex = days.indexOf(lowerCaseDay);
            const slot = slotsContainer.querySelector(`.workout-slot[data-day="${lowerCaseDay}"]`);

            if (slot && Array.isArray(planData[day])) {
                planData[day].forEach(exercise => {
                    // Backend now returns sets/reps reliably
                    const sets = parseInt(exercise.sets, 10) || 1; // Default to 1 set if parsing fails
                    const reps = parseInt(exercise.reps, 10) || 1; // Default to 1 rep
                    const weight = parseInt(exercise.weight, 10) || 5; // Default to 5kg

                    const exerciseElement = document.createElement('div');
                    exerciseElement.className = 'workout-exercise';
                    exerciseElement.dataset.sets = sets;
                    exerciseElement.dataset.reps = reps;
                    exerciseElement.dataset.weight = weight;
                    exerciseElement.innerHTML = `
                        <h4 class="exercise-name">${exercise.name}</h4>
                        <p class="exercise-sets-reps">${sets} sets x ${reps} reps</p>
                        <p class="exercise-weight">${weight}kg</p>
                    `;
                    slot.appendChild(exerciseElement);
                });

            } else if (!Array.isArray(planData[day])) {
                console.warn(`[loadWorkoutPlan] Data for day '${day}' is not an array:`, planData[day]);
            } else {
                 console.warn(`[loadWorkoutPlan] Could not find slot DOM element for day: ${lowerCaseDay}`);
            }
        }

    } catch (error) {
        console.error("Error loading workout plan:", error);
    }
}