import Home from "@/pages/Home.vue";
import {createRouter, createWebHistory} from "vue-router";
import Topics from "@/pages/TopicsList.vue";
import Students from "@/pages/Students.vue";
import Events from "@/pages/Events.vue";
import Links from "@/pages/Links.vue";
import ValueTypes from "@/topics/ValueTypes.vue";
import VariableAssignmentStatement from "@/topics/VariableAssignmentStatement.vue";
import DataOutput from "@/topics/DataOutput.vue";
import DataInput from "@/topics/DataInput.vue";
import ArithmeticOperations from "@/topics/ArithmeticOperations.vue";
import ConditionalStatement from "@/topics/ConditionalStatement.vue";
import LoopStatement from "@/topics/LoopStatement.vue";

const topics = [
    {path: '/topics/1', component: ValueTypes},
    {path: '/topics/2', component: VariableAssignmentStatement},
    {path: '/topics/3', component: DataOutput},
    {path: '/topics/4', component: DataInput},
    {path: '/topics/5', component: ArithmeticOperations},
    {path: '/topics/6', component: ConditionalStatement},
    {path: '/topics/7', component: LoopStatement},
]

const routes = [
    {path: '/', component: Home},
    {path: '/topics', component: Topics},
    ...topics,
    {path: '/students', component: Students},
    {path: '/events', component: Events},
    {path: '/links', component: Links},
]

const router = createRouter({
    history: createWebHistory('/kcdim/'),
    routes,
    scrollBehavior(to, from, savedPosition) {
        return {
            top: 0,
        }
    },
})

export default router;